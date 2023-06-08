# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:40:43 2022

@author: Anngel Ortiz
"""

def contar(cadena):
    contador = 0
    
    while cadena[contador:]: 
    #recorre desde contador = 0 hasta el final de la cadena
        contador += 1;
    return contador

frase = (input("Ingresa una palabra "))
print (len(frase)) #cálcula la longitud de frase
print(contar(frase))