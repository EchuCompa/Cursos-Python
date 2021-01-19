# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:25:17 2020

@author: Diego
"""
import csv
#from pprint import pprint

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
            # Modo TUPLA
            # lote = (row[0], int(row[1]), float(row[2]))
            # Modo Diccionario
            # lote = { headers[0] :row[0] , headers[1]: int(row[1]), headers[2]: float(row[2]) }
            # Modo Diccionario + Zip
            lote = dict(zip(headers, row))
            lote["cajones"] = int(lote["cajones"])
            lote["precio"] = float(lote["precio"])
            camion.append(lote)
    return camion

precios_camio = leer_camion("Data/fecha_camion.csv")
# pprint(camio)

def leer_precios(nombre_archivo):
    precios= {}
    with open(nombre_archivo, 'rt') as fi:
        rows = csv.reader(fi)
        for row in rows:
            # Esto es para que no se trabe si hay alguna lista con datos faltantes
            if len(row)>1:
                precios[row[0]]= float(row[1])
    return precios

# lista_precios = leer_precios("Data/precios.csv")

# venta = 0
# costo_camio = costo_camion("Data/fecha_camion.csv")
# #Aclaro que entendí que los precios del camión son lo que pago por los productos
# #y los precios 
# for j in precios_camio:
#     # No hay mucha magia, agarro los precios a los que vende la fruta y los 
#     # multiplico por la cantidad de cajones (asumo que es alte crack y vende todo)
#    precio_fruta = float(lista_precios[j["nombre"]])
#    cajones = int(j["cajones"])
#    venta  += cajones*precio_fruta

# print("La diferencia es de $", round(venta-costo_camio,2))
#Osea que genero ganancia, sino alto bajón.
   
#conciso, legible y muy bonito, nada que agregar está todo diez puntos 