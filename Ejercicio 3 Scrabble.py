# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def extraer_palas(texto):
    palabras = []
    pala = []
#    completo = int(len(texto)/10)
    for i in range(len(texto)):
        x = texto[i]
        t = ord(texto[i])
        if t< 251 and t>64 :
            pala.append(x)
        elif len(pala)> 0:
            yes = ("".join(pala)).lower()
            palabras.append(yes)
            pala = []
#        if i % completo == 0:
#            print(i / completo*10, "% completado")
    return palabras

def valor_pala(pala):
    valor = 0    
    for j in range(len(pala)):
            z = pala[j]
            if z in ['e','a', 'i', 'n', 'r', 't','o', 'l','u']:
                valor += 1
            if z in [ 'd',  'g']:
                valor += 2
            if z in ['b','c','m','p']:
                valor +=3
            if z in ['f','h','v','w','y']:
                valor += 4
            if z in ["k"]:
                valor +=5
            if z in ['j','x', 'ñ']:
                valor +=8
            if z in ['q','z']:
                valor +=10
    return valor

        
def crear_letras(dicciona, cant_letras): #Devuleve las letras que tiene que usar y todas lasp posibles palabras. 
    letras = []
    posibles = ['e','a', 'i', 'n', 'r', 't','o', 'l','u', 'd',  'g', 'b','c','m','p', 'f','h','v','w','y','k', 'j','x','ñ', 'q','z'] 
    for j in range(len(posibles)):
        if j<9:
            t = 18
        elif j<11:
            t = 12
        elif j<15:
            t = 6
        elif j<20:
            t = 4
        elif j<21:
            t = 4
        elif j<24:
            t = 2
        elif j<26:
            t = 2
        for i in range(t):
            letras.append(posibles[j])
    #Ahora elijo 7 letras random
    go=True
    while go== True:
        random.shuffle(letras)
        letris= []
        for i in range(cant_letras):
           letris.append(letras[i])
        pala= formar_palabras(dicciona, letris)
        if len(pala) > 0:
            letras.append(letris)
            letras.append(pala)
            go=False
    return [letras[-1], letras[-2]]

def formar_palabras(dixio, letters): #Te devuelve todas las palabras posibles
    palabras = []
    for i in range(len(dixio)):
        count = 0
        word = []
        for z in range(len(letters)):
            word.append(letters[z])
        for j in range(len(dixio[i])):
            if dixio[i][j] in word and len(word)>0:
                count += 1
                word.pop(word.index(dixio[i][j])) #Esto es para que no usen más letras de las posibles
        if count == len(dixio[i]):
            palabras.append(dixio[i])
    return palabras
            

def proceso_creacion(diccio):   
    lista_palas = extraer_palas(diccio)
    return lista_palas

def mayor_puntaje(palabras):
    valores = []
    holus = 0
    for x in range(len(palabras)):
        valores.append(valor_pala(palabras[x]))
    if len(palabras)>0 :
        holus = palabras[valores.index(max(valores))]
    return holus

def mas_larga(palabras):
    valores = []
    holus = 0
    for x in range(len(palabras)):
        valores.append(len(palabras[x]))
    if len(palabras)>0 :
        holus = palabras[valores.index(max(valores))]
    return holus

def calcular_frecuencias(lis, tipo_fre):
    frecue = []
    count=1
    if tipo_fre == "larga":
        while count<10:
            words = 0
            for i in lis:
                if i == count:
                    words += 1
            count += 1
            frecue.append(words)
    elif tipo_fre == "puntaje":
        while count<40:    
            words = 0
            for j in lis:
                if j == count:
                    words += 1
            count += 1
            frecue.append(words)
    return frecue
        
    

def juego(tipo_pala, n_rep): 
    diccionario = open('diccionario.txt').read()
    dixio = proceso_creacion(diccionario)
    listado_palas = []
    for j in range(n_rep):
        letras_palabras = crear_letras(dixio, 9)
        if tipo_pala == "puntaje":   
            pala1 = valor_pala(mayor_puntaje(letras_palabras[0]))
        elif tipo_pala== "larga":
            pala1 = len(mas_larga(letras_palabras[0]))
        listado_palas.append(pala1)
    freq = calcular_frecuencias(listado_palas, tipo_pala)
    valores = []
    for n in range(len(freq)):
        valores.append(n)
    print(freq)
    plt.bar(valores, freq)
    plt.show()
    
            
    
    
juego("larga", 100)


