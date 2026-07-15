from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registro_usuario_tendero():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost/PHP_CON_CLAUDE/upgradedStoreProjectMejoradoFrontend/views/loginView.php")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userName"))
        ).send_keys("tendero1")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userEmail"))
        ).send_keys("tendero1@email.com")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userPassword"))
        ).send_keys("contraseñaSegura123")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirmPassword"))
        ).send_keys("contraseñaSegura123")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
        ).click()         

        titulo_login = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "exito"))
        ).text

        assert "iniciar sesión" in titulo_login.lower()        

        print("Test Exitoso. El usuario fue registrado y redirigido al Login correctamente.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_registro_usuario_tendero()