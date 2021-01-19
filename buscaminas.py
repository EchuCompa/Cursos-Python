# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:56:28 2020

@author: Diego
"""
import random
import numpy as np

def crear_tablero_minado(filas, columnas, bombas, coord) :
    tab = np.repeat(0,(filas) *(columnas)).reshape(filas, columnas)
    tab1 = np.repeat(0, (filas) *(columnas)).reshape(filas, columnas)
    posi = mezclar_celdas(tab1)
    for k in range(bombas):
        if posi[k] != coord:
            tab[posi[k]]= -1
    poner_numeros(tab)
    return tab

def crear_mapa(tab):
    tabler = np.repeat(".",tab.shape[0]*tab.shape[1]).reshape(tab.shape[0], tab.shape[1])
    return tabler


def mezclar_celdas(tablero):
    celdas = []
    for i in range (tablero.shape[0]) :
            for j in range (tablero.shape[1]) :
                    celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def en_rango(tab, coord):
    esta = True
    if coord[0] < 0 or coord[0] > tab.shape[0]-1 or coord[1] < 0 or coord[1] > tab.shape[1]-1:
        esta = False
    return esta

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
        if en_rango(tablero, veci[i]):
            veci2.append(veci[i])
        i = i+1 
    return veci2

def poner_numeros(tab):
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]): 
            if tab[(i,j)] != -1 :
                vecis = vecinos_de(tab, (i,j))
                minas = 0
                for b in range(len(vecis)):
                    if tab[vecis[b]]== -1:
                        minas +=1
                tab[(i,j)] = minas
                
def seguir_jugando(mapa, tab):
    jugar = False
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]): 
            if mapa[(i,j)] == "." and tab[(i,j)] != -1 :
                jugar = True
    return jugar 

def tocar(coord, mapa, tablero_oculto):
    toque = True
    if mapa[coord] == ".":
        if tablero_oculto[coord] != -1:
            mapa[coord] = tablero_oculto[coord]
            if tablero_oculto[coord]== 0:
                vecin = vecinos_de(mapa, coord)
                for v in range(len(vecin)):
                    mapa[vecin[v]] = tablero_oculto[vecin[v]]
        else:
            mapa[coord] = "X"
            toque = False
    else:
        print("Ya fue elegida esa posición, elija otra")
    return toque
        
     
             
def jugar_partida():
    fi = 9
    co = 9
    minas = 20
    comienzo=True
    mapa = crear_mapa(np.repeat(".",fi*co).reshape(fi, co))
    while comienzo == True:
        f1 = int(input("Introduzca la fila de su celda elegida: "))
        c1 = int(input("Introduzca la columna de su celda elegida: "))
        if en_rango(mapa, (f1,c1)):
            comienzo = False
        else:
            print("Coordenadas fuera de rango, ingrese de nuevo")
    oculto = crear_tablero_minado(fi,co, minas, (f1,c1))
    tocar((f1,c1), mapa, oculto)
    juego = [True,True]
    while not False in juego:
        print(mapa)
        f = int(input("Introduzca la fila de su celda elegida: "))
        c = int(input("Introduzca la columna de su celda elegida: "))
        if en_rango(oculto, (f,c)):
            juego[0] = tocar((f,c), mapa, oculto)
            juego[1] = seguir_jugando(mapa, oculto)
            if juego[0] == False:
                print("Kabuuum!! Mejor suerte la próxima ;")
            elif juego[1]== False:
                print("Ganaste!! Animal, bestia, master, crack, champion!!")
        else:
            print("Coordenadas fuera de rango, ingrese de nuevo")
    
# jugar_partida()    
    
        
        
        
        
        
        

