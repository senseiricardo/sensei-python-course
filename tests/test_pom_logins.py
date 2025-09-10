from utils.data_loader import load_users

def test_login_01_pom(login_page):
    user = load_users()
    username = user["valid_user"]["username"]
    password = user["valid_user"]["password"]
    login_page.login(username, password)
    # Validar que estes en la pagina de Products
    assert "inventory" in login_page.driver.current_url

def test_login_04_pom(login_page):
    #login_page = LoginPage(driver) --> Eliminar esta linea que esta duplicada
    login_page.login("", "")
    # Guardar el valor de el mensaje de error
    error_message = login_page.get_error_message()
    # Validar el mensaje de error
    assert "Epic sadface: Password is required" == error_message, f"El mensaje de error {error_message} es invalido"

