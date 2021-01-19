# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:29:19 2020

@author: Diego
"""
from informe import leer_camion
from collections import Counter



camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

camion = leer_camion('Data/camion.csv')
tenencias = Counter()
for s in camion:
        tenencias[s['nombre']] += int(s['cajones'])
        

# Las 3 frutas con más cajones
tenencias.most_common(3)

camion2 = leer_camion('Data/camion2.csv')
tenencias2 = Counter()
for s in camion2:
         tenencias2[s['nombre']] += s['cajones']
