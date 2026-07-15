from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_crear_producto_correcto():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost/PHP_CON_CLAUDE/upgradedStoreProjectMejoradoFrontend/views/loginView.php")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userIdentifier"))
        ).send_keys("usuarioSeguroyAdmin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userPassword"))
        ).send_keys("123contraseñaSegura")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        ).click()

        inputRadioTendero = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "rol2"))
        )

        inputRadioTendero.click()             

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Dashboard")
        )                

        assert driver.title == "Dashboard", (
            f"Se esperaba el título 'Dashboard', "
            f"Pero el navegador mostró: '{driver.title}'"
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Crear producto"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productName"))
        ).send_keys("Galletas de Chocolate Festival x6")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productPrice"))
        ).send_keys("2000")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "currentStock"))
        ).send_keys("50")             

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        ).click()           
        
        mensaje = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bienvenida"))
        ).text

        assert "bienvenido" in mensaje.lower()

        print("PASS - Producto creado correctamente")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_crear_producto_correcto()