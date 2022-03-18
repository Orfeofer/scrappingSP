import pandas as pd
from productosDep1PlazaVea import data1
from productosDep2PlazaVea import data2
from productosDep3PlazaVea import data3








data = pd.concat([data1, data2, data3], axis = 0)

data.to_excel("DataProductos.xlsx", index = False)
