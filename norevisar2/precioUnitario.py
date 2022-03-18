from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_precios = []
lista_final = []

'''
def quitar_moneda(cadena):
    indice = 0
    for letra in cadena:
        if(letra == )
'''
######################

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

        #####################  PRECIOS #################

        precios = soup.find_all("div", class_ = "Showcase__salePrice")
        precios_lista = [elemento.get_text() for elemento in precios]

        lista_precios += precios_lista

        print(f"categoria {elemento} cargada")
    print(f"departamento {clave} cargado")


for i in range(0, len(lista_precios)-1):
    if (i-1) % 3 == 0:
        lista_final.append(lista_precios[i])

for i in range(len(lista_final)):
    lista_final[i] = lista_final[i].replace("S/ ","")


lista_final = [float(x) for x in lista_final]

print(lista_final)
print(len(lista_final))



