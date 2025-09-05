from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def test_product_07():
    # Setup Chrome
    #driver = get_driver(browser="chrome", headless=False)
    driver = get_driver()

    # EXPLICIT WAIT
    wait = WebDriverWait(driver, 10)

    # Navegar al sitio
    driver.get("https://www.saucedemo.com/")

    user = wait.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))

    # Login
    user.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # SLEEP - HARDWAIT
    time.sleep(1) # ⚠️ Tratar de evitarlo lo mas posible

    # IMPLICIT WAIT
    driver.implicitly_wait(10)

    # Validar que estes en la pagina de Products
    assert "inventory" in driver.current_url, f"la URL {driver.current_url} no contiene inventorio"

    # Assertion
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) > 0, "No se encontraron elementos en inventory page"

    # Seleccionar el primer producto
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()

    # Validar el product name
    wait_fluent = WebDriverWait(
        driver,
        timeout=15,
        poll_frequency=1
    )
    product_name= wait_fluent.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']"))).text
    #product_name = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text # CSS
    assert "Backpack" in product_name

    # Back to products
    driver.find_element(By.ID, "back-to-products").click()
    assert "inventory" in driver.current_url

    #inventory_item_name 
    #data-test="inventory-item-name"
    #id="back-to-products"

def get_driver(browser="chrome", headless=False):
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        # Opciones basicas para que no aparezcan los pop up alerts
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)

        # Evitar que el driver sepa que esta siendo controlado por un script
        options.add_argument("--disable-blink-features=AutomationControlled")

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options = options)
    else:
        raise ValueError("Browser not supported")
    return driver