# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:04:03 2020

@author: Diego
"""
frutas = "Melon," + 'Manzana,Naranja,Mandarina,Banana,Kiwi' + ",Pera"

cadena = "Ejemplo con for"
cant  = 0
for c in cadena:
    if c == "o":
        cant += 1

lista_frutas = frutas.split(",")

