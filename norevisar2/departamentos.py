from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_departamentos = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

link = "https://www.plazavea.com.pe/packs"
response = requests.get(link, headers = headers)
html = response.content
soup = bs(html, "lxml")

departamentos = soup.find_all("li")
departamentos_lista = [elemento.get_text() for elemento in departamentos]
lista_departamentos += departamentos_lista

print(lista_departamentos)
