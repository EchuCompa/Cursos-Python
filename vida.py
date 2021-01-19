# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from datetime import datetime
from datetime import timedelta

#7.1
    
def segundos_vividos(fecha): 
    nacimiento = datetime.strptime(fecha, '%d/%m/%Y')
    actualidad = datetime.now()
    tiempo_vivido = actualidad - nacimiento
    return tiempo_vivido.total_seconds()


#7.2
#Asumo que la primavera empieza el 22 septiembre.

def cronica_pasion():
    actualidad = datetime.now()
    primavera = datetime(year = actualidad.year , month = 9, day = 22)
    tiempo_faltante = (primavera - actualidad).days % 365
    print(f"Faltan {tiempo_faltante} días para darsela en la pera")
    


#7.3

licencia = datetime(2020, 9, 26) 
duracion = timedelta(days = 200)
dia_finalizacion = licencia + duracion

#7.4

def dias_habiles(inicio, fin, feriados):
    dias_habi = 0
    fecha_actual = datetime.strptime(inicio, '%d/%m/%Y')
    final = datetime.strptime(fin, '%d/%m/%Y')
    while (final -fecha_actual > timedelta(days = 0) ): # Mientras no te pases del final
        chequeo = fecha_actual.strftime("%d/%m/%Y") #Lo paso al formato de la lista
        
        if (chequeo not in feriados and fecha_actual.weekday() <= 4) :
            # Compruebo si no es feriado o fin de semana
            dias_habi += 1
        fecha_actual +=  timedelta(days = 1)
    return dias_habi


            