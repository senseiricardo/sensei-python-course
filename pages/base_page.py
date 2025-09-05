from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
    
    def type(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def click(self, by, locator):
        self.find(by, locator).click()

    def wait_for_element_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def implicit_wait(self, timeout):
        self.implicit_wait(timeout)