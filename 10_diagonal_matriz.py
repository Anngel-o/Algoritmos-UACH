# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 07:53:23 2022

@author: Anngel Ortiz
"""

from numpy.random import *

mat = randint(1,99,(5,5)) #numeros aleatorios en matriz de 5 x 5

for ren in range(5):
    for col in range(5):
        print(mat[ren][col], end=" ")
    print()
print()
    
for ren in range(5):
    for col in range(5):  
        if ren == col:
            print(mat[ren][col])
            
        