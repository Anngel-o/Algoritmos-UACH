# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 00:32:13 2022

@author: Anngel Ortiz
"""

frase = (input("Ingresa una frase "))
palabras = frase.split() #genera particiones de los elementos que integran la frase

print(palabras)

numeros_palabras = len(palabras)

if numeros_palabras %2 == 0:
    print("Par")
else:
    print("Impar")
    