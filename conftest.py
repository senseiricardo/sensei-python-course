import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailPage
from config.config import BASE_URL

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
    
    driver.get(BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def product_details(driver):
    return ProductDetailPage(driver)