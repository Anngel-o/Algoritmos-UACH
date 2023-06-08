# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 08:30:57 2022

@author: Anngel Ortiz
"""
#import numpy as np
from numpy import * #se importa todo

#print(np.ones((3,4)))

def par_impar(numeros):#parámetro
    for i in numeros:
        if i % 2 == 0:
            print("fo")
        else:
            print("la")
    
lista = arange(0,101)
print(lista)

print(par_impar(lista)) #argumento
        

