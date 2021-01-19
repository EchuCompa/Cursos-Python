# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:39:30 2020

@author: Diego
"""
import random
import numpy as np
import matplotlib.pyplot as plt

# Mantengo mi postura, aguante Exactas programa loco (/◕ヮ◕)/

def crear_album(figus_total):   
    return np.zeros(figus_total)

def album_incompleto(album, amigos): # Le agregue el criterio amigos por el 4.29
    completo = False    
    for x in range(amigos):
        if x in album:
            completo = True # Si encuentra un 0,1....amigos en el albúm
            # significa que el mismo está incompleto.
            break
    return completo

def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

def cuantas_figus(figus):
    album = crear_album(figus)
    figus_compradas = 0
    while album_incompleto(album):
        figu = comprar_figu(figus)
        figus_compradas += 1
        album[figu] = 1
    return figus_compradas

#Ejercicio 4.19 + 4.20

# n_repeticiones = 1000
# figus_total = 670
# canti_figus = [cuantas_figus(figus_total) for albu in range(n_repeticiones)]
# prome = np.mean(canti_figus)
# print (f"En promedio hay que comprar {prome} figuritas para completar un albúm de {figus_total} figus")

"""Respuestas
1) ¿Creo que no influye tener paquetes en vez de figuritas ya que el proceso sería el
    mismo? Me genera dudas mi propia respuesta pero no ve en que cambiaría. Meramente 
    sería más "veloz" la obtención de figus, pero ni siquiera.
2) Cómo una lista de k figuritas.  """

def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for fig in range(figus_paquete) ]

def cuantos_paquetes(figus, figus_paquete):
    album = crear_album(figus)
    paquetes_comprados = 0
    while album_incompleto(album, 1):
        paquete = comprar_paquete(figus, figus_paquete)
        paquetes_comprados += 1
        for figu in paquete: #El hermoso proceso de pegar las figus en el álbum ♥
            album[figu] = 1
    return paquetes_comprados

# Ejercicio 4.24
# Lo hice con mil repeticiones porque mi compu puede  (▀̿̿Ĺ̯̿▀̿ ̿)  y le cambie el nombre 
# a "variable" + "1" pues pajero always. ¯\_(ツ)_/¯

# figus_paquete = 5
# n_repeticiones1 = 1000
# figus_total1 = 670
# canti_figus1 = [cuantos_paquetes(figus_total1, figus_paquete) for albu in range(n_repeticiones1)]
# prome1 = np.mean(canti_figus1)
# print (f"En promedio hay que comprar {prome1} paquetes para completar un albúm de {figus_total1} figus")

# Ejercicio 4.25

# cracks_con_suerte = np.array(canti_figus1) <= 850
# chance_850 = np.sum(cracks_con_suerte) / len(cracks_con_suerte)
# funcara___ = cracks_con_suerte.mean() # Funco y queda más lindo así, pareciera que entiendo algo

#Ejercicio 4.26

# plt.hist(canti_figus1, bins=150)

#Ejercicio 4.27

# Rta: Mirando el gráfico tiraría que 1100 paquetes pero vamos a asegurarnos mejor..

# echu_la_pego = False
# rta_correcta = 0
# for paque in range(1100,1200,20):
#     proba = np.mean(np.array(canti_figus1) >= paque)
#     if proba >= 0.9 and paque <= 1100:
#         echu_la_pego = True
#         print(proba, paque)
#     elif proba >= 0.9 and rta_correcta == 0:
#         rta_correcta = paque

# # Le dejo al corrector que compruebe por su cuenta.
# if echu_la_pego:
#     print("Alto crack")
# else:
#     print(f"Comprate anteojos máster, es obvio que la cantidad de paquetes era {rta_correcta}")

#Ejercicio 4.28

# Use la función sample ya que no me agarra repetidas y pa usar lo aprendido
def comprar_paquete_no_repe(figus_paquete, lista_figus):
    return random.sample(lista_figus, k =figus_paquete)
    
def cuantos_paquetes_no_repe(figus, figus_paquete, amigos):
    album = crear_album(figus)
    paquetes_comprados = 0
    figuritas = list(range(figus))
    while album_incompleto(album, amigos):
        paquete = comprar_paquete_no_repe(figus_paquete, figuritas)
        paquetes_comprados += 1
        for figu in paquete: #El hermoso proceso de pegar las figus en el álbum ♥
            album[figu] += 1 #Acá le agrego un más por el ejercicio 4.29
    return paquetes_comprados

# De vuelta procedo a usar nombres súper declarativos y claros por suerte.

# figus_paquete1 = 5
# n_repeticiones2 = 1000
# figus_total2 = 670
# canti_figus2 = [cuantos_paquetes_no_repe(figus_total2, figus_paquete1, 1) for albu in range(n_repeticiones2)]
# prome2 = np.mean(canti_figus2)
# print (f"En promedio hay que comprar {prome2} paquetes (sin repes) para completar un albúm de {figus_total2} figus")

# Siento que la medida disminuiría la capacidad de relacionarse de los niños y niñas
# de todo el país ya que podrían abrir paquetes ellos solos sin estar cerca de gente
# con la que intercambiar figuritas. Por lo tanto es vital que no se efectue este cambio.

"""Rta: No varían mucho las probabilidades ya que los paquetes tienen
una cantidad pequeña de figus"""

#Ejercicio 4.29
#Para que completen el albúm el array tienen que estar lleno de números <= 5, lo que
# sería equivalente a completar 5 álbumes

# Por suerte para vos está es la última edición de nombres de variables estúpidos

figus_paquete2 = 5
n_repeticiones3 = 1000
figus_total3 = 670  
amigos = 5
canti_figus3 = [cuantos_paquetes_no_repe(figus_total3, figus_paquete2, amigos) for albu in range(n_repeticiones3)]
prome3 = np.mean(canti_figus3) / amigos # Lo divido por amigos así se cuánto necesitan para cada albúm
print (f"En promedio hay que comprar {prome3} paquetes (sin repes) por álbum para ", end ="")
print (f" completar {amigos} albúm/es de {figus_total3} figus entre {amigos} amigos.")


