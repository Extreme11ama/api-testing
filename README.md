# API Testing Automation Project

Automated API test suite built with Python, testing the JSONPlaceholder REST API.

## Tools
- Python
- Requests
- PyTest

## Test Coverage
- GET /posts
- GET /posts/{id}
- POST /posts
- PUT /posts/{id}
- DELETE /posts/{id}

## Test Cases
- Status code validation
- Response data validation
- Schema validation
- Response time performance testing
- Parameterized testing across multiple IDs
- Negative testing with invalid IDs
- Negative testing with missing fields

## PyTest Features Used
- Fixtures for reusable client setup
- Parametrize for data driven testing
- Logging for test execution visibility

## Run Tests
### run all tests
pytest

### run with logs visible
pytest -s