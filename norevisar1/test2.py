##################################
##################################
######## NO CONSIDERAR ############
####################################
####################################

from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re
from selenium import webdriver
import time


lista_cod = []
lista = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


'''link = "https://www.plazavea.com.pe/carnes-aves-y-pescados"
response = requests.get(link, headers = headers)
html = response.content
'''
driver_path = 'C:\\Users\\Fernandez\\Downloads\\chromedriver_win32\\chromedriver.exe'


driver = webdriver.Chrome(driver_path)
driver.get("https://www.plazavea.com.pe/carnes-aves-y-pescados")
time.sleep(50)

soup = bs(driver.page_source, "lxml")

unidad = soup.find_all("div", class_ = "Showcase__units-reference")
unidad_lista = [elemento.get_text() for elemento in unidad]
lista_cod += unidad_lista

'''
lsx = re.split('  ', lista_cod[0])
for elemento in lsx:
    lista.append(elemento)
'''

driver.quit()
#lista.pop(0)
#lista.pop(0)
print(lista_cod)
print(len(lista_cod))



#print(lista_cod)

#print(len(unidad))