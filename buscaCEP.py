from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
time.sleep(4)

navegador.find_element_by_id("endereco").send_keys("31340000")
time.sleep(3)
navegador.find_element_by_name("btn_pesquisar").click()