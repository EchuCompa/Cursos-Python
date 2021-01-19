# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:59:13 2020

@author: Diego
"""
import random

#Ejercicio 4.11
import numpy as np

temps = []
n=999
for j in range(n):
    temps.append(37.5 + random.normalvariate(0, 0.2))

def median(lista1): #También puedo importar "median()" de statistics, pero re aburrido
    lista = sorted(lista1)
    if len(lista) % 2 == 0:
        media = (lista[len(lista)//2 + 1] + lista[len(lista)//2 ]) /2 
    else:
        media = lista[len(lista)//2 + 1]
    return media

# Cómo sacar las cuartiles:
# Con un método similar que con la mediana sólo que dividiendo por 1/4 , 2/4 y 3/4.
# Y además tendría que hacer un caso para cada posible resto de divir al número por 4.

# Luego de 1 día, -23 horas y -59 minutos pude encontrar las funciones que necesitaba.
maxi = max(temps)
mini = min(temps)
prome = sum(temps)/len(temps)
media = median(temps)


# Ejercicio 4.13
# No hay mucha magia, te dicen cómo hacerlo

tempes = np.array(temps)
np.savetxt("Temperaturas.npy" , tempes)