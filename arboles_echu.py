# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 00:01:20 2020

@author: Diego
"""
import csv
from collections import Counter

# Ejercicio 2.22
def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows= csv.reader(f)
        headers = next(rows)
        arboles = []
        for row in rows:
            #Si el arbol pertenece al parque que busco entonces lo agrego, easy enough
            if row[headers.index("espacio_ve")] == parque:
                arboles.append(dict(zip(headers, row)))
    return arboles

#Ejercicio 2.23
def especies(lista_arboles):
    especi = []
    for arbol in lista_arboles:
        # Si la especie ya está en la lista entonces no la agrego para que no haya repetidas, aunque es mejor hacerlo con un set, je
        # sipe yo lo hice con set
        if arbol["nombre_com"] not in especi:
            especi.append(arbol["nombre_com"])
    return especi

# general_paz = leer_parque("Data/arbolado_en_espacios_verdes.csv", "GENERAL PAZ")
# cente = leer_parque("Data/arbolado_en_espacios_verdes.csv", "CENTENARIO")
los_andes = leer_parque("Data/arbolado_en_espacios_verdes.csv", "EJERCITO DE LOS ANDES")
# especie = especies(general_paz)

#Ejercicio 2.24
def contar_ejemplares(lista_arboles):
    cantidad_ejemplares = Counter()
    for arbol in lista_arboles:
        # Sumo 1 al contador cada vez que aparece la especie en los árboles del parque
        cantidad_ejemplares[arbol["nombre_com"]] += 1
    print(cantidad_ejemplares.most_common(5))
    return cantidad_ejemplares

# ejem_genpaz= contar_ejemplares(general_paz)

# Siento que los comentarios que estoy haciendo son medio obvios y sin sentido, así que
# de ahora en más sólo voy a comentar cuándo sea necesario o vea que la función puede ser confusa

#Ejercicio 2.25
def obtener_alturas(lista_arboles, especie):
    alturas= []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            alturas.append(float(arbol["altura_tot"]))
    return alturas

# jaca_genpaz = obtener_alturas(general_paz, "Jacarandá")
# max_jaca_genpaz = max(jaca_genpaz)
# prome_jaca_genpaz = sum(jaca_genpaz) / len(jaca_genpaz)

#Ejercicio 2.26
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones= []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inclinaciones.append(float(arbol["inclinacio"]))
    return inclinaciones

# inclinacio_genpaz = obtener_inclinaciones(general_paz, "Jacarandá")

#Ejercicio 2.27
def especimen_mas_inclinado(lista_arboles):
    inclinaciones = []
    especie = especies(lista_arboles)
    # Aca voy obteniendo el árbol más inclinado de cada especie
    for esp in especie:
        inclinaciones.append(max(obtener_inclinaciones(lista_arboles, esp)))
    # Devuelvo la especie con el árbol más inclinado
    return (especie[inclinaciones.index(max(inclinaciones))], max(inclinaciones))

especi_los_andes = especies(los_andes)
# especi_cente = especimen_mas_inclinado(cente)

#Ejercicio 2.28
def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones = []
    especie = especies(lista_arboles)
    # Aca voy obteniendo el promedio de inclinación de cada especie
    for esp in especie:
        incli = obtener_inclinaciones(lista_arboles, esp)
        prome_espe = sum(incli)/len(incli)
        print(prome_espe, esp)
        inclinaciones.append(prome_espe)
    # Devuelvo la especie con el mayor promedio de inclinación
    return (especie[inclinaciones.index(max(inclinaciones))], max(inclinaciones))

especie_mas_inclinada = especie_promedio_mas_inclinada(los_andes)
    
# es medio aburrido que esté todo tan bien (?) porque tengo ganas de comentar cosas
# pero no le puedo marcar nada
# mentira si:
# PORQUÉ abreviás genpaz cuando ya existe gral como abreviatura de general???????????????
# onda es mucho más legible y simpático gralpaz
# ah se fijaba en eso bue
# pero en serio muy lindas tus funciones! felicitaciones