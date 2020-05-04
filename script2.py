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


def magnetization(a,tc, beta, x):
    y  = a*(x-tc)**beta
    return y


pmc=10000000
n = 2 #numero de runes que voy a tirar
T = [1.0,   1.05,    1.1,    1.15,    1.2,    1.25,    1.30,    1.35,    1.40,    1.45,    1.50,    1.55,    1.60,    1.65,    1.70,    1.75,    1.80,    1.85,    1.90,    1.95,    2.00,    2.05,    2.10,    2.15,    2.20,    2.25,    2.30,    2.35,    2.40,    2.45,    2.50,    2.55,    2.60,    2.65,    2.70,    2.75,    2.80,    2.85,    2.90,    2.95,    3.00,    3.05,    3.10,    3.15,    3.20,    3.25,    3.30,    3.35,    3.40,    3.45,    3.50,    4.00,    4.50,    5.00,      2.13, 2.14, 2.125, 2.135, 2.23, 2.27]
run = [15,   15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15, 15, 15, 15, 15, 15, 15]

#T = [2.30, 1.00, 4.00]
#run = [15, 15, 15]




datos = []; E = []; Evar = []; Eerror = []; M = []; Mvar = []; Merror = []; Ratio = []; Cv = []; X = []

for i in T:
    e = []; evar = []; eerror = []; m = []; mvar = []; merror = []; ratio = []; cv = []; x = []
    for j in run:
        for k in range(n+1,j+1):
#            f = open ( '/media/sf_D_DRIVE/Doctorado/Materias/Simulación/Ising/RUNS/'+str(i)+'_temp/'+str(k)+'_run/output.dat' , 'r')
            f = open ( 'D:/Doctorado/Materias/Simulación/Ising/RUNS/'+str(i)+'_temp/'+str(k)+'_run/output.dat' , 'r')
            datos = [line.split() for line in f]

            ##leyendo los listas
            e.append(float(datos[1][2]))
            evar.append(float(datos[2][1]))
            eerror.append(float(datos[3][1]))
            m.append(float(datos[4][2]))
            mvar.append(float(datos[5][1]))
            merror.append(float(datos[6][1]))
            ratio.append(float(datos[7][1]))

           
#    figure(figsize=(14,9))
#    hist(m)
#    grid()
#    xlabel('M', fontsize=14)
#    savefig('M'+str(i)+'.jpg')



            
    E.append(mean(e))
    Evar.append(mean(evar))
    Eerror.append(mean(eerror))
    M.append(abs((mean(m))/400))
    Mvar.append(mean(mvar))
    Merror.append(mean(merror))
    Ratio.append(mean(ratio))
    Cv.append(mean(evar)/(pmc*i**2))
    X.append(mean(mvar)/(i**2))


################################################
figure(figsize=(14,9))
errorbar(T, E,fmt='o', label='E')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=14)
ylabel('E', fontsize=14)
#legend(loc='upper right', fontsize=12)
savefig('energy.jpg')

################################################
x = list(range(2000, 2300)); temp = []
for i in x: temp.append(i*(1/1000))
figure(figsize=(14,9))
errorbar(T, M,fmt='o',color='orange', label='M')
plot(temp, [magnetization(1.08,2.258,0.1246,i) for i in temp])
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=14)
ylabel('M', fontsize=14)
#legend(loc='upper right', fontsize=12)
savefig('magnetization_fit.jpg')

################################################
figure(figsize=(14,9))
errorbar(T, Ratio, fmt='o', color='green', label='Ratio')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=14)
ylabel('Ratio', fontsize=14)
#legend(loc='upper right', fontsize=12)
savefig('ratio.jpg')

################################################
figure(figsize=(14,9))
errorbar(T, Cv, fmt='o', color='yellow', label='Cv')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=14)
ylabel('Cv', fontsize=14)
#legend(loc='upper right', fontsize=12)
savefig('Cv.jpg')

################################################
figure(figsize=(14,9))
errorbar(T, X, fmt='o', color='grey', label='Xv')
# Plot set
#semilogy()
grid()
xlabel('T', fontsize=14)
ylabel('X', fontsize=14)
#legend(loc='upper right', fontsize=12)
savefig('X.jpg')

show()
