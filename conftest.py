import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-blink-features=AutomationControlled")

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Unsupported browser")
    
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()