# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:48:38 2020

@author: Diego
"""
import random 
from collections import Counter 

# Ejercicio 4.6

# def tirar():
#     tirada = []
#     for d in range(5):
#         tirada.append(random.randint(1, 6))
#     return tirada


def es_generala(tirada): #hard
    generala= False
    if tirada.count(tirada[0])==5:

        generala= True
    return generala

# N = 10000000
# salio_generala_servida = [es_generala(tirar()) for i in range(N)]
# G = sum(salio_generala_servida)
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

"""Preguntas 
1)Pues mientras más veces uno hace el experimento mayor será la precisión
2) Hay 6^5 posibles tiradas, de las cuales solo 6 posibilidades en las cuales
    hay una generala. Por lo tanto las probabilidades son de 6 / 6^5. 
    """


# Ejercicio 4.7
caras = [1,2,3,4,5,6]

def tirar(dados):
    nuevos_dados = (5-len(dados))
    dados.extend(random.choices(caras, k = nuevos_dados )) #Repone los dados que hagan falta
    return dados

def seleccio_dados(dados):
    frecue = Counter(dados)
    mas_comu = frecue.most_common(1) #Agarro el elemento más común y su frecuencia.
    dados = [mas_comu[0][0]] * mas_comu[0][1]
    return dados
    
    

def tira_3():
    tirada = []
    es_gene = False
    for tir in range(3):
        tirada = tirar(tirada) # Vuelve a tirar los dados
        if es_generala(tirada):
            es_gene = True
            break
        tirada = seleccio_dados(tirada) #Elige los dados que le convienen
    return es_gene


N = 100000
salio_generala = [tira_3() for i in range(N)]
G = sum(salio_generala)
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

