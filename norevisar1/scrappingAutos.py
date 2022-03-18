import requests
from bs4 import BeautifulSoup as bs

def obtenerDatosAutos():
    def getText(lista):
        return [elemento.get_text() for elemento in lista]

    def scrapear(tag, clase):
        lista = soup.find_all(tag, class_=clase)
        lista = getText(lista)
        return lista

    def quitarTresCaracteres(lista):
        for i in range(len(lista)):
            lista[i] = lista[i][:-3]
        return lista
        
    link = "https://www.autocosmos.com.pe/auto/usado"
    response = requests.get(link)

    html = response.content

    soup = bs(html, "lxml")

    marcas = scrapear("span", "listing-card__brand")
    modelos = scrapear("span", "listing-card__model")

    nombres = [marcas[i] + " " + modelos[i] for i in range(len(marcas))]

    detalles = scrapear("span", "listing-card__version")

    anios = scrapear("span", "listing-card__year")

    dolares = scrapear("span", "listing-card__price-value")

    lugares = scrapear("span", "listing-card__city")
    lugares = quitarTresCaracteres(lugares)

    return {
        "nombre": nombres,
        "detalles": detalles,
        "anios": anios,
        "preciosDolares": dolares,
        "ubicacion": lugares
    }