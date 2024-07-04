# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:51:43 2024

@author: USER
"""

# Unidades base
# -------------
m, kN, sec = 1.0, 1.0, 1.0

LunitsTXT = "m"
FunitsTXT = "KN"
TunitsTXT = "sec"

# Otras unidades
# --------------
mm = m/1E3
cm = m/1E2
N = kN/1E3
mN = N/1E6
Pa, kPa, MPa, GPa = N/m**2, 1E3*N/m**2, 1E6*N/m**2, 1E9*N/m**2
g = 9.80665*m/(sec**2)

# Conversión de unidades
# ----------------------
inch = 0.0254*m
ft = 12*inch
kip = N/0.000225
ksi = kip/(inch**2)
psi = ksi/1E3