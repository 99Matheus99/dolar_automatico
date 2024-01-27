# obs.: note que para usar o e-mail do destinatário é necessário, se for G-mail
# ativar a senha de app nas configurações
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from email.message import EmailMessage # biblioteca para configurar a mensagem do email
import ssl # mantém uma conexão interna segura no envio1
import smtplib # biblioteca para enviar emails
import os # biblioteca para acessar as variáveis de ambiente 

def mensagem_email(dolar): # passo a passo básico para enviar e-mails pelo python
    try:
        remetente = os.environ.get('usuario_email_matheus') # guardado em variáveis de ambiente para segurança
        senha = os.environ.get('senha_email_matheus')  # guardado em variáveis de ambiente para segurança
        destinatario = 'thomazrb@gmail.com'

        sujeito = 'valor atual do dolar pelo selenium'
        corpo = f'O valor do dolar nesse momento e R${dolar}'
        
        em = EmailMessage() # objeto que contém a mensagem escrita abaixo
        em['from'] = remetente
        em['to'] = destinatario
        em['subject'] = sujeito
        em.set_content(corpo)

        contexto = ssl.create_default_context() # contexto de segurança

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(remetente, senha)
            smtp.sendmail(remetente, destinatario, em.as_string())
        
        print('Email enviado com sucesso!')
    except Exception as erro: # mostra o erro, caso ele aconteça
        print(f'Erro ao enviar e-mail: {erro}')

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

# PARTE QUE ENVIA O EMAIL
mensagem_email(valor)

driver.quit()