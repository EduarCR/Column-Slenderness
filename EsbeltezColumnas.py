# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:49:19 2024

@author: USER
"""

import numpy as np
from Units import m, MPa
import matplotlib.pyplot as plt

plt.close("all")

def plot_params(title,xLabel,yLabel,titleFontSize = 14,otherFontSize = 10,otherFontName = "Gill Sans MT"):
    plt.rc("axes", axisbelow=True)
    plt.rcParams.update({'font.size': otherFontSize})
    plt.rcParams["font.family"] = "serif"
    plt.rcParams['font.serif'] = [otherFontName]
    plt.rcParams['axes.unicode_minus'] = False
    plt.tick_params(direction="in", length=5, colors="k", width=0.75,
                    labelsize=otherFontSize, rotation=0)
    plt.minorticks_on()
    plt.grid(which='major', color='grey', linewidth=0.5, alpha = 0.8)
    # plt.grid(True, which='minor', linewidth=0.5, alpha = 0.4)
    plt.title(title,fontsize=titleFontSize,fontname=otherFontName)
    plt.xlabel(xLabel,fontsize=otherFontSize,fontname=otherFontName)
    plt.ylabel(yLabel,fontsize=otherFontSize,fontname=otherFontName)


# Datos

b = 0.3*m
h = 0.3*m
k = 1       # Factor de longitud efectiva
fc = 21*MPa
fy = 500*MPa

# Cálculos

PI      = np.pi
L       = np.linspace(0.5*m, 20*m, 200)
Ag      = b*h
Ig      = b*h**3/12
beta    = 0.7
Ec      = (4700*(fc/MPa)**0.5)*MPa
EIefec  = 0.4*Ec*Ig/(1+beta)
Pc      = 0.75*PI**2*EIefec/(k*L)**2
fiPn    = 0.65*0.8*(0.85*Ag*fc+0.01*Ag*fy)

print("fiPn=",fiPn)

plt.figure(), plot_params("Límites de esbeltez de columna", "Longitud [m]","Carga [kN]")
plt.ylim([0,1.2*fiPn])
plt.xlim([0,L[-1]])
plt.plot([0, L[-1]],[fiPn,fiPn])
plt.plot(L,Pc)

"""
- La columna falla si está por encima de la curva naranja y/o azul
- La columna es corta si su longitud es menor a la abcisa del punto de intercepción entre
las curvas azul y naranja. En caso contrario es una columna larga/esbelta
"""