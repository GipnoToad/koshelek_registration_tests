# Defines the base page class with common methods used across different page objects.
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common import exceptions

class BasePage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url
        self.actions = ActionChains(self.browser)

    def open(self):
        """Opens the specified URL in the browser."""
        self.browser.get(self.url)

    def open_shadow_root(self, locator: tuple):
        """Opens and returns the shadow root element for the given locator."""
        try:
            shadow_host = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(locator)
            )
            return self.browser.execute_script('return arguments[0].shadowRoot', shadow_host)
        except Exception as e:
            raise Exception(f"Error locating shadow root for {locator}. Exception: {e}")

    def find_element_in_shadow_root(self, shadow_root, locator: tuple):
        """Finds and returns an element within the shadow root."""
        try:
            return shadow_root.find_element(*locator)
        except Exception as e:
            raise Exception(f"Element {locator} not found in shadow root. Exception: {e}")

    def element_is_visible_in_shadow_root(self, shadow_root, locator: tuple, wait=5):        
        """Checks if an element is visible within the shadow root."""
        try:
            element = self.find_element_in_shadow_root(shadow_root, locator)
            WebDriverWait(self.browser, wait).until(EC.visibility_of(element))
            return True
        except Exception as e:
            raise Exception(f"Element {locator} is not visible in shadow root. Exception: {e}")

    def fill_field_in_shadow_root(self, shadow_root, locator: tuple, value: str):
        """Fills a text field within the shadow root with the given value."""
        try:
            element = self.find_element_in_shadow_root(shadow_root, locator)
            element.clear()
            element.send_keys(value)
        except Exception as e:
            raise Exception(f"Unable to fill field {locator}. Exception: {e}")

    def click_element_in_shadow_root(self, shadow_root, locator: tuple):
        """Clicks an element within the shadow root."""
        try:
            element = self.find_element_in_shadow_root(shadow_root, locator)
            element.click()
        except Exception as e:
            raise Exception(f"Unable to click element {locator}. Exception: {e}")
        
    def element_is_clickable_in_shadow_root(self, shadow_root, locator: tuple):
        """Checks if an element is clickable within the shadow root."""
        try:
            element = self.find_element_in_shadow_root(shadow_root, locator)
            print(element.is_enabled())
            return element.is_enabled() and element.is_displayed()
        except Exception as e:
            raise Exception(f"Element {locator} is not clickable in shadow root. Exception: {e}")
        
    def get_text_from_shadow_root(self, shadow_root, locator: tuple):
        """Gets and returns the text of an element within the shadow root."""
        try:
            element = self.find_element_in_shadow_root(shadow_root, locator)
            return element.text
        except Exception as e:
            raise Exception(f"Unable to get text from element {locator}. Exception: {e}")
        
    def text_as_expected_text(self, text:str, expected_text: str):
        """Checks if a text on the page is the same as expected."""
        assert text == expected_text, f"{expected_text}. Фактический текст: {text}"