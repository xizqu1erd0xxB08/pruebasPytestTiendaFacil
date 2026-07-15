from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_editar_producto_correcto():
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

        botones_editar_iniciales = driver.find_elements(By.XPATH, "//button[text()='Editar']") # Botones de editar

        assert len(botones_editar_iniciales) > 0, "No se encontraron botones de editar"

        botones_editar_iniciales[0].click() # Clic en el primer botón de editar

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "productName"))
        ).clear()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "productName"))
        ).send_keys("Galletas de Coco Festival x6")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "productPrice"))
        ).clear()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "productPrice"))
        ).send_keys("2000")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "currentStock"))
        ).clear()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "currentStock"))
        ).send_keys("50")  
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        ).click() 

        mensaje = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "productos"))
        ).text

        assert "mis productos" in mensaje.lower(), "No se redirigió correctamente a la página de productos"

        print("PASS - Producto editado correctamente")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_editar_producto_correcto()