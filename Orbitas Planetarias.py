# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:20:06 2020

@author: Pau
"""
import imageio
import numpy as np
import matplotlib.pyplot as plt

def calcula_delta(x_sol, x_tierra):
    distan= x_sol-x_tierra
    return distan

def calcula_distancia(pos_sol, pos_tierra):
    distancia = np.sqrt(calcula_delta(pos_sol[0], pos_tierra[0])**2+calcula_delta(pos_sol[1], pos_tierra[1])**2)
    return distancia

def calcula_aceleracion(pos_sol, pos_tierra):
    G = 6.674e-11 
    M = 1.98e30
    distx = calcula_delta(pos_sol[0], pos_tierra[0])
    disty = calcula_delta(pos_sol[1], pos_tierra[1])
    dista= calcula_distancia(pos_sol, pos_tierra)
    ax = (G*M/(dista**2))*distx/dista
    ay = (G*M/(dista**2))*disty/dista
    return [ax, ay]

lista_aceleracion_x =[0]
lista_aceleracion_y =[0]
pos_sol = [0,0]
x_lista = [-147095000000.0, -147095000000.0] 
y_lista = [0.0, 2617920000.0]
dt = 86400
tiempo_total = 400
dia = [0]

def realiza_verlet(pos_anterior, pos_actual, dt):
    aceleracion_actual = calcula_aceleracion(pos_sol, pos_actual )
    pos_posterior = []
    pos_posterior.append(2*pos_actual[0]-pos_anterior[0]+aceleracion_actual[0]*dt**2)
    pos_posterior.append(2*pos_actual[1]-pos_anterior[1]+aceleracion_actual[1]*dt**2)
    return pos_posterior

for i in range (1, tiempo_total-1):
    pos_anterior=[x_lista[i-1],y_lista[i-1]] 
    pos_actual= [x_lista[i],y_lista[i]] 
    aceleracion = calcula_aceleracion(pos_sol ,pos_actual )
    pos_posterior = realiza_verlet(pos_anterior, pos_actual, dt)
    x_lista.append(pos_posterior[0])
    y_lista.append(pos_posterior[1])
    lista_aceleracion_x.append(aceleracion[0])
    lista_aceleracion_y.append(aceleracion[1])
    dia.append(i)    
aceleracion = calcula_aceleracion(pos_sol ,pos_actual )  
lista_aceleracion_x.append(aceleracion[0])
lista_aceleracion_y.append(aceleracion[1]) 
plt.figure()

def hacer_foto(x_lista, y_lista, pos_sol, dia, acele_x, acele_y):
    plt.clf()
    plt.plot(x_lista, y_lista,'grey')
    plt.plot(0,0, 'yo', ms=20)
    plt.plot(x_lista[dia], y_lista[dia], 'bo', ms=10)
    plt.arrow(x_lista[dia], y_lista[dia], acele_x[dia]*10**12.5, acele_y[dia]*10**12.5, width =10**9.5 , Color ="g" )

def hacer_video ( x_lista , y_lista , pos_sol , nombre_video, acele_x, acele_y ) :
    lista_fotos =[] 
    for i in range (len ( x_lista ) ) :
        if i%2==0: 
            hacer_foto( x_lista , y_lista , pos_sol , i, acele_x, acele_y)
            plt.savefig(nombre_video+'.png')
            lista_fotos . append ( imageio . imread ( nombre_video +'.png') )
        print (str( i ) +'de '+str(len(x_lista ) ) + ' fotos guardadas ')
    imageio.mimsave( nombre_video +'.mp4', lista_fotos ) 
    print ('Video Guardado ')
 
#aver = hacer_video(x_lista, y_lista, pos_sol, 'Esperoquefunque', lista_aceleracion_x, lista_aceleracion_y)

def gráfico_velocidad(x_lista, y_lista):
    velocidad_x = []
    velocidad_y = []
    for i in range(0, len(x_lista)-1, 2):
        velocidad_x.append(calcula_delta(x_lista[i], x_lista[i+1])/2)
        velocidad_y.append(calcula_delta(y_lista[i], y_lista[i+1])/2)
    plt.plot( velocidad_x, "blue")
    plt.plot( velocidad_y, "red")
    plt.xlabel("Rojo=Velocidad en Y", color="red")
    plt.ylabel("Azul=Velocidad en X", color="blue")
    plt.title( "Velocidades a lo largo del tiempo (metros/dia)", color="green")
    plt.show()
    
gráfico_velocidad(x_lista, y_lista)
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    