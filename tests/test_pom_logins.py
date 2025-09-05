from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_01_pom(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Validar que estes en la pagina de Products
    assert "inventory" in driver.current_url

def test_login_04_pom(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")
    # Guardar el valor de el mensaje de error
    error_message = login_page.get_error_message()
    # Validar el mensaje de error
    assert "Epic sadface: Username is required" == error_message, f"El mensaje de error {error_message} es invalido"

