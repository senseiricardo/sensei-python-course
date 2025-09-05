from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    # Objects
    PRODUCT_NAME = (By.XPATH, "(//*[@data-test='inventory-item-name'])[1]")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")

    # Custom functions
    def click_first_product(self):
        self.click(*self.PRODUCT_NAME)

    def get_product_name(self):
        return self.find(*self.PRODUCT_NAME).text
    
    def go_back(self):
        self.click(*self.BACK_TO_PRODUCTS_BUTTON)