from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as elementonuevo
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

from bs4 import BeautifulSoup as bs
import requests

lista_nombres_locales = []

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

link = "https://www.tiendasmass.com.pe/nuestros-locales"
driver.get(link)

WebDriverWait(driver, 451)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.btn-close')))\
    .click()

'''
elementonuevo = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/div/section/div[2]/div[3]')   
verical_ordinate = 100


for i in range(0, 50):
   #print(verical_ordinate)
   driver.execute_script("arguments[0].scrollTop = arguments[1]", elementonuevo, verical_ordinate)
   verical_ordinate += 100
   time.sleep(1)
'''

for i in range(1, 451):

    ################ NOMBRE LOCALES #########################

    WebDriverWait(driver, 451)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/div/div[2]/div/main/div/section/div[2]/div[3]/ul[{i}]/li/div[2]/p/strong")))
    texto_columnas = driver.find_element_by_xpath(f"/html/body/div/div[2]/div/main/div/section/div[2]/div[3]/ul[{i}]/li/div[2]/p/strong")
    texto_columnas = texto_columnas.text
    lista_nombres_locales.append(texto_columnas)
 
print(lista_nombres_locales)
print(len(lista_nombres_locales))

driver.quit()

