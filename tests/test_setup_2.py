from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_01():
    # 1️⃣ Configuración inicial del driver
    driver = webdriver.Chrome()
    #driver.maximize_window()

    # 2️⃣ Navegar al sitio
    driver.get("https://www.saucedemo.com/")

    # 3️⃣ Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 4️⃣ Verificar que se ha iniciado sesión correctamente
    assert "inventory" in driver.current_url

    # 5️⃣ Cerrar sesión
    time.sleep(2)
    driver.quit()