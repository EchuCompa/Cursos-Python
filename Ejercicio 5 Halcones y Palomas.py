# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:19:42 2020

@author: Diego
"""
import random
import matplotlib.pyplot as plt

def creacion(n_palomas,n_halcones, n_fuentes):    
    pobla = [] #Acá se crea la cantidad de palomas que va a haber
    for j in range(n_palomas):
        pobla.append("p")
    for h in range(n_halcones):
        pobla.append("h")
    
    fuentes = [] #Acá se crea la cantidad de fuentes que va a haber
    for f in range(n_fuentes):
        fuentes.extend([f,f])
    random.shuffle(fuentes)
    return[pobla,fuentes]


def comen(pobla,fuentes)    :
    comen = [] #Acá se distribuye cada paloma a su respectiva fuente
    for d in range(len(pobla)):
        if d >= len(fuentes):
            comen.append(0)
        else:
            comen.append(fuentes[d])
    return comen
    

def alimentar(comen,pobla,p):
    comieron = [-1 for x in range(len(pobla))]
    if len(comen) <= len(set(comen)): #Acá compruebo si hay más de dos animales en una fuente
        "No pasa nada"
    else:
        for count,ave in enumerate(comen): #Acá se distribuye la comida
            if comen.count(ave) == 2 and comieron[count]==-1:
                indice_cumpa = comen.index(ave, count+1, len(comen))
                cumpa,habita = pobla[indice_cumpa], pobla[count]
                print(cumpa, habita)
                if (cumpa, habita) == ("p","p" ):
                    comieron[count] = 1
                    comieron[indice_cumpa] = 1
                elif (cumpa, habita) == ("p","h" ):
                    comieron[count] = 2-p
                    comieron[indice_cumpa] = p
                elif (cumpa, habita) == ("h","p" ):
                    comieron[count] = p
                    comieron[indice_cumpa] = 2-p
                else:
                    comieron[count] = 0
                    comieron[indice_cumpa] = 0
                # print("Cumpa", comieron[indice_cumpa], "Habita:", comieron[count])
            elif ave == 0:
                comieron[count] = 0
            else:
                comieron[count] = 2
    return comieron

def balance(pobla, alime,p): #Acá pasa la magia, se mueren quienes no comen, sobreviven los que si y se reproducen los que comieron dos
    count= 0
    s=0 
    for a in alime:
        if a == 0:
            del pobla[count]
            # print("murio2",pobla[count])
            count -= 1
        elif a==p:
             if 1-p<random.random():
                  del pobla[count]    
                  count -= 1
                  # print("murió2")
        elif a==2-p:
             if 1-p>random.random():
                  pobla.append(pobla[count])  
                  # print("Vivió2")  
        elif a == 1:
            "No pasa nada"
        elif a ==2:
            pobla.append(pobla[count])
        elif a == -1:
            s += 1
            count -= 1
            del pobla[count]
        count += 1
    print("No alcanzo", s, "veces")
    return pobla

def evolucion(n_palomas, n_halcones, n_fuentes, n_dias, p):
    comienzo = creacion(n_palomas,n_halcones, n_fuentes) 
    pobla,fuentes = comienzo[0],comienzo[1]
    halcones = []
    palomas = []
    for j in range(n_dias):
        distri_comida = comen(pobla,fuentes) 
        alimento = alimentar(distri_comida,pobla,p)
        pobla = balance(pobla, alimento,p)
        halcones.append(pobla.count("h"))
        palomas.append(pobla.count("p"))
    plt.plot(palomas, halcones, label=("El valor de p es", p))
    plt.xlabel("Palomas")
    plt.ylabel("Halcones")
    plt.title("Relación entre población de palomas y halcones")
    plt.legend(loc="lower left")
    print(halcones, palomas)
    
evolucion(100,50,80,10, 0.2)
        

        
            
    