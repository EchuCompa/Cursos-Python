# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 00:57:42 2020

@author: Diego
"""
import csv

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

arboleda = leer_arboles("Data/arbolado_en_espacios_verdes.csv")

#Ejercicio 3.19
# Luego de 5 horas, 23 minutos y 40 segundos logre inferir la condición necesaria.
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"]    

#Ejercicio 3.20
# Este me costo 2 horas nomas, creo que le estoy agarrando la mano
H1=[( float(arbol['altura_tot']), float(arbol["diametro"]) ) for arbol in arboleda if arbol["nombre_com"]=="Jacarandá"]  

#Ejercicio 3.21

especies1 = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


#De vuelta no hay mucha magia, la verdad que una verga los ejercicios de esta semana. Esperaba entregar algo mejor
# lo siento Ari, no soy yo, es el curso. :`(
def medidas_de_especies(especies,arboleda):
    medidas_especies= { espe :[( float(arbol['altura_tot']), float(arbol["diametro"]) ) for arbol in arboleda if arbol["nombre_com"]==espe] for espe in especies} 
    return medidas_especies

n = medidas_de_especies(especies1,arboleda)