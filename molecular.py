# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:45:37 2020

@author: Pau
"""
import random
import numpy as np

salida=open("salida.xyz","w")

 #Bordes taim!!!
def rebotar(pos, vel, mini, maxi) :    
     if pos > maxi:
        vel = -vel
        pos = pos - 2*(pos - maxi)
     if pos < mini :
       vel = -vel
       pos = pos - 2*(pos - mini)
     return [pos, vel]

def mover_particula(pos_x, pos_y, vel_x, vel_y, dt, x_min, x_max, y_min, y_max):
    posi =  [pos_x + vel_x*dt]
    posi.append( pos_y + vel_y*dt)
    checkx = rebotar(posi.pop(0), vel_x, x_min, x_max)
    checky = rebotar(posi.pop(0), vel_y, y_min, y_max)
    posi.append(checkx.pop(0))
    posi.append(checky.pop(0))
    velo = [checkx.pop(0)]
    velo.append(checky.pop(0))
    return [posi, velo]
    
def escribir_frame(archivo, pos_x, pos_y):    
    print("1",file=salida)
    print(" ",file=salida)
    print("6", pos_x, pos_y , "0", file=salida)
    

def dist_cuadrada(p1, p2):
    distancia = (p1[0] - p2[0])**2+(p1[1] - p2[1])**2
    return distancia

def calcular_fuerzas(pos_x, pos_y, k):
    fuerzas_x = []
    fuerzas_y = []
    for i in range(len(pos_x)):
        fuerzax = 0
        fuerzay = 0
        for j in range(len(pos_x)-1):
            if i != j:
                dist = dist_cuadrada([pos_x[i], pos_y[i]], [pos_x[j], pos_y[j]])
                fuerzax += 4*k*(pos_x[i] - pos_x[j])/dist**3 - 2*k2*(pos_x[i] - pos_x[j])/dist**2  
                fuerzay += 4*k*(pos_y[i] - pos_y[j])/dist**3 - 2*k2*(pos_y[i] - pos_y[j])/dist**2
        fuerzas_x.append(fuerzax)
        fuerzas_y.append(fuerzay) 
    return [fuerzas_x, fuerzas_y]

def aplicar_fuerzas(fuerzas_x, fuerzas_y, vel_x, vel_y ,masas) :
    for i in range(len(fuerzas_x)):
        vel_x[i] += fuerzas_x[i]/ masas[i]*dt  
        vel_y[i] += fuerzas_y[i]/ masas[i]*dt
        
def suma_energias(pos_x, pos_y, vel_x, vel_y,  masas, k, energias):
    for i in range(len(vel_x)):
        energias[i] = 1/2*masas[i]*(vel_x[i]**2+vel_y[i]**2)
        for j in range(len(pos_x)) :
            if j != i:
                energias[i] += k/dist_cuadrada([pos_x[i], pos_y[i]], [pos_x[j], pos_y[j]]) 
                

def dinamica(dt, k, k2,  min_x, max_x, min_y, max_y, pasos_totales, n_parts):
    #Creacion de listas necesarias pa la simulación.
    energias = np.zeros(n_parts)
    pos_x = []
    pos_y = []
    vel_x = []
    vel_y = []
    masas= [] 
    letsee = 0
    for i in range(n_parts) :
        pos_x.append(random.random()*30)
        pos_y.append(random.random()*30)
        vel_x.append(random.random()*2-1)
        vel_y.append(random.random()*2-1)
        masas.append(1)
    for i in range(pasos_totales):
        fuerzas = calcular_fuerzas(pos_x, pos_y, k)
        aplicar_fuerzas(fuerzas[0], fuerzas[1], vel_x, vel_y, masas)
        suma_energias(pos_x, pos_y, vel_x, vel_y, masas, k, energias)
        if (i % 100) == 0:
            print(n_parts, file=salida)
            print(" ", file=salida)
            for i in range(len(energias)):
                letsee += energias[i]
            print(letsee)
            energias = np.zeros(n_parts) 
        for j in range(n_parts):
            move = mover_particula(pos_x[j], pos_y[j], vel_x[j], vel_y[j], dt, min_x, max_x, min_y, max_y)
            posi_actual = move[0]
            velo_actual = move[1]
            if (i % 100) == 0:
                print("8", pos_x[j], pos_y[j] , "0", file=salida)
                #escribir_frame(salida, pos_x[j], pos_y[j])
            pos_x[j] = posi_actual[0]
            pos_y[j] = posi_actual[1]
            vel_x[j] = velo_actual[0]
            vel_y[j] = velo_actual[1]
    salida.close()
    
min_x = 0
max_x = 30.0
min_y = 0
max_y = 30.0

pasos_totales = 10000
dt = 0.05
k = 1
k2 = 1
n_parts = 10

dinamica(dt, k, k2,  min_x, max_x, min_y, max_y, pasos_totales, n_parts)

