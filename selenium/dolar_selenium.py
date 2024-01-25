from selenium import webdriver
from selenium.webdriver.common.by import By

# PARTE QUE ABRE O NAVEGADOR
driver = webdriver.Chrome()
driver.get('https://economia.uol.com.br/cotacoes/cambio/')
driver.implicitly_wait(0.5)

# PARTE QUE PEGA OS VALORES
elemento = driver.find_element(by=By.NAME, value='currency2')
valor = elemento.get_attribute('value') # aqui pega o valor da variável que está dentro do parâmetro "value"
print(f'O valor atual do dólar é {valor}')

driver.quit()