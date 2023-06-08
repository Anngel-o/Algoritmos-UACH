# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:16:45 2022

@author: Anngel Ortiz
"""
from numpy.random import *

#def max(numeros):
#    mayor = numeros[0]
        
#    for i in range (1, len(numeros)):
#        if numeros[i] > mayor:
#            mayor = numeros [i]
#    return mayor

#mat = arange(1,51).reshape(5,-1) #el -1 acomoda las fila (o columnas)
#print(mat)
#print(max(mat))

mat = randint(1,99,(4,4)) #numeros aleatorios en matriz de 4 x 4

maximo = mat[0][0]

for ren in range(4):
    for col in range(4):
        print(f'{mat[ren][col]}')
        if mat[ren][col] > maximo:
            maximo = mat[ren][col]
            
print(f"El maximo es: {maximo}")

import numpy as np #np es un alias

print(f"El maximo usando numpy es: {np.max(mat)}")
        
    


    
    