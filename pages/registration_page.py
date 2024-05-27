# Defines the page object model for the registration page.
from pages._locators import RegistrationPageLocators
from .base_page import BasePage

class RegistrationPage(BasePage):
    def is_registration_page(self):
        """Verifies the registration page title is displayed correctly."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.element_is_visible_in_shadow_root(shadow_root, RegistrationPageLocators.REGISTRATION_PAGE_TITLE)
        shadow_title = self.find_element_in_shadow_root(shadow_root, RegistrationPageLocators.REGISTRATION_PAGE_TITLE)
        self.text_as_expected_text(shadow_title.text, "Регистрация")

    def fill_username(self, username):
        """Fills the username field with the provided username."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.fill_field_in_shadow_root(shadow_root, RegistrationPageLocators.USERNAME_FIELD, username)

    def get_username_error(self):
        """Returns the username error message text."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        return self.get_text_from_shadow_root(shadow_root, RegistrationPageLocators.USERNAME_FIELD_ERROR)

    def fill_email(self, email):
        """Fills the email field with the provided email."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.fill_field_in_shadow_root(shadow_root, RegistrationPageLocators.EMAIL_FIELD, email)

    def get_email_error(self):
        """Returns the email error message text."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        return self.get_text_from_shadow_root(shadow_root, RegistrationPageLocators.EMAIL_FIELD_ERROR)

    def fill_password(self, password):
        """Fills the password field with the provided password."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.fill_field_in_shadow_root(shadow_root, RegistrationPageLocators.PASSWORD_FIELD, password)

    def get_password_error(self):
        """Returns the password error message text."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        return self.get_text_from_shadow_root(shadow_root, RegistrationPageLocators.PASSWORD_FIELD_ERROR)

    def fill_referral_code(self, code):
        """Fills the referral code field with the provided code."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.fill_field_in_shadow_root(shadow_root, RegistrationPageLocators.REFERRAL_CODE_FIELD, code)

    def get_referral_code_error(self):
        """Returns the referral code error message text."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        return self.get_text_from_shadow_root(shadow_root, RegistrationPageLocators.REFERRAL_CODE_FIELD_ERROR)
    
    def is_submit_button_is_clickable(self):
        """Verifies the submit button is clickable."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        assert self.element_is_clickable_in_shadow_root(shadow_root, RegistrationPageLocators.SUBMIT_BUTTON), f"Submit button with locator {RegistrationPageLocators.SUBMIT_BUTTON} is unclickable"

    def is_submit_button_is_unclickable(self):
        """Verifies the submit button is unclickable."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)      
        assert not self.element_is_clickable_in_shadow_root(shadow_root, RegistrationPageLocators.SUBMIT_BUTTON), f"Submit button with locator {RegistrationPageLocators.SUBMIT_BUTTON} is clickable"

    def click_submit_button(self):
        """Clicks the submit button."""
        shadow_root = self.open_shadow_root(RegistrationPageLocators.SHADOW_ROOT)
        self.click_element_in_shadow_root(shadow_root, RegistrationPageLocators.SUBMIT_BUTTON)