# Defines the locators used in the registration page.
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    SHADOW_ROOT = (By.CSS_SELECTOR, ".remoteComponent")
    REGISTRATION_PAGE_TITLE = (By.CSS_SELECTOR, 'div[data-wi="title"]')
    USERNAME_FIELD = (By.CSS_SELECTOR, 'div[data-wi="user-name"] input')
    USERNAME_FIELD_ERROR = (By.CSS_SELECTOR, 'div[data-wi="user-name"] div[data-wi="message"] span')
    EMAIL_FIELD = (By.CSS_SELECTOR, "#username")
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, 'div[data-wi="identificator"] div[data-wi="message"] span')
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#new-password")
    PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, 'div[data-wi="password"] div[data-pw="auth-widget-password-input-message"] span')
    REFERRAL_CODE_FIELD = (By.CSS_SELECTOR, 'div[data-wi="referral"] input')
    REFERRAL_CODE_FIELD_ERROR = (By.CSS_SELECTOR, 'div[data-wi="referral"] div[data-wi="message"] span')
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, 'div[data-wi="user-agreement"] input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
