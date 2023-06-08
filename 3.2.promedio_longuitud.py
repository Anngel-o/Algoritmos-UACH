# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:40:43 2022

@author: Anngel Ortiz
"""

cad = "Angel aprende analisis de algoritmos"
def promedio(x):
	palabras = cad.split()
	print(sum(len(pal) for pal in palabras)/len (palabras))
print(cad)