from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as elementonuevo
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

lista_nombres_departamentos = []
href_departamentos = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = 'C:\\Users\\Fernandez\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

link = "https://www.vivanda.com.pe/"
driver.get(link)
'''
WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[10]/div/div/div[2]/button[2]')))\
    .click()
'''
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div/div[1]/div/div[5]/div/div[1]/div/div/div')))\
    .click()

for i in range(1, 16):

    #################### NOMBRE DEPARTAMENTOS ########################

    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/div[8]/div/div[2]/div/div[1]/div/div[2]/ul/li[{i}]/a")))

    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/div[8]/div/div[2]/div/div[1]/div/div[2]/ul/li[{i}]/a")))

    lnk = driver.find_element_by_xpath(f"/html/body/div[8]/div/div[2]/div/div[1]/div/div[2]/ul/li[{i}]/a")

    texto_columnas = driver.find_element_by_xpath(f"/html/body/div[8]/div/div[2]/div/div[1]/div/div[2]/ul/li[{i}]/a")
    texto_columnas = texto_columnas.text

    link_categoria = lnk.get_attribute("href") 

    lista_nombres_departamentos.append(texto_columnas)

    href_departamentos.append(link_categoria)

dict_dep_href = dict(zip(lista_nombres_departamentos, href_departamentos))

#print(lista_nombres_departamentos)
#print(len(lista_nombres_departamentos))

print(href_departamentos)
print(len(href_departamentos))

print(dict_dep_href)
print(len(dict_dep_href))

driver.quit()
 


