# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:13:32 2020

@author: Diego
"""

import random
import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 5.11 + 5.16

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0 # Comparaciones, 5.16
    while izq <= der and pos == -1:
        medio = (izq + der) // 2
        comps += 2 # Por que hace dos comparaciones sobre x
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d} = {lista[medio]}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado! 
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            
    if pos == -1:   # Si no lo encontro entonces es mayor o menor que el medio
        if lista[medio] < x:
            pos = medio + 1
        else:
            pos = medio 
    return (pos, comps)

# Ejercicio 5.12

def insertar(l,e):
    posi,comps = donde_insertar(l, e)
    if not (l[posi] == e): # Si el elemento no está en la lista 
                           # también podría usar "in", pero medio trampa
        l.insert(posi, e)
    return posi 

# li = [1,2,3,4,5,7,8,9,10]
# j = insertar(li, 6)

# Comprobando 5.16

# mi = list(range(1000))
# t = donde_insertar( mi, 50)


def busqueda_secuencial_(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 #sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps

def generar_lista(n,m):
    l = random.sample(range(m),k=n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0,m-1)

m = 10000 # 1 a m = rango de elementos de la lista
n = 100 # Elementos de la listas
k = 1000 #Cantidad de comparaciones promedio

def experimento_secuencial_promedio(lista,m,k):
    comps_tot = 0
    for i in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,e)[1]

    comps_prom = comps_tot / k
    return comps_prom



largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n,m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista,m,k)

#ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.figure()
plt.plot(largos,comps_promedio,label='Búsqueda Secuencial')
# plt.xlabel("Largo de la lista")
# plt.ylabel("Cantidad de comparaiciones")
# plt.title("Complejidad de la Búsqueda")





def experimento_binario_promedio(lista,m,k):
    comps_tot = 0
    for i in range(k):
        e = generar_elemento(m)
        comps_tot += donde_insertar(lista,e)[1]
    comps_prom = comps_tot / k
    return comps_prom

comps_promedio_bin = np.zeros(256)

for i, n in enumerate(largos):
    lista1 = generar_lista(n,m) # genero lista de largo n
    comps_promedio_bin[i] = experimento_binario_promedio(lista1,m,k)

#ahora grafico largos de listas contra operaciones promedio de búsqueda.

plt.plot(largos,comps_promedio_bin,label='Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()


"""Pareciera que la complejidad de la búsqueda binaria es mucho menor que la búsqueda
secuencial """

# De bonus dejo cómo hacer un proceso de búsqueda binaria del 1 a 100 en C++.
# Por si te queres pasar a Compu Ari, siempre es un buen momento
"""
    /* int v1 =50; //Comparison number
    int increment = 50; 
    char answer='y';
    cout << "Yes = y , No = n, You guessed it! = g \n";
    cout << "Is your number bigger than " << v1 << " ? : \n";
    while (cin>>answer && answer != 'g') {
        switch (answer) {
        case 'y':
            increment /= 2;
            v1 += increment;
            break;
        case 'n':
            increment /= 2;
            v1 -= increment;
            break;
        default :
            cout << "That´s not a valid answer. \n";
            break;
        }
        cout << "Is your number bigger than " << v1 << " ? : \n";
        if (increment <= 1) increment=2; // So it doesn´t stop, jejox.
        }
    cout << "Your number is " << v1 << "\n";*/
"""