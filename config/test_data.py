# config/test_data.py

negative_tests = [
    {
        "field": "username",
        "value": "abc",
        "expected_result": "USERNAME_ERROR_SHORT",
        "error_method": "get_username_error"
    },
    {
        "field": "username",
        "value": "",
        "expected_result": "USERNAME_ERROR_EMPTY",
        "error_method": "get_username_error"
    },
    {
        "field": "username",
        "value": "invalid@name",
        "expected_result": "USERNAME_ERROR_INVALID",
        "error_method": "get_username_error"
    },
    {
        "field": "email",
        "value": "",
        "expected_result": "EMAIL_ERROR_EMPTY",
        "error_method": "get_email_error"
    },
    {
        "field": "email",
        "value": "invalidemail",
        "expected_result": "EMAIL_ERROR_INVALID",
        "error_method": "get_email_error"
    },
    {
        "field": "password",
        "value": "",
        "expected_result": "PASSWORD_ERROR_EMPTY",
        "error_method": "get_password_error"
    },
    {
        "field": "password",
        "value": "short",
        "expected_result": "PASSWORD_ERROR_SHORT",
        "error_method": "get_password_error"
    },
    {
        "field": "password",
        "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1",
        "expected_result": "PASSWORD_ERROR_LONG",
        "error_method": "get_password_error"
    },
    {
        "field": "referral_code",
        "value": "123",
        "expected_result": "REFERRAL_CODE_ERROR_INVALID",
        "error_method": "get_referral_code_error"
    },
    {
        "field": "referral_code",
        "value": "123456789",
        "expected_result": "REFERRAL_CODE_ERROR_INVALID",
        "error_method": "get_referral_code_error"
    }
]