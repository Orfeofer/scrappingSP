from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as elementonuevo
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

import re

nombres_prod = []

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

link = "https://www.plazavea.com.pe/carnes-aves-y-pescados"
driver.get(link)

'''
WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[10]/div/div/div[2]/button[2]')))\
    .click()
'''
time.sleep(1)  

#################### NOMBRE PRODUCTOS ############################

WebDriverWait(driver, 300)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.Showcase__name')))\

texto_columnas = driver.find_element_by_css_selector('a.Showcase__name')

texto_columnas = texto_columnas.text
nombres_prod.append(texto_columnas)
print(nombres_prod)
print(len(nombres_prod))




