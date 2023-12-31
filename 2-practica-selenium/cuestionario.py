
from dotenv import load_dotenv
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

load_dotenv()
USERNAME = os.getenv("USERNAME2")
PASSWORD = os.getenv("PASSWORD2")

try:
  #! Navegador Chrome
  driver = webdriver.Chrome()

  #! Página web
  driver.get("https://virtual.um.edu.ar/login/index.php")
  driver.implicitly_wait(10)
  print("Página de login abierta con éxito")

  #! Campo de nombre de usuario
  driver.find_element(By.ID, "username").click()
  driver.find_element(By.ID, "username").send_keys(USERNAME)

  #! Campo de contraseña
  driver.find_element(By.ID, "password").click()
  driver.find_element(By.ID, "password").send_keys(PASSWORD)
  print("Campos de login encontrados con éxito")


  #! Boton de login
  driver.find_element(By.ID, "loginbtn").click()
  print("Boton de login encontrado con éxito")
  driver.implicitly_wait(10)

  #! Página web
  driver.get("https://virtual.um.edu.ar/mod/questionnaire/complete.php?id=210589")
  driver.implicitly_wait(10)
  print("Página de cuestionario abierta con éxito")


  #! Pregunta 1: Si
  driver.find_element(By.ID, 'auto-rb0001').click()
  print("Pregunta 1 respondida con éxito")
  time.sleep(5)

  #! Pregunta 2: menú desplegable
  select = Select(driver.find_element(By.ID, 'dropSelecciòn'))
  select.select_by_value('4053')
  print("Pregunta 2 respondida con éxito")

  #! Enviar el cuestionario
  driver.find_element(By.CSS_SELECTOR, '.buttons > .btn').click()
  print("Cuestionario enviado con éxito")

  #! Verificar URL de la página de confirmación
  assert 'https://virtual.um.edu.ar/mod/questionnaire/complete.php' in driver.current_url
  print("URL de confirmación encontrada con éxito")

  #! Busca el elemento 'h3'
  element = driver.find_element(By.XPATH, "//h3[contains(text(), 'Gracias por realizar esta encuesta')]")
  assert element is not None, "No se encontró un elemento 'h3'"
  print("Elemento 'Gracias por realizar esta encuesta' encontrado con éxito")

  #! Continuar
  driver.find_element(By.CSS_SELECTOR, '.mod_questionnaire_completepage button.btn.btn-secondary').click()
  print("Boton de continuar encontrado con éxito")
  time.sleep(10)


except Exception as e:
  print("++++ Error en los tests ++++")
  print(e)
  
finally:
  #! Cerrar Chrome
  driver.quit()
  print("Cerrando navegador...")