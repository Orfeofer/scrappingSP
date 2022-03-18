from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

lista_nombres = []
lista_marcas = []

lista_precios = []
lista_final_prec = []

lista_href = []


lista_unidad = []
lista_fin_unidad = []


lista_codigo = []
lista_cod_final = []

ls_completa = []

lista_departamento = []
lista_categoria = []
lista_sub_categ = []


lista_cod_depa = []
lista_cod_cat = []


######### DEPARTAMENTO = FRUTAS Y VERDURAS #################

departamentos = ['frutas-y-verduras']
categorias = ['frutas', 'verduras']

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


for elemento in categorias:

    link = f"https://www.plazavea.com.pe/frutas-y-verduras/{elemento}"
    response = requests.get(link, headers = headers)
    html = response.content
    soup = bs(html, "lxml")

    #############################  NOMBRES_PRODUCTOS   ############################

    nombres = soup.find_all("a", class_ = "Showcase__name")
    nombres_lista = [elemento.get_text() for elemento in nombres]
    lista_nombres += nombres_lista

    #############################   MARCAS    ###################################

    marcas = soup.find_all("div", class_ = "Showcase__brand")
    marcas_lista = [elemento.get_text() for elemento in marcas]
    lista_marcas += marcas_lista
    
    
    ############################# PRECIOS #######################################

    precios = soup.find_all("div", class_ = "Showcase__salePrice")
    precios_lista = [elemento.get_text() for elemento in precios]
    lista_precios += precios_lista


    ############################ LINK PRODUCTO ##################################

    for e in soup.find_all(class_ = "Showcase__name", href = True):
        lista_href.append(e['href'])
    
    print(f"categoría {elemento} cargada")


i = 1
j = 0

for element in lista_href:
    link2 = element
    response = requests.get(link2, headers = headers)
    html = response.content
    soup = bs(html, "lxml")

    ########################### CODIGO PRODUCTO ##################################

    lista_codigo = []

    codigo = soup.find("span", class_ = "ProductCard__sku")
    codigo_lista = [elemento.get_text() for elemento in codigo]
    lista_codigo += codigo_lista

    lista_cod_final.append(lista_codigo[1])

    
    ########################### UNIDAD MEDIDA #####################################

    unidad = soup.find("div", class_ = "ProductCard__prices__title")
    unidad_lista = [elemento.get_text() for elemento in unidad]
    lista_unidad = []
    lista_unidad += unidad_lista

    cadena = ''
    for elem in lista_unidad:
        cadena = f"{cadena}{elem}"
        
    lista_fin_unidad.append(cadena)


    ############################ DEPARTAMENTO, CATEGORIA Y SUBCATEGORIA #####################

    ls_completa = []

    nlst = soup.find_all("span", itemprop = "name")
    area_nlst = [elemento.get_text() for elemento in nlst]
    ls_completa += area_nlst


    ########################### DEPARTAMENTO #####################################

    lista_departamento.append(ls_completa[1])
    lista_cod_depa.append(lista_departamento[j][:5])

    ########################### CATEGORIA #####################################

    lista_categoria.append(ls_completa[2])
    lista_cod_cat.append(lista_categoria[j][:4])

    ########################### SUBCATEGORIA #####################################

    lista_sub_categ.append(ls_completa[3])


    print(f"link {i}: {element} cargado")

    i += 1
    j += 1

for i in range(0, len(lista_precios)-1):
    if (i-1) % 3 == 0:
        lista_final_prec.append(lista_precios[i])

for i in range(len(lista_final_prec)):
    lista_final_prec[i] = lista_final_prec[i].replace("S/ ","")

lista_final_prec = [float(x) for x in lista_final_prec]


'''print(lista_nombres)
print(len(lista_nombres))

print(lista_marcas)
print(len(lista_marcas))

print(lista_final_prec)
print(len(lista_final_prec))

print(lista_href)
print(len(lista_href))

print(lista_fin_unidad)
print(len(lista_fin_unidad))

print(lista_cod_final)
print(len(lista_cod_final))

print(lista_departamento)
print(len(lista_departamento))

print(lista_categoria)
print(len(lista_categoria))

print(lista_sub_categ)
print(len(lista_sub_categ))'''

#print(lista_cod_depa)
#print(len(lista_cod_depa))

#print(lista_cod_cat)
#print(len(lista_cod_cat))





################################ DATAFRAME #####################################

nombres_series = pd.Series(lista_nombres)
marcas_series = pd.Series(lista_marcas)
precio_series = pd.Series(lista_final_prec)
unidad_series = pd.Series(lista_fin_unidad)
codigo_series = pd.Series(lista_cod_final)
departamento_series = pd.Series(lista_departamento)
categoria_series = pd.Series(lista_categoria)
subcategoria_series = pd.Series(lista_sub_categ)

data2 = pd.DataFrame({"cod_producto": codigo_series,
                     "nombre_producto": nombres_series,
                     "unidad_medida": unidad_series,
                     "precio_unitario_producto": precio_series,
                     "marca_prod": marcas_series,
                     "id_sub_categoria": subcategoria_series,
                     "id_categoria": categoria_series,
                     "id_departamento": departamento_series})

data2.to_excel("DataProductos2.xlsx", index = False)



