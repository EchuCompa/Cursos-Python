# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:16:49 2020

@author: Diego
"""
value = 42863.1
# print(value)
# print(f'{value:0.4f}')
# print(f'{value:>16.2f}')
# print(f'{value:<16.2f}')
# print(f'{value:*>16,.2f}')

import csv

def costo_camion(nombre_archivo):
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = dict(zip(headers, row))
            ncajones = int(lote["cajones"])
            precio = float(lote["precio"])
            total += ncajones * precio
    return total

def leer_camion(nombre_archivo):
    camion= []
    with open(nombre_archivo, 'rt') as fi:
        rows = csv.reader(fi)
        headers = next(rows)
        for row in rows:
            lote = dict(zip(headers, row))
            camion.append(lote)
    return camion

precios_camio = leer_camion("Data/fecha_camion.csv")

def leer_precios(nombre_archivo):
    precios= {}
    with open(nombre_archivo, 'rt') as fi:
        rows = csv.reader(fi)
        for row in rows:
            if len(row)>1:
                precios[row[0]]=row[1]  
    return precios

lista_precios = leer_precios("Data/precios.csv")
record = []

for j in precios_camio:
   precio_fruta = float(lista_precios[j["nombre"]])
   cajones = int(j["cajones"])

