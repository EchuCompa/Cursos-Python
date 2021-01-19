# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:56:11 2020

@author: Diego
"""
#Dudas que me quedaron
#¿Cómo hago para hacer una comparación múltiple en un if statement? Por ejemplo, quiero saber si x1, x2, x3…..xn  son mayores a 0. Pero no quiero poner: x1> 0 and x2 > 0, ……. xn > 0, la pregunta es si hay una forma más “elegante”. Algo como (x1,x2,x3, …. xn) >0 si es que se puede. 
#¿Cómo hago para que al introducir dos líneas con una escala mucho más grande que la otra no me quede una mucho más pequeña? Ergo, como “agrando” la más pequeña para poder ver sus resultados también. 



import random
import numpy as np
import matplotlib.pyplot as plt

def jugada(p):
    return random.random()<p

def partida(j, m , p):
    mone_j = j
    mone_c = m-j
    count = 0
    while mone_j>0 and mone_c>0 :
        if jugada(p):
            mone_j += 1
            mone_c -= 1
        else:
            mone_j -= 1
            mone_c += 1
        count += 1
    return [mone_c > 0, count]
            
            
def repeti(n_rep, saltos_p,  r):
    valores_m = [10, 20, 30, 50]
    for m in range(len(valores_m)):
        valores_j = np.arange(0, valores_m[m],2)
        valores_p = [1/6, 1/2, 4/5]
        for p in range(len(valores_p)):
            prome_wins = []
            prome_dura = []
            for j in range(len(valores_j)):
                tiradas = []
                duracion = []
                for i in range(n_rep):
                    z= partida(valores_j[j], valores_m[m], valores_p[p])
                    tiradas.append(z[0])
                    duracion.append(z[1])
                prome_wins.append(tiradas.count(False)/len(tiradas))
                prome_dura.append(sum(duracion)/len(duracion))
            plt.figure()
            plt.plot(valores_j, prome_wins, "blue", label= "Con valor  P= " + str(valores_p[p]))
            plt.plot(prome_dura, prome_wins, "red")
            plt.xlabel("Valor J= Azul y Duracion = Rojo" , color="green")
            plt.ylabel("Promedio de Victorias", color = "cyan")
            plt.title(("Con valor  P= ", valores_p[p] ,"y valor M= ",valores_m[m] ) , color= "orange")
            plt.legend(loc="lower left")
            plt.show()   
    return prome_wins
    
ho = repeti(100, 0.5 , 30) 