# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:33:09 2022

@author: Anngel Ortiz
"""

import time

arr = [0, 4, 7, 1600, 1, 2, -100, 78, 13, 7, 12]

inicial = time.process_time()

for i in range(0,len(arr)):
    minimo = i
    for j in range(i+1, len(arr)):
        if arr[minimo] > arr[j]:
            minimo = j
           
    temp = arr[i]
    arr[i] = arr[minimo]
    arr[minimo] = temp

final = time.process_time()
print("El arreglo ordenado es: ")
print(arr)
print (final - inicial)