# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:40:43 2022

@author: Anngel Ortiz
"""

def palindromo(cad):
	if cad == cad[::-1]:
		return True
	else:
		return False
print(palindromo("Ana"))