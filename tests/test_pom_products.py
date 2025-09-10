from pages.product_details_page import ProductDetailPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailPage

def test_product_pom_07(login_page, product_details):
    login_page.login("standard_user", "secret_sauce")
    product_details.click_first_product()

    product_name = product_details.get_product_name()
    assert "Backpack" in product_name

    product_details.go_back()
    assert "inventory" in login_page.driver.current_url

def test_product_pom_07_duplicated1(driver):
    login_page = LoginPage(driver) # ---> Usar el conftest.py
    product_details = ProductDetailPage(driver) # ---> Usar el conftest.py

    login_page.login("standard_user", "secret_sauce")
    product_details.click_first_product()

    product_name = product_details.get_product_name()
    assert "Backpack" in product_name

    product_details.go_back()
    assert "inventory" in driver.current_url

def test_product_pom_07_duplicated2(driver):
    login_page = LoginPage(driver)
    product_details = ProductDetailPage(driver)

    login_page.login("standard_user", "secret_sauce")
    product_details.click_first_product()

    product_name = product_details.get_product_name()
    assert "Backpack" in product_name

    product_details.go_back()
    assert "inventory" in driver.current_url
