# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:10:17 2020

@author: Diego
"""
import matplotlib.pyplot as plt
import numpy as np


#Ejercicio 6.9

# fig = plt.figure()
# plt.subplot(2, 1, 1) # define la figura de arriba
# plt.plot([0,1,2],[0,1,0]) # dibuja la curva
# plt.xticks([]), plt.yticks([]) # saca las marcas

# plt.subplot(2, 3, 5) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
# plt.plot([0, 1],[0 ,0])
# plt.xticks([]), plt.yticks([])

# plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
# plt.plot([0,1],[0,1])
# plt.xticks([]), plt.yticks([])


# plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
# plt.plot([0,1],[1,0])
# plt.xticks([]), plt.yticks([])

# plt.show()

# Modificá el código anterior para ponerles nombres a los ejes ("tiempo" y distancia al origen") y al gráfico.
# Graficá 12 trayectorias en la misma figura, con diferentes colores.
# Usá la estructura de subplots sugerida en el Ejercicio 6.9 para graficar tres pubplots en una figura:
# Arriba, grande, 12 trayectorias aleatorias como en el inciso anterior
# Abajo a la izquierda la trayectoria que más se aleja del origen.
# Abajo a la derecha la trayectoria que menos se aleja del origen.
# Ojo, cuando decimos la que más o menos se aleja, nos referimos a en algún momento, no necesariamente a la que termina más cerca o más lejos.

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
M= 12

fig = plt.figure()
plt.subplot(2,1,1)
maxi, mini = (0,0)
for x in range(M): #Los distintos colores se ponen automaticamente :)
    random_walk = randomwalk(N)
    plt.plot(random_walk)
    prome = np.mean(random_walk)
    if  prome < np.mean(mini): #Acá guardo los máximos y minimos. 
        mini = random_walk
    if prome > np.mean(maxi):
        maxi = random_walk

#Título + nombre de los ejees
plt.title('12 Caminatas al Azar')
# plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.xticks([])
plt.ylim(-500,500)


plt.subplot(2,2,3)
plt.plot(maxi)
plt.xticks([])
plt.title('La que más se aleja')
plt.ylim(-500,500)

plt.subplot(2,2,4)
plt.plot(mini)
plt.xticks([])
plt.title('La que menos se aleja')
plt.ylim(-500,500)

plt.show()