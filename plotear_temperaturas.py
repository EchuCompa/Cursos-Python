# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:34:10 2020

@author: Diego
"""
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

temperaturas = np.loadtxt("Temperaturas.npy")

# Con esto se ve decente creo
plt.hist(temperaturas,bins=80)

# Así queda más lindo y además tenes la distribución Gaussiana que ni idea pa que sirve
# pero suena útil. Viva Exactas Programa 2!!
plt.figure()
sns.distplot(temperaturas, bins=80)