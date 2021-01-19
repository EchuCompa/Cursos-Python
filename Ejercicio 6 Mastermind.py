# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:02:55 2020

@author: Diego
"""
import random

def contar_con_ubicacion_sinrep(a,b):
    coinci = 0
    for count,x in enumerate(a):
        if x == b[count]:
            coinci += 1
    return coinci

def contar_mal_ubicadas_sinrep(a,b):
    coinci = 0
    repe = {}
    for t in set(b): #Esto es para que no cuente coincidencias demás. 
        repe[t] = b.count(t)
    for x in a:
        if x in b and  repe[x]!=0:
           coinci += 1
           repe[x] -= 1
    return coinci

def contar_coincidencias_sinrep(a,b):
    s = contar_con_ubicacion_sinrep(a,b)        
    g = contar_mal_ubicadas_sinrep(a,b)
    return [s, g-s]

def jugar_sinrep():
    intentos = 0
    gano = False
    cifras = int(input("Ingrese el número de cifras que desea que tenga el número que inten\
tara adivinar: \n>>>"))
    b = [str(random.randint(0,9)) for x in range(cifras)]
    if cifras>0:
        while not gano:
            intentos += 1
            a = list(input("Ingrese el número que cree que es: \n>>>"))
            t = contar_coincidencias_sinrep(a,b)
            if t[0] == len(b):
                gano= True
                print("Adivinaste master, el número era", "".join(b), "y lo adivinaste en sólo", intentos, "intentos, un animal.")
            elif len(a) == len(b):
                print("Tenes ", t[0], "dígitos que están bien ubicados y", t[1], "números que están en el original")
            else:
                print("El número de cifras del número a adivinar es ", len(b), "y usted \n \
ingreso un número de ", len(a), "cifras, porfavor intente de vuelta")
            
jugar_sinrep()
    

