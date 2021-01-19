# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:24:47 2020

@author: Diego
"""
def propaga(lista):
    for x in range(2): # Hago una pasada de derecha a izquierda y luego viceversa
        for i,e in enumerate(lista): 
            if e== 1:
                if i<(len(lista)-1) and lista[i+1]==0: #Me fijo que no sea el último elemento
                    lista[i+1] = 1
        print(lista)
        lista = lista[::-1] #Invierto la lista
    return lista



t = propaga([1,0,0,0,-1,0,0,1,0,0,-1,0,0,1])