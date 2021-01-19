# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:32:50 2020

@author: Diego
"""
from info import leer_camion, leer_precios
#Ejercicio 3.10
# nums = [1,2,3,4]
# cuadrados = [ x * x for x in nums ]
# dobles = [ 2 * x for x in nums if x > 2 ]

#Ejercicio 3.11
camion = leer_camion('Data/camion.csv')
costo = sum([ s['cajones'] * s['precio'] for s in camion ]) 
precios = leer_precios('Data/precios.csv')
# valor = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])

# #Ejercicio 3.12

# mas100 = [ s for s in camion if s['cajones'] > 100 ]
# myn = [ s for s in camion if s['nombre'] in {'Mandarina','Naranja'} ]
# costo10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]

# #Ejercicio 3.13

# nombre_cajones =[ (s['nombre'], s['cajones']) for s in camion ]
# nombres = { s['nombre'] for s in camion }
# stock = { nombre: 0 for nombre in nombres }
# for s in camion:
#         stock[s['nombre']] += s['cajones']

#Ejercicio 3.14

import csv
# f = open('Data/fecha_camion.csv')
# rows = csv.reader(f)
# headers = next(rows)
# select = ['nombre', 'cajones', 'precio']
# indices = [ headers.index(ncolumna) for ncolumna in select ]
# camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]


#Ejercicio 3.15
f = open('Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
types = [str, int, float]
row = next(rows)

r = list(zip(types, row))

converted = [func(val) for func, val in r]

#Ejercicio 3.16
s= { name: func(val) for name, func, val in zip(headers, types, row) }
