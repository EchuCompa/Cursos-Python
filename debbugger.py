# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
"""Debugger = Depurar
    Ctrl + F5 = Empezar debbuger
    Ctrl + F10 = Avanzar un paso
    Ctrl + F11 = Meterse dentro de la función
    Ctrl + Shift + F11 = Salir de la función """


#Ejercicio 4.1

# def invertir_lista(lista):
#     '''Recibe una lista L y la develve invertida.'''
#     invertida = []
#     i=len(lista)
#     while i > 0:    # tomo el último elemento 
#         i=i-1
#         invertida.append (lista.pop(i))  #Acá es donde se modifica la función
#         invertida.append(lista[i]) #Está seriá una posible solución al problema.
#     return invertida

# l = [1, 2, 3, 4, 5]    
# m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')


#Ejercicio 4.2

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#             # registro = {} # Con esto se soluciona
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

# ----------------------------------------------------------------------------------------

# Ejercicio 4.3

# def propagar_al_vecino(l):
#     modif = False
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1]==0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i>0 and l[i-1]==0:
#             l[i-1] = 1
#             modif = True
#     return modif

# def propagar(l):
#     m = l.copy()
#     veces=0
#     while propagar_al_vecino(l):
#         veces += 1

#     print(f"Repetí {veces} veces la función propagar_al_vecino.")
#     print(f"Con input {l}")    
#     print(f"Y obtuve  {m}")
#     return m


# propagar([0,0,0,0,1])
# propagar([0,0,1,0,0])
# propagar([1,0,0,0,0])

"""Preguntas 
1) Porque revisa si está en el último o primer elemento respectivamente
2) Por cómo avanza la función, ya que la misma va de derecha a izquierda.
3) a) Se puede repetir n-1 veces. b) (2n -2) operaciones c) (n-1) *(2n-2), osea es cuadratico.
    """
# ----------------------------------------------------------------------------------------
# Ejercicio 4.4
    
# def propagar_a_derecha(l):
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1:
#             if l[i+1]==0:
#                 l[i+1] = 1
#     return l
# #%
# def propagar_a_izquierda(l):
#     return propagar_a_derecha(l[::-1])[::-1]
# #%
# def propagar(l):
#     l1 = l.copy() # Modificación punto 3.
#     ld=propagar_a_derecha(l1)
#     lp = propagar_a_izquierda(ld)
#     return lp

# l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
# print("Estado original:  ",l)
# print("Propagando...")
# lp=propagar(l)
# print("Estado original:  ",l)
# print("Estado propagado: ",lp)

"""Preguntas
1) Porque en ningún momento se hizo una copia por lo tanto las modificaciones fueron sobre la original
2) Porque sólo se propago de izquierda a derecha, luego la función izquierda si obtuvo una "nueva lista".
3) Línea 101
4) Hace n-1 operaciones
5) Efectua 2*(n-1) + n operaciones.
    """
# ----------------------------------------------------------------------------------------
# Ejercicio 4.5
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)  #En vez de "" hay que poner "x"
    if debug:
        print(ps)
    return trad2l(ps)

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)


"""Preguntas
1) Se acorta la lista (quitando las x), porque primero las usa cómo método de separación
    en la línea 144, pero luego en la 146 junta los distintos caracteres sin la x.
2) Línea 146
3) Es un algoritmo lineal
"""
    """