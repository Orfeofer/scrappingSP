from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_unidad = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

link = "https://www.plazavea.com.pe/carne-molida-de-pavita-x500g/p"
response = requests.get(link, headers = headers)
html = response.content
soup = bs(html, "lxml")

unidad = soup.find("div", class_ = "ProductCard__prices__title")
unidad_lista = [elemento.get_text() for elemento in unidad]
lista_unidad += unidad_lista
print(lista_unidad)
print(len(lista_unidad))

cadena = ''

for elemento in lista_unidad:
    cadena = f"{cadena}{elemento}"

print(cadena)

#Precio x kg
    
