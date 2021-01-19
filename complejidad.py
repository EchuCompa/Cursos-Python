# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:24:10 2020

@author: Diego
"""
from copy import copy 
# Ejercicio 5.13

def incrementar(s):
    carry = 1
    l=len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i]==1 and carry==1):
            s[i]=0
            carry=1
        else:
            s[i]=s[i]+carry
            carry=0
    return s

# Ejercicio 5.14
""" Pinta que es una función lineal ya que la cantidad de operaciones se ejecutan
una sola vez ante la longitud de la lista, y siempre se la revisa por completo. 
Por lo que su complejidad es lineal"""

# Ejercicio 5.15

def listar_secuencias(n):
    secuencias_bin = [[0]*n]
    for x in range((2**n)-1):
        anterior = copy(secuencias_bin[x])  # Hago una copia para que no se modifique 
        #                                     la secuencia anterior.                              
        secuencias_bin.append(incrementar(anterior))
    return secuencias_bin

j = listar_secuencias(3)


"""La función listar secuencias es una función exponencial, ya que la cantidad
de secuencias que tiene que formar es de 2^n"""