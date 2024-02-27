# Test Case Management Flask API

This repository contains a Flask API for managing test cases and their execution results across multiple test assets. The data is stored in a SQLite database. The API exposes various endpoints for creating, retrieving, updating, and deleting test cases, as well as recording and retrieving execution results.

## Task Description

The goal of this project is to develop a Flask API that satisfies the following requirements:

1. **Database Setup**: Set up a SQLite database to store test cases and their execution results with an appropriate table schema.

2. **API Endpoints**:
   - Create a new test case and store it in the SQLite database.
   - Retrieve a list of all test cases from the SQLite database.
   - Retrieve a single test case by its ID from the SQLite database.
   - Update an existing test case in the SQLite database.
   - Delete a test case by its ID from the SQLite database.
   - Record the execution result of a test case for a specific test asset in the SQLite database.
   - Retrieve the execution results of all test cases for a specific test asset from the SQLite database.

3. **Data Validation and Error Handling**: Implement data validation and error handling for each API endpoint to ensure the required fields are present and have the correct data types.

4. **Unit Tests**: Write unit tests to ensure the functionality of each API endpoint.

## Repository Content

- `api.py`: The main Python file containing the implementation of the Flask API.
- `README.md`: This file, providing an overview of the project and instructions.

## Getting Started

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/test-case-management.git
   cd test-case-management
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   ```bash
   python api.py
   ```

4. **API Endpoints**:
   - Retrieve all test cases: [http://127.0.0.1:5000/api/test_cases](http://127.0.0.1:5000/api/test_cases)
   - Populate the database with sample test cases: [http://127.0.0.1:5000/api/db_populate](http://127.0.0.1:5000/api/db_populate)
   - For other endpoints, check the API documentation or refer to the `snippets/` folder.
  
## Snippets

Results of URL: http://127.0.0.1:5000/api/test_cases corresponding of endpoint '/api/test_cases'

![image](https://github.com/Nehalshetta/Flask-API/assets/63877578/1af613ae-348f-465f-99bf-45d7fbebf9f1)


Results of URL: http://127.0.0.1:5000/api/db_populate corresponding of endpoint '/api/db_populate'

![image](https://github.com/Nehalshetta/Flask-API/assets/63877578/212d3025-addb-4489-b814-74594e019a9c)


Results of URL: http://127.0.0.1:5000/api/1 corresponding of endpoint '/api/test_cases/<int:test_case_id>'

   *Test ID 1*
   
   ![image](https://github.com/Nehalshetta/Flask-API/assets/63877578/c28b6d75-bfe9-4b6c-87fd-a4803ad23114)
   
   
   
   *Test ID 2*
   
   ![image](https://github.com/Nehalshetta/Flask-API/assets/63877578/df5172f7-2672-4ada-a593-086a0302043a)









