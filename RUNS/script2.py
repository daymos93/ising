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
#from numpy import *
import math

n = 2 #numero de runes que voy a tirar
T = [1.0, 1.5, 1.75, 1.8, 1.85, 1.9, 1.95, 1.96, 1.97,1.98, 1.99, 2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.5, 2.75, 3.0, 4.0, 5.0]
run = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
datos = []; E = []; Evar = []; Eerror = []; M = []; Mvar = []; Merror = []; Ratio = []

for i in T:
    e = []; evar = []; eerror = []; m = []; mvar = []; merror = []; ratio = []
    for j in run:
        for k in range(n+1,j+1):
            f = open ( '/home/mroncoroni/Cursos/Simulaciones/Ising/RUNS/T_'+str(i)+'/'+str(k)+'_run/output.dat' , 'r')
            datos = [line.split() for line in f]

            ##leyendo los listas
            e.append(float(datos[1][2]))
            evar.append(float(datos[2][1]))
            eerror.append(float(datos[3][1]))
            m.append(float(datos[4][2]))
            mvar.append(float(datos[5][1]))
            merror.append(float(datos[6][1]))
            ratio.append(float(datos[7][1]))
            
    E.append(mean(e))
    Evar.append(mean(evar))
    Eerror.append(mean(eerror))
    M.append(abs(mean(m)))
    Mvar.append(mean(mvar))
    Merror.append(mean(merror))
    Ratio.append(mean(ratio))
   

figure(figsize=(14,9))
errorbar(T, E,fmt='o', label='E')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=12)
ylabel('E', fontsize=12)
#legend(loc='upper right', fontsize=12)
savefig('energy.jpg')

figure(figsize=(14,9))
errorbar(T, M,fmt='o',color='orange', label='M')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=12)
ylabel('M', fontsize=12)
#legend(loc='upper right', fontsize=12)
savefig('magnetization.jpg')

figure(figsize=(14,9))
errorbar(T, Ratio, fmt='o', color='green', label='Ratio')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=12)
ylabel('Ratio', fontsize=12)
#legend(loc='upper right', fontsize=12)
savefig('ratio.jpg')

show()
