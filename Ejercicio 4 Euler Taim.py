# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math
import random

""" Euler Ejercicio Número 1 """
# def collatz(n):
#     count = 1
#     while n != 1:
#         if n%2 == 0 : 
#             n = n/2
#         else:
#             n = 3*n + 1
#         count += 1
#     return count

# s = collatz(13)
# resultados = []
# for j in range(1, 1000000):
#     resultados.append(collatz(j))
#     if j %1000 == 0:
#         print ("Ya va por el ", j/10000, "%")
    
# valor_máximo = max(resultados)
# número_máximo = resultados.index(max(resultados))

""" Euler Ejercicio Número 2 """

# es múltiplo


def factores(n):
    facts = []
    for k in range(2,n):
        if n % k == 0 :
            facts.append(k)
    return facts
     
def es_primo(n):
    primo = True
    k= 1
    while primo == True and k<n-1:
        k += 1
        if n % k == 0 :
           primo = False
    return primo

def factorizar(n, p):
    nume = n
    while nume % p == 0:
        nume /= p
    return nume
    
def factores_primos(n):
    facto_primos = []
    j = 2
    while n != 1:
        if es_primo(j) and n%j == 0:
            n = factorizar(n, j)
            facto_primos.append(j)
        j += 1
    return facto_primos
        
  
    
aver = factores_primos(423819572348)