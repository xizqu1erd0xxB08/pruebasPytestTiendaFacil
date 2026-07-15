from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_eliminar_producto_correcto():
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
            EC.element_to_be_clickable((By.LINK_TEXT, "Ver y administrar productos"))
        ).click()        

        # Botones de eliminar
        botones_eliminar_iniciales = driver.find_elements(By.XPATH, "//button[text()='Eliminar']")

        assert len(botones_eliminar_iniciales) > 0, "No se encontraron botones de eliminar"

        cantidad_botones_iniciales = len(botones_eliminar_iniciales)

        botones_eliminar_iniciales[0].click() # Clic en el primer botón de eliminar

        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.XPATH, "//button[text()='Eliminar']")) == cantidad_botones_iniciales - 1
        )

        mensaje = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "productos"))
        ).text

        assert "mis productos" in mensaje.lower(), "No se redirigió correctamente a la página de productos"

        botones_eliminar_despues = driver.find_elements(By.XPATH, "//button[text()='Eliminar']")

        assert len(botones_eliminar_despues) == cantidad_botones_iniciales - 1, "El producto no se eliminó."

        print("PASS - Producto eliminado correctamente")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_eliminar_producto_correcto()