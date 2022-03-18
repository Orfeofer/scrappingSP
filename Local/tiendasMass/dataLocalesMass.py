import pandas as pd
from nombresLocalesMass import lista_nombres_locales
from direccionesMass import lista_direcciones

nombres_locales_series = pd.Series(lista_nombres_locales)
direcciones_series = pd.Series(lista_direcciones)

data = pd.DataFrame({"nombres_locales": nombres_locales_series,
                     "direcciones_locales": direcciones_series})

data.to_excel("dataLocalesMass.xlsx", index = False)