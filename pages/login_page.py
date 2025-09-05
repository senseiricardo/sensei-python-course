from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # OBJECTS
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    # CUSTOM FUNCTIONS
    def login(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)
        #self.implicit_wait(self, 10)
    
    def get_error_message(self):
        return self.find(*self.ERROR_MESSAGE).text