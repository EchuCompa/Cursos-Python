# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:46:06 2020

@author: Pau
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import imageio
import os



def crear_tablero_alea(n, cant_copos) :
    tab = np.repeat(0,(n)**2).reshape(n,n)
    tab[0] = -1
    tab[n-1] = -1
    
    for j in range(cant_copos):
        x = random.randint(1,tab.shape[0]-2)
        y = random.randint(1,tab.shape[1]-2)
        tab[(x,y)] = tab[(x,y)] + 1
    return tab

def crear_capacidad(n, kappa, opta):
    pes = np.repeat(0,(n)**2).reshape(n,n)
    for i in range(pes.shape[0]-1): 
        for j in range(pes.shape[1]-1):
            if opta==17 :
                pes[(i,j)] = random.randint(4, kappa)
            else :
                pes[(i,j)] = 4
    return pes

def es_borde(tablero, coord) :
    return tablero[coord] == -1    

def tirar_copo(tablero, coord):
    tablero[coord] = tablero[coord] + 1
    return tablero

def vecinos_de(tablero, coord) :
    veci = []
    f= coord[0]
    c= coord[1]
    veci.append((f+1,c))
    veci.append((f-1,c))
    veci.append((f,c+1))
    veci.append((f,c-1))
    veci.append((f+1,c-1))
    veci.append((f+1,c+1))
    veci.append((f-1,c-1))
    veci.append((f-1,c+1))
    i = 0
    veci2 = []
    while i<len(veci) :
        if not es_borde(tablero, veci[i]):
            veci2.append(veci[i])
        i = i+1 
    return veci2

def desbordar_posicion(tablero, pes) :
    for i in range(1, tablero.shape[0]-2): #Esto es desbordar_valle
        for j in range(1, tablero.shape[1]-2):
            if tablero[(i,j)] > pes[(i,j)]: #Esto es hay que desbordar
                vecin = vecinos_de(tablero, (i,j))
                h = 4 #random.randint(pes[(i,j)] , tablero[(i,j)])
                tablero[(i,j)] = tablero[(i,j)] - h
#                for k in range(h) :
#                    x = random.randint(0, len(vecin)-1)
#                    tablero[vecin[x]]= tablero[vecin[x]] + 1
                for m in range(4):
                    tablero[vecin[m]]= tablero[vecin[m]] + 1                
    return tablero
                    
def estabilizar(tablero, pes) :
    segui = False
    copos = 0
    for i in range(1, tablero.shape[0]-2): #Esto es desbordar_valle
        for j in range(1, tablero.shape[1]-2):
            if tablero[(i,j)] > pes[(i,j)]: #Esto es hay que desbordar
                segui = True
    if segui== False : #Se estan distribuyendo copos demás, la pregunta es porque
        for i in range(1, tablero.shape[0]-2): #Esto es desbordar_valle
              for j in range(1, tablero.shape[1]-2):  
                  copos= copos + tablero[(i,j)]
        print("Los copos totales son", copos)
    
    return segui

def paso(tablero, pes):
    tablero[int(tablero.shape[0]/2), int(tablero.shape[1]/2) ] = tablero[int(tablero.shape[0]/2), int(tablero.shape[1]/2) ] + 2 #Asi lo tira en la mitad del tablero
#    i = random.randint(1,tablero.shape[0]-2)
#    j = random.randint(1,tablero.shape[1]-2)
#    tablero[(i,j)] = tablero[(i,j)] + 1
    while estabilizar(tablero, pes)==True:
         desbordar_posicion(tablero, pes)       
    return tablero
                    
def guardar_foto(t, paso, kappa) :
    dir_name = "output"
    if not os.path.exists(dir_name): # me fijo si no existe el directorio
        os.mkdir(dir_name) #si no existe lo creo
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=kappa-1)
    plt.colorbar()
    ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
    plt.savefig(file_name)   
    print(file_name)
    plt.clf()
    
def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos=[]
    for i in range (cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))
    video_name = os.path.join(dir_name, "avalancha2.mp4")
    # genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print('Estamos trabajando en el directorio', os.getcwd())
    print('y se guardo el video:', video_name)


def probar(n, pasos, cantcop,   kappa, opta):
    t = crear_tablero_alea(n, cantcop)
    p = crear_capacidad(n, kappa, opta)
    for i in range(pasos):
        paso(t, p)
        guardar_foto(t, i, kappa)
    hacer_video(pasos)
    return t

#probar(60, 3000, 0, 10, 16)
r= crear_tablero_alea(5, 10)
    
     
        
        
