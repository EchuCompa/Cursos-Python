# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:16:49 2020

@author: Diego
"""
import csv
from fileparse import parse_csv
import sys


def costo_camion(nombre_archivo):
    total = 0.0
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = dict(zip(headers, row))
            ncajones = int(lote["cajones"])
            precio = float(lote["precio"])
            total += ncajones * precio
    return total

# -------------------------------------------------------------------------
# Ejercicio 6.5

def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as file:
        return parse_csv(file) 

# Para ambos, tuve que poner el return dentro del with para que no me cierre el archivo

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as file:
        return parse_csv(file, has_headers=False)


def hacer_informe(lista_precios, precios_camio):
    record = []
    lista_precios = dict(lista_precios)
    for j in precios_camio:
       nombre = j["nombre"]
       cajones = int(j["cajones"])
       precio = float(j["precio"])
       cambio = round(float(lista_precios[j["nombre"]])-float(j["precio"]),2)
       data_fruta = (nombre, cajones, precio, cambio)
       record.append(data_fruta)
    return record

# Ejercicio 5.1

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    nombre, cajones, precio, cambio = headers
    print(f'{nombre:<10s} {cajones:<10s} {precio:<10s} {cambio:<10s}')
    print("---------- ---------- ---------- ----------")
    for nombre, cajones, precio, cambio in informe:
            # precio = "$" + str(precio)
            print(f'{nombre:>10s} {cajones:>10d} ${precio:>10.2f} {cambio:>10.2f} ')
    return 0 #Es una práctica que se hace en C++ parece, así que la adopto para ser cool
     
# Ejercicio 5.2   


def informe_camion(data_precios, data_camion):
    lista_precio = leer_precios(data_precios)
    precios_camion = leer_camion(data_camion)
    informe = hacer_informe(lista_precio, precios_camion)
    imprimir_informe(informe)
    return 0 

informe_camion("Data/precios.csv", "Data/camion.csv")

# def main(argv):
#     if len(argv) != 3:
#         raise SystemExit(f'Uso adecuado: {argv[0]} ' 'archivo_camion archivo_precios')
#     camion = argv[1]
#     precios = argv[2]
#     return informe_camion(precios, camion)
    
    
# if __name__ == '__main__':
#     main(sys.argv) 


# files = ['Data/camion.csv', 'Data/camion2.csv'] #Chequeanding
# for name in files:
#         print(f'{name:-^43s}')
#         informe_camion('Data/precios.csv', name)
#         print()





