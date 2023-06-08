# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:13:12 2022

@author: Anngel Ortiz
"""
from numpy.random import *
import time

arr = randint(0,100000,100000) #numeros aleatorios en vector 
inicial = time.process_time()

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

insertionSort(arr)

final = time.process_time()

print("El arreglo ordenado es: ")
for i in range(0,len(arr)):
    print(arr[i])
    
print (final - inicial)