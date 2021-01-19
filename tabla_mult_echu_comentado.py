# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:56:03 2020

@author: Diego
"""
#Es una forma horrible y súper manual, pero cumple su cometido.
fila = tuple([0]*10)

print("     0   1   2   3   4   5   6   7   8   9")
print("------------------------------------------")
for n in range(10):
    (cer, pri, seg, ter, cua, qui, sex,  sep, och, nov)= fila
    print(f"{n}:  {cer:>2d}  {pri:>2d}  {seg:>2d}  {ter:>2d}  {cua:>2d}  {qui:>2d}  {sex:>2d}  {sep:>2d}  {och:>2d}  {nov:>2d}")
    fila = (cer, pri+1, seg+2, ter+3, cua+4, qui+5, sex+6,  sep+7, och+8, nov+9)
    
#yo traté de buscarle la vuelta a algo más general pero sólo llegué usando
#el formato ese de %4d %4s etc. y no f-strings
# (es más, me quemé tanto la cabeza con eso que después ni me salió con f-strings)
# así que lo que hiciste vos me parece perfecto
