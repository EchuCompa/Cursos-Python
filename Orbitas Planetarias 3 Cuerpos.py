# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:43 2020

@author: Diego
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

def calcula_delta(x_sol, x_tierra):
    distan= x_tierra-x_sol
    return distan

def calcula_distancia(pos_sol, pos_tierra):
    distancia = np.sqrt(calcula_delta(pos_sol[0], pos_tierra[0])**2+calcula_delta(pos_sol[1], pos_tierra[1])**2)
    return distancia

pos_sol = [0.0,0.0]
x_lista1 = [-147095000000.0, -147095000000.0] #Estos son los valores de la Tierra
y_lista1 = [0.0, 2617920000.0]
x_lista2 = [-147481000000.0, -147481000000.0] #Estos son los valores de la Luna
y_lista2 = [0.0 , 2617920000.0]
M3 = 5.97e24 #Masa de la Tierra
M2 = 7.35e22 #Masa de la Luna
M = 1.99e30 #Masa del Sol
dt = 86400
tiempo_total = 50
dia = np.arange(1, tiempo_total-1)

#Ya que no son listas, sino que arrays, pero las dejo anota
lista_aceleracion_x = np.zeros(tiempo_total) #Aceleraciones de la Tierra
lista_aceleracion_y = np.zeros(tiempo_total)

lista_aceleracion_x2 = np.zeros(tiempo_total) #Aceleraciones de la Luna
lista_aceleracion_y2 = np.zeros(tiempo_total)
#Puedo de alguna forma meter una variable que vaya cambiando a que lista yo mando las cosas


def calcula_aceleracion(pos_planeta1, pos_planeta2, planeta, pos_acele):
    G = 6.674e-11 
    distx = calcula_delta(pos_planeta1[0], pos_planeta2[0])
    disty = calcula_delta(pos_planeta1[1], pos_planeta2[1])
    dista= calcula_distancia(pos_planeta1, pos_planeta2)
    if planeta==-1 or planeta==-2: # Significa que la fuerza es ejercida por el sol
        ax = (G*M/(dista**2))*distx/dista
        ay = (G*M/(dista**2))*disty/dista
        if planeta==-1: #Del Sol a la Tierra
            lista_aceleracion_x[pos_acele] =    lista_aceleracion_x[pos_acele] + ax
            lista_aceleracion_y[pos_acele] =    lista_aceleracion_y[pos_acele] + ay
        else: #Del Sol a la Luna
            lista_aceleracion_x2[pos_acele] =    lista_aceleracion_x2[pos_acele] + ax
            lista_aceleracion_y2[pos_acele] =    lista_aceleracion_y2[pos_acele] + ay
    if planeta==1 : # Significa que la fuerza es ejercida por la Tierra
        ax = (G*M3/(dista**2))*distx/dista
        ay = (G*M3/(dista**2))*disty/dista
        lista_aceleracion_x2[pos_acele] =    lista_aceleracion_x2[pos_acele] + ax
        lista_aceleracion_y2[pos_acele] =    lista_aceleracion_y2[pos_acele] + ay
    if planeta==2 : # Significa que la fuerza es ejercida por la Luna
        ax = (G*M2/(dista**2))*distx/dista
        ay = (G*M2/(dista**2))*disty/dista
        lista_aceleracion_x[pos_acele] =    lista_aceleracion_x[pos_acele] + ax
        lista_aceleracion_y[pos_acele] =    lista_aceleracion_y[pos_acele] + ay
    

def realiza_verlet(pos_anterior, pos_actual, dt, aceleracion_actual):
    pos_posterior = []
    pos_posterior.append(2*pos_actual[0]-pos_anterior[0]+aceleracion_actual[0]*dt**2)
    pos_posterior.append(2*pos_actual[1]-pos_anterior[1]+aceleracion_actual[1]*dt**2)
    return pos_posterior

def recorrido(x_lista, y_lista, x_lista2, y_lista2) :
    for i in range (1, tiempo_total-1):
        pos_anterior=[x_lista[i-1],y_lista[i-1]] 
        pos_actual= [x_lista[i],y_lista[i]]
        pos_anterior2=[x_lista2[i-1],y_lista2[i-1]] 
        pos_actual2= [x_lista2[i],y_lista2[i]]
        calcula_aceleracion(pos_actual, pos_actual2, 2, i-1)  #Aceleración de la Tierra
        calcula_aceleracion(pos_actual, pos_sol, -1, i-1)
        calcula_aceleracion(pos_actual2, pos_actual, 1, i-1)  #Aceleración de la Luna
        calcula_aceleracion(pos_actual2, pos_sol, -2, i-1)
        pos_posterior = realiza_verlet(pos_anterior, pos_actual, dt, [lista_aceleracion_x[i],lista_aceleracion_y[i]] )
        pos_posterior2 = realiza_verlet(pos_anterior2, pos_actual2, dt, [lista_aceleracion_x2[i],lista_aceleracion_y2[i]] )
        x_lista.append(pos_posterior[0])
        y_lista.append(pos_posterior[1])
        x_lista2.append(pos_posterior2[0])
        y_lista2.append(pos_posterior2[1])
    # Estos son los últimos valores de aceleraciones que se crean. Es necesario, no?
    calcula_aceleracion([x_lista1[tiempo_total-2], y_lista1[tiempo_total-2]], [x_lista1[tiempo_total-1], y_lista1[tiempo_total-1]], 2, tiempo_total-1)  #Aceleración de la Tierra
    calcula_aceleracion([x_lista1[tiempo_total-1], y_lista1[tiempo_total-1]], pos_sol, -1, tiempo_total-1)
    calcula_aceleracion([x_lista2[tiempo_total-2], y_lista2[tiempo_total-2]], [x_lista2[tiempo_total-1], y_lista2[tiempo_total-1]], 1, tiempo_total-1)  #Aceleración de la Tierra
    calcula_aceleracion([x_lista2[tiempo_total-1], y_lista2[tiempo_total-1]], pos_sol, -2, tiempo_total-1)
    plt.figure()


def hacer_foto(x_lista, y_lista, x_lista1, y_lista1,  pos_sol, dia, acele_x, acele_y, acele_x1, acele_y1):
    plt.clf()
    plt.plot(x_lista, y_lista,'grey')
    plt.plot(x_lista1, y_lista1,'green')
    plt.plot(0,0, 'yo', ms=60)
    plt.plot(x_lista1[dia], y_lista1[dia], "ko" , ms=10)
    plt.plot(x_lista[dia], y_lista[dia], 'bo', ms=20)
    plt.arrow(x_lista[dia], y_lista[dia], acele_x[dia]*10**12.5, acele_y[dia]*10**12.5, width =10**9.5 , Color ="g" )
    plt.arrow(x_lista1[dia], y_lista1[dia], acele_x1[dia]*10**12.5, acele_y1[dia]*10**12.5, width =10**9.5 , Color ="r" )
    plt.show() # Me sirve para ver en que me equivoque, ya se que con esto no funca
    
    
def hacer_video ( x_lista , y_lista, x_lista1 , y_lista1 , pos_sol , nombre_video, acele_x, acele_y, acele_x1, acele_y1 ) :
    lista_fotos =[] 
    for i in range (len (x_lista) ) :
        if i%2==0: 
            hacer_foto( x_lista , y_lista ,  x_lista1 , y_lista1 , pos_sol , i, acele_x, acele_y, acele_x1, acele_y1)
            plt.savefig(nombre_video+'.png')
            lista_fotos.append ( imageio.imread ( nombre_video +'.png') )
        print (str( i ) +'de '+str(len(x_lista ) ) + ' fotos guardadas ')
    imageio.mimsave( nombre_video +'.mp4', lista_fotos ) 
    print ('Video Guardado ')
   
recorrido(x_lista1, y_lista1, x_lista2, y_lista2)
aver = hacer_video(x_lista1, y_lista1, x_lista2, y_lista2, pos_sol, 'ParavosMartín', lista_aceleracion_x, lista_aceleracion_y, lista_aceleracion_x2, lista_aceleracion_y2)
