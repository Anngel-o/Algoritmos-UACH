# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:58:13 2022

@author: nngel

"""

from numpy.random import *
import time
import random

inicial = time.time()

tasks = [randint(1,500, (3)) 
         for i in range(10)]

#tasks = [[0,6,3],[1,4,5],[3,5,1],[3,8,8],[4,7,4],[5,9,4],[6,10,2],[4,11,3]]
print(tasks)

#ordenar trabajos por tiempo final
from operator import itemgetter

tasks = sorted(tasks, key = itemgetter(1))
for i, t in enumerate (tasks):
    print(f'Trabajo {i+1} => finaliza en {t[1]}')

#busqueda binaria buscará un elemento en el arreglo ordenado, lo comparará contra el
#elemento de la mitad del arreglo, si es menor, descartará la segunda mitad del arreglo
#y vuelve a comparar el elemento buscado contra el elemento de la mitad del 1er array
def binarySearch(A, index, start, end):
    mid = int((start+end)/2)
    if index == A[mid]:
        return mid
    elif start == end:
        return -1
    elif index < A[mid]:
        return binarySearch(A, index, 0, mid-1)
    else:
        return binarySearch(A, index, mid+1, end)

#probar la busqueda binaria
f = [4,5,6,7,8,9,10,11]
#Acá buscamos el n6 en el array, el cual está en la posición 2
print(binarySearch(f, 34, 0, 7))

#Extraemos la lista de tiempos finales de tasks y las ganancias de cada trabajo
t_f = []
weigths = list()
for i in tasks:
    t_f.append(i[1])
    weigths.append(i[2])
print(t_f)
print(weigths)

#Calculamos los p()'s de los procesos
w = []
print(tasks)
for index, trabajo in enumerate(tasks):
    print(f'trabajo {index+1}, inicia {trabajo[0]}, lista de tiempos finales {t_f}')
    w.append(binarySearch(t_f, trabajo[0],0,9))

#Estos son los valores de p()'s de los trabajos -->LIST COMPRENHENSION
p = [i+1 for i in w]
print(p)
len(p)
list(map(lambda i: i+1, w))

#COMPUTE-OPT(j)
p.insert(0,0)
weigths.insert(0,0)

def computeOpt(j,p,w):
    if j == 0:
        return 0
    else:
        return max(computeOpt(j-1,p,w), w[j]+computeOpt(p[j],p,w))

print(computeOpt(8, p, weigths))

#M-COMPUTE-OPT(j)
#inicializamos el vector M
M = []
for i in range(9):
    M.append(-1)
#print(p)
print(M)

def McomputeOpt(j,p,w, M):
    if j > 0:
        if M[j] == -1:
            M[j] = max(McomputeOpt (j-1,p,w,M), w[j] + McomputeOpt(p[j], p, w, M) )
        return M[j]
    else:
        return 0

print(McomputeOpt(8, p, weigths, M))