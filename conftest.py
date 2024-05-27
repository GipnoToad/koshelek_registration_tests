import pytest
from selenium import webdriver

def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--headless", action="store_true", 
                     help="Start browser in headless mode")


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):
    options = webdriver.ChromeOptions()
    headless = request.config.getoption("headless")
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()