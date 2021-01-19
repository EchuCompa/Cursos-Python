# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:39:51 2020

@author: Diego
"""
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

#Primeros ejercicios

"""
Código pa la terminal

import html2text
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto = converter.handle(response.css('*').get())
f = open("Documents/Echu/Programacion/Exactas_programa/novela.txt", "w", encoding="utf-8")
f.write(texto)
f.close
"""


texto1 = """Sherlock Holmes is a fictional private detective created by British 
author Sir Arthur Conan Doyle. Referring to himself as a consulting detective 
in the stories, Holmes is known for his proficiency with observation, deduction, 
forensic science, and logical reasoning that borders on the fantastic, which he 
employs when investigating cases for a wide variety of clients, including 
Scotland Yard."""


#Ejercicio 4

def separar_texto(texto):
    lista_pala = texto.split(" ")
    for i,pala in enumerate(lista_pala): #Saco los puntos y comas de las palabras.
        if len(pala)>=1:
            if pala[-1] in [".", ",", ":"]:
                lista_pala[i] = pala[:-1] 
            lista_pala[i] = (pala.strip()).lower()
    # Hago esto para quitar los espacios en blanco
    palabras = [x for x in lista_pala if len(x)>0]
    return palabras

#Ejercicio 5

def generar_diq(texto):
    diccio = {}
    for pala in texto:
        if pala not in diccio.keys():
            diccio[pala] = 1
        else:
            diccio[pala] += 1
    return diccio

nueva_data = separar_texto(texto1)
diq = generar_diq(nueva_data)
palabras = pd.DataFrame.from_dict({"Frecuencia": diq})

#Ejercicio 6

# sns.barplot( x=palabras.index , y=palabras["Frecuencia"], errwidth=100)
# plt.xticks(rotation="90")

#Ejercicio 7

# wordcloud = WordCloud(width=480, height=480, margin=0)
# wordcloud.generate_from_frequencies(diq)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.margins(x=0, y=0)
# plt.show()

# Ejercicio 8

def generar_dic_fil(texto, palabras_filtro, n):
    palas = []
    frec = []
    for pala in texto:
            if pala not in palas:
                palas.append(pala)
                frec.append(1)
            else:
                frec[palas.index(pala)] += 1
    if n<= 0:
        n = len(palas)  - len(palabras_filtro)
    diccio = {}
    i= 0
    while i<n:
        # Agrego al diccionario la palabra con mayor frecuencia de la lista.
        indi_frec  = frec.index(max(frec))
        frecu = frec.pop(indi_frec)
        pala = palas.pop(indi_frec)
        if pala not in palabras_filtro and len(pala)>3:
            diccio[pala] = frecu 
            i += 1
    return diccio

#Ejercicio 9

def histo_wordcloud(texto, palabras_filtro, nom_cloud):
    new_data = separar_texto(texto)
    frec_pals = generar_dic_fil(new_data, palabras_filtro, 20)
    palabras = pd.DataFrame.from_dict({"Frecuencia": frec_pals})
    # Histograma.
    sns.barplot( x=palabras.index , y=palabras["Frecuencia"], errwidth=100)
    plt.xticks(rotation="90")
    plt.show()
    
    wordcloud = WordCloud(width=480, height=480, margin=0)
    wordcloud.generate_from_frequencies(frec_pals)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig(nom_cloud) #Esto es para guardar la wordcloud. 
    plt.show()
    



# filtro_a_manopla = ["the", "a", "*", "=", "their", "OR", "other", "this", "they", "from", "by", "have", "be", "are", "were", "on", "or", "The", "had", "not", "of", "that", "it", "and", "to", "with", "with", "is", "as", "at", "I", "in", "he", "yoy", "she", "was", "which", "for"]    
# # with open("Doyle.txt", "rt", encoding="utf8") as f1:
# #     t = f1.read()
# #     histo_wordcloud(t, filtro)

# #Ejercicio 10

# with open("common_words.txt", "rt", encoding="utf8") as f2:
#     r = f2.read()
#     filtro = r.split("\n")
#     filtro.extend(["*", "="])
# #Es un archivo que encontre por Internet con las más 1000 palabras más frecuentes, copa3.

# with open("estudios_falsos.txt", "rt", encoding="utf8") as f:
#     t = f.read()
#     histo_wordcloud(t, filtro, "no_me_importa")





