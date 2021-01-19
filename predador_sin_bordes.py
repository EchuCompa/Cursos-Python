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
    posi = mezclar_celdas(tab1)
    ani= []
    for z in range(n_antilopes):
        ani.append("A")
    for j in range(n_leones):
        ani.append("L")
    for k in range(len(ani)):
        tab[posi.pop(0)]= ani.pop(0) 
    print(tab)
    return tab



def vecinos_de(tablero, coord) :
    veci = [0,0,0,0,0,0,0,0]
    f= coord[0]
    c= coord[1]
    fult = tablero.shape[0]-1
    cult = tablero.shape[1]-1
    if f==0 :
        veci[1]= (fult, c) #Escribi el código de esta forma para respetar el orden de los vecinos
        if c == 0 :
            veci[0]= (fult, cult)
        else:
            veci[0]= (fult, c-1)
        if c==cult:
            veci[2] = (fult, 0)
        else:
            veci[2]= (fult, c+1)
    else:
        veci[1]= (f-1,c)
    if f==fult:
        veci[5]= (0, c)
        if c==0:
            veci[6]= (0, cult)
        else:
            veci[6]= (0, c-1)
        if c==cult:
            veci[4]= (0,0)
        else:
            veci[4]= (0, c+1)
    else:
        veci[5] = (f+1, c)              
    if c==0 :
        veci[7] = (cult , f)
    else:
        veci[7] = (f,c-1)
    if c==cult:
        veci[3]= (f, 0)
    else:
        veci[3] = (f,c+1)
#    veci[0] = (f-1,c-1), veci[1] = (f-1,c), veci[2] = (f-1,c+1), veci[3] = (f,c+1), veci[4] = (f+1,c+1), veci[5] = (f+1,c),veci[6] = (f+1,c-1), veci[7] = (f,c-1)
#    random.shuffle(veci2) De esta forma se cumple el optativo 14 técnicamente
    return veci

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

def alimentar(tablero):
       for i in range(0, tablero.shape[0]-1): 
            for j in range(0, tablero.shape[1]-1):
                if tablero[(i,j)] == "L" :
                    comida = buscar_adyacente(tablero, (i,j), "A") 
                    if comida != [] :
                        if tablero[comida] == "A" :
                            tablero[(i,j)] = " "
                            tablero[comida] = "L" 
       return tablero

def reproducir(tablero):
    for i in range(0, tablero.shape[0]-1): 
        for j in range(0, tablero.shape[1]-1):
            if tablero[(i,j)] != " " :
                pare = tablero[(i,j)]
                hayamor =  buscar_adyacente(tablero, (i,j), pare)
                if hayamor != [] :
                    futu_cria =  buscar_adyacente(tablero, (i,j), " ")
                    if futu_cria != [] :
                        tablero[futu_cria] = pare
    return tablero

def mover(tablero):  
    for i in range(0, tablero.shape[0]-1): 
        for j in range(0, tablero.shape[1]-1):
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
    for i in range(0, tablero.shape[0]-1): 
        for j in range(0, tablero.shape[1]-1):
                    celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def cuantos_cada(tablero):
    ani = [0,0]
    for i in range(tablero.shape[0]-1): 
        for j in range(tablero.shape[1]-1):
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

tab1 = generar_tablero_azar(12, 9, 5, 3)
#resu = registrar_evolucion(tab1, 10)
jaja = vecinos_de(tab1, (0,0))                

