# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:47:59 2022

@author: Anngel Ortiz
"""

from numpy.random import *

mat = randint(1,99,(5,5)) #numeros aleatorios en matriz de 4 x 4

for ren in range(5):
    for col in range(5):
        print(mat[ren][col], end=" ")
    print()
print()
    
print("TRIANGULO INFERIOR")
for ren in range(5):
    for col in range(5):  
        if col < ren:
            print(mat[ren][col])

print("TRIANGULO SUPERIOR")
for ren in range(5):
    for col in range(5):  
        if col > ren:
            print(mat[ren][col])