# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 01:04:27 2020

@author: Diego
"""
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


n=1000000
puntos = [generar_punto() for x in range(n)]
puntos_circulo =  [ (x,y) for x,y in puntos if (x**2+y**2 < 1) ]
pi = 4*len(puntos_circulo) / len(puntos)

