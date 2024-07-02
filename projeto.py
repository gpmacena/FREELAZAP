# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade Nativa do whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pyperclip

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")
time.sleep(30)

mensagem = """ Fala galera!
Se inscreve no canal do maceninha, ele é fera!
"""

#enviar a mensagem para meu numero, para depois encaminhar

#clicar na lupa
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('11977965017')
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

#escrever a mensagem para mim
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(500)
