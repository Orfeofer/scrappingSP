from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as elementonuevo
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from nombreDepartamentos import href_departamentos, lista_nombres_departamentos, dict_dep_href

lista_nom_categorias = []

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

lista = href_departamentos

lista.remove('https://www.vivanda.com.pe/packs')
lista.remove('https://www.vivanda.com.pe/pollo-rostizado-y-comidas-preparadas')
lista.remove('https://www.vivanda.com.pe/mascotas')
#print(lista)


for i in range(1, 13):

    lnk = lista[i-1]
    driver.get(lnk)
    '''
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[10]/div/div/div[2]/button[2]')))\
        .click()
    '''

    '''
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "div.vivanda-menu-dropdown-0-x-menu_dropdown_container_category_children")))
    '''
    WebDriverWait(driver, 30)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            f"/html/body/div[2]/div/div[1]/div/div[7]/div/div/section/div[2]/div/div[3]/section/div/div[1]/div/div[3]/div/div/div[2]/div/div[{i}]/div/div[2]")))
    
    
    texto_columnas = driver.find_element_by_css_selector("div.vivanda-menu-dropdown-0-x-menu_dropdown_container_category_children")
    texto_columnas = texto_columnas.text

    lista_nom_categorias.append(texto_columnas)

    driver.quit()

print(lista_nom_categorias)
print(len(lista_nom_categorias))



                                            




    








