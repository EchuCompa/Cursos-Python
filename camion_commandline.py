# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:16:39 2020

@author: Diego
"""

import csv 
import sys 

def costo_camion(archivo):
    datos= []
    costo = 0
    with open(archivo, "rt") as file:
        next(file)  #No me importa la primera fila 
        #edgy
        rows= csv.reader(file)
        for row in rows:
            print(row)
            try:
                costo += int(row[1]) * float(row[2])
                datos.append(row)
            except ValueError:
                datos.append(0)
    return costo

if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = "Data/camion.csv"

costo = costo_camion(archivo)
print("Costo total:", costo)