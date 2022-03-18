from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

link = "https://vea.plazavea.com.pe/principal/nuestras-tiendas"
driver.get(link)

for i in range(1, 66):

    ################ NOMBRE LOCALES #########################

    WebDriverWait(driver, 70)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[{i}]/div[1]/span[1]")))

    texto_columnas = driver.find_element_by_xpath(f"/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[{i}]/div[1]/span[1]")
    texto_columnas = texto_columnas.text
    lista_nombres_locales.append(texto_columnas)
 

print(lista_nombres_locales)
print(len(lista_nombres_locales))

driver.quit()



