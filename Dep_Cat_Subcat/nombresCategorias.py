from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as elementonuevo
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from nombreDepartamentos import lista_nombres_departamentos
import re

lista_nombre_cat = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
#options.add_argument('--disable-extensions')
driver_path = 'C:\\Users\\Fernandez\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

link = "https://www.vivanda.com.pe/packs"
driver.get(link)

WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[10]/div/div/div[2]/button[2]')))\
    .click()

time.sleep(1)    

for i in range(1, 13):

    #################### NOMBRE CATEGORIAS ########################
    
    WebDriverWait(driver, 30)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/div[2]/div/div[1]/div/div[7]/div/div/section/div[2]/div/div[3]/section/div/div[1]/div/div[3]/div/div/div[2]/div/div[{i}]/div/div[2]")))
                                            
    texto_columnas = driver.find_element_by_xpath(f"/html/body/div[2]/div/div[1]/div/div[7]/div/div/section/div[2]/div/div[3]/section/div/div[1]/div/div[3]/div/div/div[2]/div/div[{i}]/div/div[2]")
    texto_columnas = texto_columnas.text
    lista_nombre_cat.append(texto_columnas)

    time.sleep(1)

lista = lista_nombre_cat
lsx = []

for i in range(len(lista)):
    lista[i] = re.split('\n', lista[i])
    for elemento in lista[i]:
        lsx.append(elemento)

print(lsx)
print(len(lsx))
#print(lista)
#print(len(lista))
#print(lista_nombre_cat)
#print(len(lista_nombre_cat))

driver.quit()
