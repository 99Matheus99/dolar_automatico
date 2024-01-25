from selenium import webdriver

# PARTE QUE ABRE O NAVEGADOR
driver = webdriver.Chrome()
driver.get('https://economia.uol.com.br/cotacoes/cambio/')
driver.implicitly_wait(0.5)



driver.quit()