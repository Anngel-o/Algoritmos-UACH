# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:31:58 2022

@author: Anngel Ortiz
"""
from numpy.random import *
import time

num = randint(0,100000,100000) #numeros aleatorios en vector 

inicial = time.process_time()

for i in range(0,len(num)):
    minimo = i
    for j in range(i+1, len(num)):
        if num[minimo] > num[j]:
            minimo = j
           
    temp = num[i]
    num[i] = num[minimo]
    num[minimo] = temp
    
final = time.process_time()

print("El arreglo ordenado es: ")
print(num)

print (final - inicial)



