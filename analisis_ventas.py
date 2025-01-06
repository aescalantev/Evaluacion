# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:57:17 2025

@author: aesca
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('ventas_productos.csv')
df['Precio_Total']=df['Cantidad']*df['Precio']

print(df.head())

plt.bar(df['Producto'],df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio_Total')
plt.title('Precio Total por Producto')
plt.savefig('grafico_precios.png')
plt.show()

          