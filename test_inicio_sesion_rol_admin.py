from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_con_seleccion_rol_administrador():
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

        inputRadioAdministrador = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "rol1"))
        )

        inputRadioAdministrador.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Panel de administrador")
        )                

        assert driver.title == "Panel de administrador", (
            f"Se esperaba el título 'Panel de administrador', "
            f"Pero el navegador mostró: '{driver.title}'"
        )

        print("PASS - Login con selección de rol Administrador exitoso")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_con_seleccion_rol_administrador()