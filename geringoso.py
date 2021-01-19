# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:12:01 2020

@author: Diego
"""
vocales = ["a","e","i","o","u"]
cadena = "Inserte su palabra"


j=0
while j< len(cadena):
    letra = cadena[j]
    if  letra in vocales:
        # Separo la palabra "Paula" en "P...." + "...a" y luego voy metiendo
        # el jeringoso trucho donde hay una vocal
        cadena = cadena[: j] + letra + "p" + letra + cadena[j+1:]
        j += 2
    j += 1 
    print(cadena)
