# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:35:43 2020

@author: Diego
"""
#Ejercicio 3.6
def buscar_u_elemento(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  
        if z == e:   
            pos = i     
        i += 1       
    return pos

def buscar_n_elemento(lista, n):
    apari = 0  # comenzamos suponiendo que e no está 
    for i,z in enumerate(lista):  
        if z == n:   
            apari += 1          
    return apari

#Ejercicio 3.7

def maxi(lista):
    m = lista[0]
    for e in lista: 
        if (e>m):
            m= e
    return m

def mini(lista):
    m = lista[0]
    for e in lista: 
        if (e<m):
            m= e
    return m



