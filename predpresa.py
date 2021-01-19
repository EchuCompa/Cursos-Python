# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:30:30 2020

@author: Pau
"""
import random
import numpy as np


def generar_tablero_azar(filas, columnas, n_antilopes, n_leones ) :
    tab = np.repeat(" ",(filas+2) *(columnas+2)).reshape(filas+2, columnas+2)
    tab1 = np.repeat(" ",(filas+2) *(columnas+2)).reshape(filas+2, columnas+2)
    tab[0] = "M"
    tab[filas+1] = "M"
    for i in range(0, filas+1, 1 ): 
        tab[(i,0)] = "M"
        tab[(i,columnas+1)] = "M"
    posi = mezclar_celdas(tab1)
    ani= []
    for z in range(n_antilopes):
        ani.append("A")
    for j in range(n_leones):
        ani.append("L")
    for k in range(len(ani)):
        tab[posi.pop(0)]= ani.pop(0) 
    return tab

def es_borde(tablero, coord) :
    return tablero[coord] == "M"

def vecinos_de(tablero, coord) :
    veci = []
    f= coord[0]
    c= coord[1]
    veci.append((f-1,c-1))
    veci.append((f-1,c))
    veci.append((f-1,c+1))
    veci.append((f,c+1))
    veci.append((f+1,c+1))
    veci.append((f+1,c))
    veci.append((f+1,c-1))
    veci.append((f,c-1))
    i = 0
    veci2 = []
    while i<len(veci) :
        if not es_borde(tablero, veci[i]):
            veci2.append(veci[i])
        i = i+1 
#    random.shuffle(veci2) De esta forma se cumple el optativo 14 técnicamente
    return veci2

def buscar_adyacente(tablero, coord, objetivo):
    i = 0
    veci = vecinos_de(tablero, coord)
    co = []
    while co == [] and i<len(veci):
        ver = veci[i]
        if tablero[(ver)]== objetivo:
                co= veci[i]
        i = i+1
    return co

def alimentar(tablero, lista_leo, lista_anti):
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i,j)] == "L" :
                comida = buscar_adyacente(tablero, (i,j), "A") 
                if comida != [] :
                    if tablero[comida] == "A" :
                        tablero[(i,j)] = " "
                        tablero[comida] = "L" 
    return tablero

def reproducir(tablero, lista_leo, lista_anti):
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i,j)] != " " :
                pare = tablero[(i,j)]
                hayamor =  buscar_adyacente(tablero, (i,j), pare)
                if hayamor != [] :
                    futu_cria =  buscar_adyacente(tablero, (i,j), " ")
                    if futu_cria != [] :
                        tablero[futu_cria] = pare
    return tablero

def mover(tablero, lista_leo, lista_anti):  
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i,j)] != " " :
                movi1 = tablero[(i,j)] 
                movi = buscar_adyacente(tablero, (i,j), " ")
                if movi != [] :
                    tablero[(i,j)] = " "
                    tablero[(movi)] = movi1
    return tablero

def evolucionar(tablero) :
    tab1 = alimentar(tablero)
    tab2 = reproducir(tab1)
    tab3 = mover(tab2)
    return tab3

def evolucionar_tiempo(tablero, k) :
    tab = tablero
    for i in range(k):
        evolucionar(tab)
    return tab

def mezclar_celdas(tablero):
    celdas = []
    for i in range (1 , tablero.shape[0]-1, 1) :
            for j in range (1 , tablero.shape[1]-1, 1) :
                    celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def cuantos_cada(tablero):
    ani = [0,0]
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i,j)] == "A" :
                ani[0] = ani[0] +1
            if tablero[(i,j)] == "L" :
                ani[1] = ani[1] +1
    return ani

def registrar_evolucion(tablero, k):
    tab = tablero
    anim = []
    for i in range(k):
        evolucionar(tab)
        anim.append(cuantos_cada(tab))
        print(tab)
    return anim

tab1 = generar_tablero_azar(15, 9, 10, 2)
resu = registrar_evolucion(tab1, 10)                

