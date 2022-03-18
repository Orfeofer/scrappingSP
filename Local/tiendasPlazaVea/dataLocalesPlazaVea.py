import pandas as pd
from nombresLocalesPlazaVea import lista_nombres_locales
from direccionesPlazaVea import lista_direcciones

nombres_locales_series = pd.Series(lista_nombres_locales)
direcciones_series = pd.Series(lista_direcciones)

data = pd.DataFrame({"nombres_locales": nombres_locales_series,
                     "direcciones_locales": direcciones_series})

data.to_excel("dataLocalesPlazaVea.xlsx", index = False)

