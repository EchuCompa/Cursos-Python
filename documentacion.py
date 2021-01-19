# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:25:12 2020

@author: Diego
"""
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    assert (int,int) == (type(desde), type(hasta)), "Tienen que ser números enteros"
    
    suma = 0
    if hasta<desde or desde == hasta:
        return suma
    for x in range(desde,hasta+1):
        suma = suma + x
    
    #Gracias Algebru, asumo que ambos son números positivos 
    # suma =  ( hasta*(hasta+1) - (desde+1)*desde ) /2
    return suma
    
def valor_absoluto(n):
    """ Recibe un número real y devuelve su valor absoluto"""
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):  
    """ Suma los elementos pares de una lista"""
    res = 0
    for e in l:
        if e % 2 ==0: 
            res += e
        else:
            res += 0
            
    return res

def veces(a, b):
    """ Suma "a" "b" veces. "b" debe ser un número entero positivo"""
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    """ Invariante de ciclo res= a*(b-nb) """
    return res


def collatz(n):
    res = 1
    """ Devuelve la cantidad de pasos que toma un número para llegar a 1 siguiendo 
    el algortimo de la conjetura de Collatz. "n" debe ser un número entero positivo"""
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    """ No se me ocurre cuál podría ser un invariante de ciclo si es que tiene"""
    return res