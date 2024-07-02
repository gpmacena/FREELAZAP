from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")

from selenium.webdriver.common.keys import Keys
import pyperclip
import time
time.sleep(30)
mensagem = """Fala galera!
Se inscreve no canal da Hahstag Programação, os caras são feras!
"""

lista_contatos = ['Anota']

nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('11977965017')
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

from selenium.webdriver.common.action_chains import ActionChains

qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1
    
for i in range(qtde_blocos):
    
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    lista_elementos = nav.find_elements('class name', '_amk4') 
    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item

    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name','_ahkm').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(1)
    
    for nome in lista_enviar:
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(0.7)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(0.7)
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(0.7)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(5)
