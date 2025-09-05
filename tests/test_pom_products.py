from pages.product_details_page import ProductDetailPage
from pages.login_page import LoginPage

def test_product_pom_07(driver):
    login_page = LoginPage(driver)
    product_details = ProductDetailPage(driver)

    login_page.login("standard_user", "secret_sauce")
    product_details.click_first_product()

    product_name = product_details.get_product_name()
    assert "Backpack" in product_name

    product_details.go_back()
    assert "inventory" in driver.current_url
