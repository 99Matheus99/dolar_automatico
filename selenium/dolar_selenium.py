from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# OPÇÕES
chrome_options = Options() # passo essa classe para uma variável
chrome_options.add_argument("--headless") # esse argumento faz o navegador rodar em segundo plano
chrome_options.add_argument("log-level=3") # esse argumento tira grande parte dos erros que aparecem no log, deixando apenas os mais graves

# PARTE QUE ABRE O NAVEGADOR
driver = webdriver.Chrome(options=chrome_options) # carrego o webdriver com essa opção
driver.get('https://economia.uol.com.br/cotacoes/cambio/')
driver.implicitly_wait(0.5)

# PARTE QUE PEGA OS VALORES
elemento = driver.find_element(by=By.NAME, value='currency2')
valor = elemento.get_attribute('value') # aqui pega o valor da variável que está dentro do parâmetro "value"
print(f'O valor atual do dólar é R${valor}')

driver.quit()