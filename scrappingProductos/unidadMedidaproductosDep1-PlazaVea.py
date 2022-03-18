from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re
from selenium import webdriver
import time

lista_unidad = []


######### DEPARTAMENTO = CARNES AVES Y PESCADOS #################
departamentos = ['carnes-aves-y-pescados']
categorias = ['pollo', 'res', 'cerdo', 'pescados-y-mariscos', 'pavo-pavita-y-otras-aves', 
                'enrollados', 'hamburguesas-nuggets-y-apanados']

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


driver_path = 'C:\\Users\\Fernandez\\Downloads\\chromedriver_win32\\chromedriver.exe'
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

for elemento in categorias:
    
    link = f"https://www.plazavea.com.pe/carnes-aves-y-pescados/{elemento}"
    driver.get(link)
    time.sleep(10)

    soup = bs(driver.page_source, "lxml")
    unidad = soup.find_all("div", class_ = "Showcase__units-reference")
    unidad_lista = [elemento.get_text() for elemento in unidad]
    lista_unidad += unidad_lista

    print(f"categoria {elemento} cargado")
    #driver.quit()

    

print(lista_unidad)
print(len(lista_unidad))

