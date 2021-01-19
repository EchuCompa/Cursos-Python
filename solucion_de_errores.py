# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         print(expresion[i])
#         if expresion[i] == 'a' or expresion[i] == 'A' :
#             return True
#              # Acá al tener un "return False" la función meramente evaluaba la primer posición.
#              # Por lo que era inecesario tener una condición "else". 
#         i += 1
#     return False 

#a= tiene_a('UNSAM 2020')
#r= tiene_a('abracadabra')
#i= tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. 
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i].lower() == 'a': #Cambie el "=" a "==" para comparar y no asignar. 
#                                         # además le agregue un lower para comparar la "A" mayuscula.
#             return True
#         i += 1
#     return False #El código decía "Falso" en vez de "False".

#e= tiene_a('UNSAM 2020')
#l= tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. 
# def tiene_uno(expresion1):
#      expresion1 = str(expresion) #Esta es otra solución alternativa al problema 
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene


# r=tiene_uno('UNSAM 2020')
# o=tiene_uno('La novela 1984 de George Orwell')
# j= tiene_uno("1984") #El error es que el tipo de datos ingresado era un "int" no un "string", cómo lo que requiere la función
# a = "Mira cómo pienso en .."
# s = ".. mi corrector"
#%%
#Ejercicio 3.4
# def suma(a,b):
#     c = a + b
#     return c # la función no devuelve nada, por lo que hay que agregarle un return c
    
# c = 0
# a = 2
# b = 3
# c= suma(a,b)
# print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5
# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             print(camion)
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#             registro = {} #El problema es que no se estaba vaciando el registro, por lo que
#             #asumo que se modificaba el registro dentro de camion también.
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)




