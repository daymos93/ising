# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:43:03 2019

@author: Dayron
"""

# importar todas las funciones de pylab
from pylab import *

# importar el módulo pyplot
import matplotlib.pyplot as plt
import numpy as np

f = open ( 'output.dat' , 'r')
datos = []
datos = [line.split() for line in f]

temp = float(datos[0][1]) #temperatura

#leyendo los listas energía y magnetización
energy = []; magnet = []; 
for i in range (2,len(datos)-1): energy.append(float(datos[i][0])); magnet.append(float(datos[i][1])); 

k = list(range(len(energy)))



#valores medios requeridos 
E = mean(energy)
M = mean(magnet)
ratio = float(datos[-1][1])

figure(figsize=(14,9))

errorbar(k, energy,fmt='o', label='E')


# Plot set
#semilogy()
grid()

legend(loc='upper right', fontsize=12)
savefig('energy.jpg')

figure(figsize=(14,9))

errorbar(k, magnet,fmt='o', label='M')


# Plot set
#semilogy()
grid()

legend(loc='upper right', fontsize=12)
savefig('magnetization.jpg')

show()