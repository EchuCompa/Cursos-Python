# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#Viendo cómo se abre un archivo comprimido 
# import gzip

# with gzip.open("Data/camion.csv.gz", "rt") as f:
#     for line in f:
#         print(line, end=" ")

import informe
import sys

def fun_costo_camion(archivo):
    costo = 0
    data = informe.leer_camion(archivo) #Acá no hago ningún cambio
    for i,row in enumerate(data):
            costo += int(row["cajones"]) * float(row["precio"]) #Y bue, reemplazo
    return costo
        
def main(argv):
    if len(argv) != 2: 
        raise SystemExit(f'Uso adecuado: {argv[0]} ' 'archivo_camion')
    camion = argv[1]
    print("Total cost: ", fun_costo_camion(camion))
    return 0
    
if __name__ == '__main__':
    main(sys.argv) 

# print('Costo total:', costo1)
