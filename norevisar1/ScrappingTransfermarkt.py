from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import openpyxl

lista_de_clubes = []
lista_de_escudos = []
lista_de_competiciones = []
lista_de_valores = []

def quitar_espacios_finales(cadena):
    indice = 0
    for letra in cadena:
        if(letra != " "):
            indice += 1
        else:
            break
    return cadena[:indice]

def quitar_espacios_iniciales(cadena):
    indice = 0
    for letra in cadena:
        if(letra == " "):
            indice += 1
        else:
            break
    return cadena[indice:]

def determinar_valor(cadena):
    s = 0
    mil_millones_euros = " mil mill. €"
    millones_euros = " mill. €"
    indice = 0
    for letra in cadena:
        if letra == " ":
            break
        indice += 1          
    if cadena[indice:] == mil_millones_euros:
        s = 1000000000
    if cadena[indice:] == millones_euros:
        s = 1000000
    return s    

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


for pagina in range(1, 5):
    
    link = f"https://www.transfermarkt.es/spieler-statistik/wertvollstemannschaften/marktwertetop?page={pagina}"
    response = requests.get(link, headers = headers)
    html = response.content
    soup = bs(html, "lxml")
    
    ####################### NOMBRES DE CLUBES ######################

    clubes = soup.find_all("td", class_ = "no-border-links hauptlink")
    clubes_lista = [elemento.get_text() for elemento in clubes]
    lista_de_clubes += clubes_lista

    ####################### COMPETICION ####################

    competiciones = soup.find_all("td", class_ = "links")
    competiciones_lista = [elemento.get_text() for elemento in competiciones]
    
    for i in range(len(competiciones_lista)):
        competiciones_lista[i] = quitar_espacios_iniciales(competiciones_lista[i])
    
    lista_de_competiciones += competiciones_lista

    ####################### VALOR DE MERCADO ###############

    valores = soup.find_all("td", class_ = "rechts", style = False)
    valores_lista = [elemento.get_text() for elemento in valores]

    for i in range(len(valores_lista)):
        valores_lista[i] = valores_lista[i].replace(",",".")
        #valor = determinar_valor(valores_lista[i])
        valores_lista[i] = quitar_espacios_finales(valores_lista[i])
        #valores_lista[i] = valores_lista[i] * valor
        
    valores_lista = [float(x) for x in valores_lista]
    lista_de_valores += valores_lista
    
    print(f"página {pagina} cargada")

clubes_series = pd.Series(lista_de_clubes)
competiciones_series = pd.Series(lista_de_competiciones)
valores_series = pd.Series(lista_de_valores)

data = pd.DataFrame({"clubes": clubes_series,
                     "competiciones": competiciones_series,
                     "valores": valores_series})

data.to_excel("dataClubes.xlsx")