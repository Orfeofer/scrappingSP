from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_marcas = []

######### DEPARTAMENTO = CARNES AVES Y PESCADOS #################

categorias1 = ['pollo', 'res', 'cerdo', 'pescados-y-mariscos', 'pavo-pavita-y-otras-aves', 
                'enrollados', 'hamburguesas-nuggets-y-apanados']

categorias2 = ['frutas', 'verduras']

diccionario = {'carnes-aves-y-pescados': categorias1, 
                'frutas-y-verduras': categorias2, 
                }

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

for clave in diccionario:
    valor = diccionario[clave]
    for elemento in valor:
        link = f"https://www.plazavea.com.pe/{clave}/{elemento}"
        response = requests.get(link, headers = headers)
        html = response.content
        soup = bs(html, "lxml")

        marcas = soup.find_all("div", class_ = "Showcase__brand")
        marcas_lista = [elemento.get_text() for elemento in marcas]
        lista_marcas += marcas_lista

        print(f"categoria {elemento} cargada")
    print(f"departamento {clave} cargado")

print(lista_marcas)
print(len(lista_marcas))