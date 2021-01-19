# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:16:56 2020

@author: Diego
"""
import csv
import gzip

# l = línea

#Ejercicio 6.4

#Filtro es el equivalente a select
def parse_csv(archivo, filtro=None, types=None, has_headers=True, silence_errors= True):
        archivo = csv.reader(archivo) #Convierto las líneas de texto a algo procesable
        if not has_headers and filtro:
            if not silence_errors:
                raise RuntimeError("Para seleccionar, necesito encabezados.")
        
        if has_headers:
            # Lee los encabezados
            headers = next(archivo)
            if filtro: #Si el filtro no está vacío
            # Crea un indíce y un nuevo encabezado si es necesario
                index = [headers.index(column_name) for column_name in filtro]
                headers = [ncolu for i,ncolu in enumerate(headers) if (i in index)]
        else:
            pass
        records = []
        for i,row in enumerate(archivo):
            if not row:    # Saltea filas sin datos
                continue
            
            if has_headers:
                if filtro: #Si el filtro no está vacío
                    row = [row[indi] for indi in index]    
                   
                if types: #Si los tipos de los datos no están vacíos
                    try :
                        row = [func(val) for func, val in zip(types, row) ]
                        
                    except Exception as e:
                        if not silence_errors:
                            print(f"No pude convertir {row}")
                            print(f"Row {i} Motivo: {e}")
                    
                record = dict(zip(headers, row))
                
            else:
                record = tuple(data for data in row) #Google ♥
            records.append(record)
        return records


#  Pinta que funca bien 

with gzip.open('Data/camion.csv.gz', 'rt') as file:
      camion = parse_csv(file, types=[str,int,float])

lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion = parse_csv(lines, types=[str,int,float])
