# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:16:49 2020

@author: Diego
"""
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


def leer_precios(nombre_archivo):
    precios= {}
    with open(nombre_archivo, 'rt') as fi:
        rows = csv.reader(fi)
        for row in rows:
            #a mi no se me había ocurrido como hacerlo con if, muy lindo
            if len(row)>1:
                precios[row[0]]=row[1]  
    return precios

###################################################################################
#Ejercicio 2.30 + 2.31

def hacer_informe(lista_precios, precios_camio):
    record = []
    for j in precios_camio:
       nombre = j["nombre"]
       cajones = int(j["cajones"])
       #para el $ yo lo metí acá, no es lo más elegante pero funcionar, funciona.
       #sería hacer:
       #precio = '$'+str(float(j['precio']))
       #y después en print() cambiás {precio:>10s}
       precio = float(j["precio"])
       cambio = round(float(lista_precios[j["nombre"]])-float(j["precio"]),2)
       data_fruta = (nombre, cajones, precio, cambio)
       record.append(data_fruta)
    return record

lista_precio = leer_precios("Data/precios.csv")
precios_camion = leer_camion("Data/fecha_camion.csv")
informe = hacer_informe(lista_precio, precios_camion)

# for nombre, cajones, precio, cambio in informe:
#         print(f'| {nombre:>10s} | {cajones:>10d} | {precio:>10.2f} | {cambio:>10.2f} | ')


#Ejercicio 2.32 + 2.33
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
nombre, cajones, precio, cambio = headers
print(f'{nombre:<10s} {cajones:<10s} {precio:<10s} {cambio:<10s}')
print("---------- ---------- ---------- ----------")
for nombre, cajones, precio, cambio in informe:
        # una opción pero medio truchelli precio = "$" + str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:$>10.2f} {cambio:>10.2f} ')
        #print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f} ')
        #NO SE CÓMO CONFIGURAR EL MALDITO "$"

#está todo muy prolijo legible y bien, apruebo 5/5 paulapuntos














