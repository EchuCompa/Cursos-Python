# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:02:14 2020

@author: Diego
"""
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

t = random.sample(naipes, k=3)

def envido(mano1):
    envidos = []
    mano = valores_reyes(mano1)
    mayor_numero = max(mano)[0]
    envidos.append(mayor_numero)
    for i in range(2): # Hago una comparación al pedo pero el código queda más legible.
        if mano[i][1] ==  mano[i+1][1]:
            envidos.append(20+mano[i][0]+ mano[i+1][0])
        if mano[i][1] == mano[i-1][1]:
            envidos.append(20+mano[i][0]+ mano[i-1][0])
    return max(envidos)

        
#Lo empece en hacer cómo una comprensión de lista pero me complico el cambio de valor
# si se te ocurre cómo hacerlo bienvenido sea.
def valores_reyes(mano):
    nuevos_valores = []
    for valor, palo in mano:
        if valor >= 10:
            valor = 0
        nuevos_valores.append((valor, palo))
    return nuevos_valores

N = 1000000
envidos = [ envido(random.sample(naipes, k=3)) for k in range(N)]

for envi in range(31,34):
    proba = envidos.count(envi)/len(envidos)
    print(f"La probabilidad de tener {envi} de envido es de {proba}")
    
"""Preguntas (aunque le debería decir respuestas pero ya quedo el formato)
1)No son iguales las tres probabilidades, ya que las combinaciones posibles para obtener 
31 son mayores que las probabilidades de obtener 32 y 33. #{(7,4),(6,5)} > #{(7,5)} or
#{(7,6)} """