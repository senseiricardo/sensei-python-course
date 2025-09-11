import pytest
import allure
import os
import tempfile
from datetime import datetime
from selenium import webdriver
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailPage
from config.config import BASE_URL

def pytest_addoption(parser):
    # Permite pasar --browser para definir el navegador (por ahora solo chrome)
    parser.addoption("--browser", action="store", default="chrome")
    # Permite usar --headless como un flag (no requiere valor)
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    # Agrega una opción de línea de comandos: --screenshot
    # Controla CUÁNDO adjuntar screenshots al reporte de Allure.
    parser.addoption(
        "--screenshot",
        action="store",
        default="fail",            # valor por defecto: solo en FAIL
        choices=("off", "fail", "pass", "always"),
        help="Cuándo adjuntar screenshots a Allure."
    )

@pytest.fixture(scope="function")
def driver(request):
    # Obtiene el valor del navegador desde la línea de comandos (por defecto: chrome)
    browser = request.config.getoption("--browser")
    # Verifica si se pasó el flag --headless
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        # 🔧 Configura opciones avanzadas de Chrome (para evitar popups de guardar contraseñas, etc.)
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)

        # 🕵️‍♂️ Oculta que Selenium está controlando el navegador (evita detección)
        options.add_argument("--disable-blink-features=AutomationControlled")

        # ✅ Solo activa headless si se pasó el flag en la terminal
        if headless:
            options.add_argument("--headless")

        # ✅ AGREGADO: ajustes solo cuando corre en CI (GitHub Actions)
        # - Fuerza headless para entornos de contenedor
        # - Asigna un user-data-dir temporal único (evita "already in use")
        # - Flags recomendados para Chrome en Linux/CI
        if os.getenv("CI", "").lower() == "true":
            options.add_argument("--headless=new")
            user_data_dir = tempfile.mkdtemp(prefix="chrome-profile-")
            options.add_argument(f"--user-data-dir={user_data_dir}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-first-run")
            options.add_argument("--no-default-browser-check")

        # 🧪 Crea el WebDriver de Chrome con las opciones anteriores
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Unsupported browser")

    # 🌐 Navega al sitio objetivo antes de cada test
    driver.get(BASE_URL)

    # 📤 Este yield entrega el driver al test, y después ejecuta driver.quit()
    yield driver

    # ❌ Cierra el navegador después del test
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def product_details(driver):
    return ProductDetailPage(driver)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que se ejecuta tras cada fase del test:
    - setup:   preparación del test
    - call:    ejecución del test
    - teardown:limpieza posterior

    Guardamos el resultado de cada fase (rep_setup/rep_call/rep_teardown)
    como atributos en el nodo del test para consultarlos después.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def _attach_artifacts(driver, name_prefix: str):
    """
    Helper: adjunta al reporte Allure dos cosas de la página actual:
    - Screenshot (PNG) en memoria (sin crear archivo intermedio)
    - HTML (page_source)

    'name_prefix' etiqueta el adjunto (e.g., "<test> - FAIL" o "<test> - PASS")
    y se añade un timestamp para distinguir múltiples capturas.
    """
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")

    # 1) Screenshot como PNG (bytes) directamente
    try:
        allure.attach(
            driver.get_screenshot_as_png(),               # bytes PNG
            name=f"{name_prefix} [{ts}] - Screenshot",    # nombre visible en Allure
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        # Si falla la captura, adjunta el error como texto para diagnosticar
        allure.attach(
            str(e),
            name=f"{name_prefix} - ERROR tomando screenshot",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2) HTML (DOM) de la página actual
    try:
        allure.attach(
            driver.page_source,                           # string HTML
            name=f"{name_prefix} [{ts}] - Page Source",
            attachment_type=allure.attachment_type.HTML
        )
    except Exception:
        # Si no hay page_source (p. ej., driver ya cerrado), lo omitimos
        pass


@pytest.fixture(autouse=True)
def _allure_screenshots(request):
    """
    Fixture AUTOUSE:
    - Se ejecuta para TODOS los tests sin que tengas que pedirlo.
    - Al FINALIZAR cada test, decide si adjunta evidencias (screenshot + HTML)
      según la política --screenshot y el resultado del test.

    IMPORTANTÍSIMO para el orden de teardown:
    Obtenemos la instancia de 'driver' ANTES del 'yield'. Esto establece
    una dependencia real con el fixture 'driver', lo cual garantiza que
    el teardown de este fixture AUTOUSE ocurra ANTES de que se destruya el driver.
    Así evitamos intentar capturar después de que el driver ya se cerró.
    """
    # Lee la política elegida por CLI o pytest.ini
    policy = request.config.getoption("--screenshot")

    # Intenta obtener el fixture 'driver' SOLO si el test lo usa.
    # Nota: request.fixturenames contiene los fixtures que el test pidió explícitamente.
    driver = None
    if "driver" in request.fixturenames:
        try:
            # Esto fuerza la dependencia y, por ende, el orden de teardown correcto.
            driver = request.getfixturevalue("driver")
        except Exception:
            driver = None

    # Dejamos que el test ejecute (setup -> call -> teardown)
    yield

    # Si la política es 'off' o no hay driver, no hay nada que hacer.
    if policy == "off" or driver is None:
        return

    # Recupera los resultados de cada fase (los colocó el hook 'pytest_runtest_makereport')
    rep_setup = getattr(request.node, "rep_setup", None)
    rep_call = getattr(request.node, "rep_call", None)
    rep_teardown = getattr(request.node, "rep_teardown", None)

    # Consideramos "failed" si hubo fallo en cualquier fase
    failed = (rep_setup and rep_setup.failed) or (rep_call and rep_call.failed) or (rep_teardown and rep_teardown.failed)
    # "passed" si la fase principal (call) pasó y no hubo fallos
    passed = (rep_call and rep_call.passed) and not failed

    # ¿Adjuntar en fail / pass según la política?
    should_on_fail = policy in ("fail", "always")
    should_on_pass = policy in ("pass", "always")

    # Adjunta según corresponda
    if failed and should_on_fail:
        _attach_artifacts(driver, f"{request.node.name} - FAIL")
    elif passed and should_on_pass:
        _attach_artifacts(driver, f"{request.node.name} - PASS")