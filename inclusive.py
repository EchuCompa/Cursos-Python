# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:33:57 2020

@author: Diego
"""
frase = "Todos, tu también'"
palabras = frase.split(" ")

for p in palabras:
    posi_p = palabras.index(p)
    if p[-1] == "o":
# Lo que hace es agarrar toda la palabra excepto la última letra y luego la sustituye
        p = p[:-1] + "e"
    elif  len(p)>1 and p[-2] == "o":
# El mismo proceso sólo que separa la palabra en 2. 
        p = p[:-2] + "e" + p[-1]
    elif ord(p[-1]) in [44,46]:
        if p[-3] == "o":
            p = p[:-3] + "e"
    palabras[posi_p] = p
    

frase_inclu = " ".join(palabras)