import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
  #! Navegador Chrome
  driver = webdriver.Chrome()

  #! Página web
  driver.get("https://biblioteca.um.edu.ar/")

  #! Esperar qu ecargue la pag web, si pasan mas de 10 segundo salta una Exception.
  driver.implicitly_wait(10)
  print("Página abierta con éxito")

  #! Campo de busqueda
  driver.find_element(By.ID, "translControl1").click()
  driver.find_element(By.ID, "translControl1").send_keys("pressman")
  driver.find_element(By.ID, "searchsubmit").click()

  driver.implicitly_wait(10)
  print("Campo de busqueda encontrado con éxito")

  #! Buscar primer titulo
  title_element_1 = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "#title_summary_60480 > .title"))
  )
  assert "INGENIERIA DEL SOFTWARE: UN ENFOQUE PRACTICO" in title_element_1.text
  print("Primer título verificado con éxito")

  #! Buscar segundo titulo
  title_element_2 = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "#title_summary_60481 > .title"))
  )
  assert "INGENIERIA DEL SOFTWARE" in title_element_2.text
  print("Segundo título verificado con éxito")

  #! Verificar que haya 2 elementos en la tabla
  table_rows = WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#bookbag_form > table > tbody > tr"))
  )
  assert len(table_rows) == 2
  print("Hay 2 elementos en la tabla")
  
except Exception as e:
  print("Error en los tests")
  print(e)
  
finally:
  #! Cerrar Chrome
  driver.quit()
  print("Cerrando navegador...")