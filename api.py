from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///test_case_database.db')
test_cases_table = db['test_cases']

def fetch_test_case(test_case_id):
    return test_cases_table.find_one(test_case_id=test_case_id)

def fetch_all_test_cases():
    return [dict(test_case) for test_case in test_cases_table.all()]

@app.route('/api/test_cases', methods=['GET', 'POST'])
def api_test_cases():
    """
    Endpoint for managing test cases.
    """
    if request.method == "GET":
        return make_response(jsonify(fetch_all_test_cases()), 200)
    elif request.method == 'POST':
        content = request.json

        # Validate required fields and their data types
        required_fields = ['test_case_id', 'name', 'description']
        for field in required_fields:
            if field not in content:
                return make_response(jsonify({"error": f"Missing required field: {field}"}), 400)
            if not isinstance(content[field], (int, str)):
                return make_response(jsonify({"error": f"Invalid data type for field {field}"}), 400)

        # Validate 'test_case_id' for new test cases
        if 'test_case_id' in content and not isinstance(content['test_case_id'], int) and content['test_case_id'] > 0:
            return make_response(jsonify({"error": "'test_case_id' must be a positive integer"}), 400)

        test_cases_table.insert(content)
        return make_response(jsonify(fetch_test_case(content['test_case_id'])), 201)

@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    """
    Populate the database with sample test cases.
    """
    test_cases_table.insert({
        "test_case_id": 1,
        "name": "First Test Case",
        "description": "This is the first test case."
    })

    test_cases_table.insert({
        "test_case_id": 2,
        "name": "Second Test Case",
        "description": "This is the second test case."
    })

    return make_response(jsonify(fetch_all_test_cases()), 200)

@app.route('/api/test_cases/<int:test_case_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_case(test_case_id):
    """
    Endpoint for managing a single test case.
    """
    with db as tx:
        test_case_obj = fetch_test_case(test_case_id)

    if request.method == "GET":
        if test_case_obj:
            return make_response(jsonify(test_case_obj), 200)
        else:
            return make_response(jsonify({"error": "Test case not found"}), 404)

    elif request.method == "PUT":
        content = request.json

        # Validate required fields and their data types
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in content:
                return make_response(jsonify({"error": f"Missing required field: {field}"}), 400)
            if not isinstance(content[field], (int, str)):
                return make_response(jsonify({"error": f"Invalid data type for field {field}"}), 400)

        # Validate 'test_case_id' data type
        if 'test_case_id' in content and not isinstance(content['test_case_id'], int):
            return make_response(jsonify({"error": "'test_case_id' must be an integer"}), 400)

        with db as tx:
            test_cases_table.update(content, ['test_case_id'])
            updated_test_case = fetch_test_case(test_case_id)

        return make_response(jsonify(updated_test_case), 200)

    elif request.method == "DELETE":
        with db as tx:
            test_cases_table.delete(test_case_id=test_case_id)

        return make_response(jsonify({}), 204)

if __name__ == '__main__':
    app.run(debug=True)
