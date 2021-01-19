# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:58:54 2020

@author: Diego
"""
# numero_valido=False
# while not numero_valido:
#     try:
#         a = input('Ingresá un número entero: ')
#         n = int(a)
#         numero_valido = True
#     except:
#         print('No es válido. Intentá de nuevo.')
# print(f'Ingresaste {n}.')


#Ejercicio 2.4
# def saludar(nombre):
#     print(f"Hola {nombre}, tudu peola?")

# saludar("Juanchi")

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    elif type(edad) == str:
        raise ValueError ("Debe ingresar su edad en números")
    return edad

