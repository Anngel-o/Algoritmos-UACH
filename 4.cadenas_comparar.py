# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:47:07 2022

@author: Anngel Ortiz
"""

def compararLongitud(f1, f2): #parámetros
    if len(f1) == len(f2):
        #return True
        ret = True
        print(ret)
    else:
        #return False
        ret = False
        print(ret)
        
frase = (input("Ingresa una palabra "))
frasedos = (input("Ingresa otra palabra "))

compararLongitud(frase, frasedos) #argumentos



