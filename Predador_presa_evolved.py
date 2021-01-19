import random
import numpy as np

lista_leo= []   #Listas con las posiciones de los antilopes y los leones
lista_anti = []
lista_coito = [] #Lista pa que los leones no se pasen de vivos. 
comida = [] #Lista que define cuándo un león se muere de hambre
leones = 3
def revisar_lista(lis, ele): 
    esta = False
    for i in range(len(lis)):
        if lis[i]== ele:
            esta = i
    return esta

def calcula_delta(x1, x2):
    distan= abs(x1-x2)
    return distan

def calcula_distancia(p1, p2):
    distancia = np.sqrt(calcula_delta(p1[0], p2[0])**2+calcula_delta(p1[1], p2[1])**2)
    return distancia

def ver_mas(lista, coord, opci): #opci define si va a buscar el que esta mas cerca o el que esta mas lejos
    dista = []
    for i in range(len(lista)):
        dista.append(calcula_distancia(lista[i], coord))
    for j in range(len(dista)):
        if opci==0:
            if dista[j]==min(dista):
               pu= j
        else:
           if dista[j]==max(dista):
               pu= j
    punto = lista[pu]
    return punto
    
def lista_posiciones(tablero):              
    for i in range(1, tablero.shape[0]): 
        for j in range(1, tablero.shape[1]):
            if tablero[(i,j)]== "L" and len(lista_leo)<leones: #Para que solo se ejecute la primera vez
                lista_leo.append((i,j))
                lista_coito.append(0)
            elif tablero[(i,j)]== "A":
                lista_anti.append((i,j))

def generar_tablero_azar(filas, columnas, n_antilopes, n_leones ) :
    tab = np.repeat(" ",(filas+2) *(columnas+2)).reshape(filas+2, columnas+2)
    tab1 = np.repeat(" ",(filas+2) *(columnas+2)).reshape(filas+2, columnas+2)
    tab[0] = "M"
    tab[filas+1] = "M"
    for i in range(0, filas+1, 1 ):
        tab[(i,0)] = "M"
        tab[(i,columnas+1)] = "M"
    posi = mezclar_celdas(tab1)
    ani= []
    for z in range(n_antilopes):
        ani.append("A")
    for j in range(n_leones):
        ani.append("L")
    for k in range(len(ani)):
        tab[posi.pop(0)]= ani.pop(0)
    lista_posiciones(tab)
    return tab

def es_borde(tablero, coord) :
    return tablero[coord] == "M"

def vecinos_de(tablero, coord) :
    veci = []
    f= coord[0]
    c= coord[1]
    veci.append((f-1,c-1))
    veci.append((f-1,c))
    veci.append((f-1,c+1))
    veci.append((f,c+1))
    veci.append((f+1,c+1))
    veci.append((f+1,c))
    veci.append((f+1,c-1))
    veci.append((f,c-1))
    i = 0
    veci2 = []
    while i<len(veci) :
        if not es_borde(tablero, veci[i]):
            veci2.append(veci[i])
        i = i+1 
#    random.shuffle(veci2) De esta forma se cumple el optativo 14 técnicamente
    return veci2

def buscar_adyacente(tablero, coord, objetivo, moti):
    i = 0
    veci = vecinos_de(tablero, coord)
    co = []
    co1 = []
    while i<len(veci):
        ver = veci[i]
        if tablero[(ver)]== objetivo:
                co.append(veci[i])
#        print(co)
        i = i+1
    if moti== "Preda" and co != []:
        co2 = ver_mas(lista_anti, coord, 0)
        co1 = ver_mas(co, co2, 0)   
    elif moti == "Presa" and co != []:
        co2 = ver_mas(lista_leo, coord, 0)
        co1 = ver_mas(co, co2, 1)
    elif co != []:
        co1= co[0]  
    return co1

def alimentar(tablero):
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):        
            if tablero[(i,j)] == "L" :
                        comida = buscar_adyacente(tablero, (i,j), "A", 2) 
                        if comida != [] :
                            if tablero[comida] == "A" :
                                tablero[(i,j)] = " "
                                tablero[comida] = "L" 
    return tablero

def reproducir(tablero):
    #Primero se van a reproducir los antilopes
    i = 0
    while i<len(lista_anti):
        punt = lista_anti[i]  
        hayamor =  buscar_adyacente(tablero, punt, "A" , "Presa")
        if hayamor != [] :
            print("repro")
            lista_anti.pop(revisar_lista(lista_anti, hayamor))
            futu_cria =  buscar_adyacente(tablero, punt, " ", "Presa")
            if futu_cria != [] :
                tablero[futu_cria] = "A"
                print("repro1")
        i = i +1
    lista_posiciones(tablero) #Para introducir los nuevos antilopes
    #Luego se van a reproducir los leones, de los cuales ninguno se va a reproducir dos veces.
    j=0
    while j<len(lista_leo) :
        punt2 = lista_leo[i]
        lista_coito[i] = 1
        hayamor2 =  buscar_adyacente(tablero, punt2, "A" , "Presa")
        if hayamor2 != [] and lista_coito[revisar_lista(lista_leo, hayamor2)] == 0:
            lista_coito[revisar_lista(lista_leo, hayamor2)] = 1
            futu_cria =  buscar_adyacente(tablero, punt2 , " ", "Presa")
            if futu_cria != [] :
                print("repro")
                tablero[futu_cria] = "A"
                lista_leo.append(futu_cria)
                lista_coito.append(0)
                comida.append(0)
        j = j + 1
    for n in range(len(lista_coito)) : #Para que se puedan reproducir de vuelta
        lista_coito[n] = 0        
    return tablero

def mover(tablero):
    #Primero se van a mover los antilopes
    for i in range(len(lista_anti)) :
            posi = lista_anti[i]
            movi = buscar_adyacente(tablero, posi, " ", "Presa")
            if movi != [] :
                tablero[(posi)] = " "
                tablero[(movi)] = "A"        
    #Luego se van a mover los leones, así tienen más oportunidades de atraparlos, sorry soy carnivoro
    for j in range(len(lista_leo)) :
            posi2 = lista_leo[j]    
            movi2 = buscar_adyacente(tablero, posi2, " ", "Preda")
            if movi != [] :
                tablero[(posi2)] = " "
                tablero[(movi2)] = "L"
    return tablero

def evolucionar(tablero) :
    tab1 = alimentar(tablero)
    tab2 = reproducir(tab1)
    tab3 = mover(tab2)
    return tab3

def evolucionar_tiempo(tablero, k) :
    tab = tablero
    for i in range(k):
        evolucionar(tab)
    return tab

def mezclar_celdas(tablero):
    celdas = []
    for i in range (1 , tablero.shape[0]-1, 1) :
            for j in range (1 , tablero.shape[1]-1, 1) :
                    celdas.append((i, j))
    random.shuffle(celdas)
    return celdas

def cuantos_cada(tablero):
    ani = [0,0]
    for i in range(1, tablero.shape[0]-1): 
        for j in range(1, tablero.shape[1]-1):
            if tablero[(i,j)] == "A" :
                ani[0] = ani[0] +1
            if tablero[(i,j)] == "L" :
                ani[1] = ani[1] +1
    return ani

def registrar_evolucion(tablero, k):
    tab = tablero
    print(tab)
    anim = []
    anim.append(cuantos_cada(tab))
    for i in range(k):
        evolucionar(tab)
        anim.append(cuantos_cada(tab))
        print(tab)
    return anim

tab1 = generar_tablero_azar(15, 9, 2, leones)
resu = registrar_evolucion(tab1, 3)                

