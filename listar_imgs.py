# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:52:48 2020

@author: Diego
"""
import os
import datetime

# Ejercicio 7.5

# dire = os.path.join("c:\\", 'Users', 'Diego', 'Documents', "Echu")

def listar_imgs(dire):
    for root, dirs, files in os.walk(dire):
       for name in files:
          # print(os.path.join(root, name)) Le agrega el path del archivo
          
          if name[-3:] == "png": #Chequea la extensión del archivo 
              print(name)
              
       # for name in dirs: Acá listaría los directorios si quisiera
       #    # print(os.path.join(root, name))

          
def main(argv):
    if len(argv) != 1: 
        raise SystemExit(f'Uso adecuado: {argv[0]} c:\\Users')
    print("Estos son los pngs de su directorio: \n")
    listar_imgs(argv)
    return 0
    
# if __name__ == '__main__':
#     import sys
#     main(sys.argv)
    
#Ejercicio 7.6

def procesamiento_archivo(directorio):
    for root, dirs, files in os.walk(directorio): #camino por el directorio
        for file in files:
            if file.endswith('.png'): #encuentro un archivo ".png"
                fecha = file[-12:-4] #delimito la fecha
                print(file , " \n \n  \n \n ")
                fecha_acceso = datetime.datetime(year = int(fecha[0:4]), month =int(fecha[4:6]), 
                                                 day = int(fecha[6:8]))        
                fecha_modif = datetime.datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), 
                                                day = int(fecha[6:8])) 
                ts_acceso = fecha_acceso.timestamp() #modifico fecha de acceso
                ts_modif = fecha_modif.timestamp() #y de última modificación
                direc = os.path.join(root, file) # le agrego el path a la dirección
                os.utime(direc, (ts_acceso, ts_modif)) # en el archivo
                os.rename(direc, direc[:-13]) #cambio el nombre 
                
    return os.listdir(directorio)
    

#Cómo cambiar la fecha de modificacion un archivo

import time

camino = './hipoteca.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))


# directorio = 'Documents'
# procesamiento_archivo(directorio)