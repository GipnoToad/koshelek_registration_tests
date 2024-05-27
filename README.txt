# Registration Page Automated Tests

This project contains automated tests for the registration page of a web application using Selenium and pytest. The tests are designed to verify various aspects of the registration form, such as input validation for username, email, password, and referral code fields.

## Project Structure

Registration_tests/
├── config/
│   ├── __init__.py
│   ├── config.py
│   ├── test_data.py
│   └── constants.py
├── pages/
│   ├── _locators.py
│   ├── base_page.py
│   └── registration_page.py
├── tests/
│   └── test_registration_page.py
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
├── install.bat
├── run_smoke_tests.bat
├── run_negative_tests.bat
├── run_all_tests.bat
└── test_logs.log

## Key Components
- **config/**: Contains configuration files and test data.
  - `config.py`: Contains configuration variables such as the URL of the registration page.
  - `test_data.py`: Contains test data for negative test cases, including invalid values and expected error messages.
  - `constants.py`: Defines constant error messages used in the tests.
- **pages/**: Contains page object model (POM) classes and locators for the registration page.
  - `_locators.py`: Defines locators used in the registration page.
  - `base_page.py`: Contains base methods and functionalities shared across different page objects.
  - `registration_page.py`: Implements the POM for the registration page, including methods to interact with form fields and retrieve error messages.
- **tests/**: Contains test cases for the registration page.
  - `test_registration_page.py`: Defines the test cases for the registration page, including smoke and negative tests. Utilizes logging to track test execution.
- `conftest.py`: Configuration file for pytest fixtures.
- `pytest.ini`: Configuration file for pytest settings.
- `README.md`: This file.
- `requirements.txt`: List of dependencies required to run the tests.
- `install.bat`: Batch script to create and activate a virtual environment and install dependencies.
- `run_smoke_tests.bat`: Batch script to run smoke tests.
- `run_negative_tests.bat`: Batch script to run negative tests.
- `run_all_tests.bat`: Batch script to run all tests.
- `test_logs.log`: Log file for test execution results.

## Installation and Setup

### Prerequisites

- Python 3.7+
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Step-by-Step Guide

1. **Clone the Repository or Unzip**:

    ```sh
    git clone <repository_url>
    ```

2. **Create and Activate a Virtual Environment, Install Dependencies**:

    Launch `install.bat`.

3. **Run Tests**:

    - **All Tests**:
    
      Launch `run_all_tests.bat`.

    - **Smoke Tests**:
    
      Launch `run_smoke_tests.bat`.

    - **Negative Tests**:
    
      Launch `run_negative_tests.bat`.

4. **Delete Virtual Environment**:

    Delete the "venv" folder manually.

5. **Reinstall and Activate a Virtual Environment, Install Dependencies**:

    Delete the "venv" folder manually and then launch `install.bat`.

## Running Tests

- **Smoke Tests**: Validate basic functionality and accessibility of the registration page.
- **Negative Tests**: Verify input validation by providing invalid data and checking for appropriate error messages.

## Checking Logs

Test logs are recorded in the file `test_logs.log`, located in the root directory of the project. Open this file to check the test execution results.

## Dependencies

- `pytest==8.0.0`
- `selenium==4.16.0`