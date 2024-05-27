# Defines the test cases for the registration page.
import pytest
import logging
from pages.registration_page import RegistrationPage
from config import constants, config, test_data

# Setting up logging
log_file = 'test_logs.log'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('Logging setup complete')

url = config.url

# Mapping fields to their respective methods
field_method_map = {
    "username": "fill_username",
    "email": "fill_email",
    "password": "fill_password",
    "referral_code": "fill_referral_code"
}

logging.debug('Field method map initialized')

@pytest.mark.smoke
def test_user_can_access_registration_page(browser):
    logging.info("Starting test: test_user_can_access_registration_page")
    page = RegistrationPage(browser, url)
    page.open()
    page.is_registration_page()
    logging.info("Test passed: test_user_can_access_registration_page")

@pytest.mark.negative
@pytest.mark.parametrize("field,value,expected_result,error_method", [
    (test["field"], test["value"], getattr(constants, test["expected_result"]), test["error_method"]) 
    for test in test_data.negative_tests if test["field"] != "referral_code"
])
def test_negative_cases(browser, field, value, expected_result, error_method):
    logging.info(f"Starting test for field: {field} with value: {value}")
    page = RegistrationPage(browser, url)
    page.open()

    # Filling the corresponding field using the field_method_map dictionary
    logging.info(f"Filling the {field}")
    fill_method = getattr(page, field_method_map[field])
    fill_method(value)

    # Clicking the submit button
    logging.info("Clicking submit button")
    page.click_submit_button()

    # Getting the error message using the provided error_method
    error_message = getattr(page, error_method)()
    
    # Checking the error message
    page.text_as_expected_text(error_message, expected_result)

    logging.info(f"Test passed for field: {field} with value: {value}")

@pytest.mark.negative
@pytest.mark.parametrize("value,expected_result,error_method", [
    (test["value"], getattr(constants, test["expected_result"]), test["error_method"]) 
    for test in test_data.negative_tests if test["field"] == "referral_code"
])
def test_referral_code(browser, value, expected_result, error_method):
    logging.info(f"Starting test for referral_code with value: {value}")
    page = RegistrationPage(browser, url)
    page.open()

    # Filling the referral code field
    logging.info("Filling the referral code")
    page.fill_referral_code(value)

    # Getting the error message using the provided error_method
    error_message = getattr(page, error_method)()

    # Checking the error message
    page.text_as_expected_text(error_message, expected_result)

    # Ensure the submit button is unclickable
    page.is_submit_button_is_unclickable()

    logging.info(f"Test passed for referral_code with value: {value}")