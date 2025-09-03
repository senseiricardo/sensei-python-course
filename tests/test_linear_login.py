from selenium import webdriver
from selenium.webdriver.common.by import By

# Buenas practicas para empezar a automatizar

# Ejecutar la prueba funcionalmente (manual testing)
# El test case depende de datos externos? 
    # SI : Puedo general el dato?
    # NO : Continua
    # Data estatico: No candidato a autmatizacion

# Pass rate - Pruebas pasadas en una ejecucion  -> 70% ->60%
# Sano 75% al 85%

# Antes de escribir el primer codigo buscar la reutilizacion

# PILARES AUTOMATIZACION -> 

# Mantenibilidad
# Reusabilidad
# Legibilidad
# Escalabilidad

# DESARROLLO

# 1- Obtener objetos -> Locators
# 2- Desarrollo del script en base al Patro de diseño
# 3- Ejecuciones

# Username -> ID -> user-name
# Password -> ID -> password
# Login - > ID -> login-button
# Header -> CLASS -> app_logo

def test_login_01():
    # Setup Chrome
    driver = webdriver.Chrome()

    # Navegar al sitio
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validar que estes en la pagina de Products
    assert "inventory" in driver.current_url

def test_login_04():
    # Setup Chrome
    driver = webdriver.Chrome()

    # Navegar al sitio
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()

    # Guardar el valor de el mensaje de error
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    # Validar el mensaje de error
    assert "Username is required" in error_message

    # XPATH ABSOLUTO /html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3
    # XPATH RELATIVO //h3[@data-test='error']



