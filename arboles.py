# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:53:31 2020

@author: Diego
"""

import csv
import matplotlib.pyplot as plt
import numpy as np


#Ejercicio 3.18

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows= csv.reader(f)
        headers = next(rows)
        arboles = []
        for row in rows:
            #Same función sólo que sin la condición de parque
            arboles.append(dict(zip(headers, row)))
    return arboles

"""
arboleda = leer_arboles("Data/arbolado_en_espacios_verdes.csv")

#Ejercicio 3.19
# Luego de 5 horas, 23 minutos y 40 segundos logre inferir la condición necesaria.
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"]    

#Ejercicio 3.20
# Este me costo 2 horas nomas, creo que le estoy agarrando la mano
H1=[( float(arbol['altura_tot']), float(arbol["diametro"]) ) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"]  

#Ejercicio 3.21

especies1 = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
"""

#De vuelta no hay mucha magia, la verdad que una verga los ejercicios de esta semana. Esperaba entregar algo mejor
# lo siento Ari, no soy yo, es el curso. :`(
def medidas_de_especies(especies,arboleda):
    medidas_especies= { espe :[( float(arbol['altura_tot']), float(arbol["diametro"]) ) for arbol in arboleda if arbol["nombre_com"]==espe] for espe in especies} 
    return medidas_especies


arboleda = leer_arboles("Data/arbolado_en_espacios_verdes.csv")
#Ejercicio 4.30

altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"]
plt.hist(altos,bins=50)
plt.figure()
#Ejercicio 4.31

diame=[ float(arbol["diametro"]) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"] 
altu = [ float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"] 

 
colors = np.random.rand(len(altu))
# Me dio paja usar S pero entendí el concepto. Acá no sirve pero se puede hacer un aréa
# en base a cierto parametro que uno quiera usar de los datos. Para "otra dimensión".
plt.scatter(diame,altu, c=colors, cmap="Accent" , alpha =0.2,)

# Parece ser que mientras más altos son mayor es su diametro, no pinta que sea lineal. 
# Si tuviera que arriesgar yo tiro que es más logaritmica.

#Ejercicio 4.32

# Separo las tuplas en dos listas. El problema fue que no use los arrays 
# y no supe cómo pasarlo de una forma más "bonita" y simple. Si hacía doble
# comprensión de listas quedaba todo apretujado. Acepto mejores ideas de hacerlo,
# son las 3 am , sepamos entender. ༼ಢ_ಢ༽

# especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# medidas = medidas_de_especies(especies, arboleda)
# alturas = {}
# diametros = {}
# for espe in especies:
#     alturas[espe] = [x[0] for x in medidas[espe]]
#     diametros[espe] = [x[1] for x in medidas[espe]]

# plt.figure()
# colores = ["red", "blue", "green"]
# for espe,color in  list(zip(especies, colores)):
#     plt.scatter(diametros[espe], alturas[espe],  c=color, alpha=0.2)
# plt.xlim(0,100) 
# plt.ylim(0,100) 
# Depende cómo definas "claro" se puede considerar que la consigna está cumplida.
# Yo creo que no, pero ya la tentación de mimir es más grande. Si tenes una forma
# más bella de hacerlo acepto sugerencias.