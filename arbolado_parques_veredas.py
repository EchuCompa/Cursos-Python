# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:33:15 2020

@author: Diego
"""

import pandas as pd
import os
import seaborn as sns

directorio = 'Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

# #df = Data Frame

# archivo = 'arbolado-en-espacios-verdes.csv' #BOBOOOOOOOO

# columnas = df.columns #Lista con cada columna
# datos_df = df.describe() #Un df de los datos de cada una de las columnas


# #Extraigo las columnas con las que quiero trabajar del Df
# cols_sel = ['nombre_cientifico',  'diametro_altura_pecho', 'altura_arbol', 'ancho_acera',]
# cols = ["diametro", "altura_tot", "nombre_cie" ] #Ni idea a que se refiere con ancho_acera
# df_lineal = df[cols].copy()

# #Renombro las columnas para que tengan el mismo nombre que me piden
# df_lineal = df_lineal.rename(columns={ 'diametro' : cols_sel[1],  "altura_tot": cols_sel[2],  "nombre_cie"  : cols_sel[0] } ) 

# #Selecciono las especies y cambio los nombres de la lista porque estaban mal tipeados
# especies_seleccionadas = ['Tilia viridis subsp. x moltkei', 'Jacarandá mimosifolia', 'Tipuana Tipu']
# df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]



#Hecho con el archivo correcto

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal = df[cols_sel].copy()
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel[:-1]], hue = 'nombre_cientifico')