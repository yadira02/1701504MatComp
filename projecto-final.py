# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:07:00 2017

@author: Luis Nerio
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:57:05 2017

@author: Luis Nerio
"""

import random
import numpy
import copy
import time

"""******************************************************************************************
############################################################################################
Función para crear números aleatorios, toma como parametros n, que es la cantidad de números
que deseas y  lim_inf y lim_sup que son parametros para indicar el intervalo en el que deben
estar los números aleatorios generados
############################################################################################
******************************************************************************************"""
def ran_num(n,lim_sup=1000000000):
    arreglo = random.sample(range(lim_sup),n)
    return arreglo

"""******************************************************************************************
############################################################################################
                                    Quicksort
Función para ordenar un arreglo de longitud arbitraria con el algoritmo quicsort , toma como
parametro el arreglo, el indice menor y mayor del arreglo
############################################################################################
******************************************************************************************"""
def quicksort(arreglo,low,high ):
    if low < high:
        m = particion(arreglo, low, high)    
        quicksort(arreglo,low,m-1)
        quicksort(arreglo, m+1 , high)


"""******************************************************************************************
############################################################################################
                                    Partición
Función para realizar una subrutina del algoritmo quicksort
la función regresa el indice del valor pivote en su orden respectivo en el arreglo
############################################################################################
******************************************************************************************"""
def particion(arreglo, low, high):
    pivote = arreglo[high]
    wall = low-1
    for j in range(low, high):
        if arreglo[j]<pivote:
            wall = wall + 1
            swap(arreglo,wall,j)
    if(arreglo[high]< arreglo[wall+1]):
        swap(arreglo,wall+1,high)
    return wall+1

"""******************************************************************************************
############################################################################################
                                            swap
Función que realiza un intercambio de posición de valores dentro de un arreglo, toma como parametros
el arreglo  y los indices de los valores a cambiar
############################################################################################
******************************************************************************************"""
def swap(arreglo, a, b):
    aux = arreglo[a]
    arreglo[a]= arreglo[b]
    arreglo[b]= aux


"""******************************************************************************************
############################################################################################
                                            Mediana
Función que encuentra la mediana de un arreglo
############################################################################################
******************************************************************************************"""

def mediana1(arr):
        tiempo1=time.time()
        quicksort(arr,0,len(arr)-1)
        if (((len(arr))%2)!=0):
            med=        arr[int(len(arr)/2)] 
        else:
            med =    (arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)] ) /2 
        tiempo2 = time.time()
        return (med,tiempo2-tiempo1)
        



def split(arreglo,n, pivote,iz, de ):
    while(iz<de):
        while ( arreglo[iz]<pivote):
            iz+=1
        while (arreglo[de]>pivote):
            de-=1
        aux = arreglo[iz]
        arreglo[iz] = arreglo[de]
        arreglo[de] = aux
    return (arreglo,pivote,iz, len(arreglo)//2)

def mediana2(arreglo ):
    tiempo1=time.time()
    k=len(arreglo)//2
    I=0
    D = len(arreglo) -1
    lon = len(arreglo)
    if(len(arreglo)%2!=0):##len(arreglo)%2!=0
        while(True):
            pivote = arreglo[(I+D)//2]
            s=split(arreglo,lon,pivote,I,D)
            if(s[2]==k):
                tiempo2=time.time()
                return (s[1], tiempo2-tiempo1)
            elif (s[2]<k):
                I = s[2]+1
            else:
                D = s[2]-1
    else:
        mediana=0
        while(True):
            pivote = arreglo[(I+D)//2]
            s=split(arreglo,lon,pivote,I,D)
            if(s[2]==k):
                #print(arreglo)
                mediana=mediana+s[1]
                arreglo.pop()
                #print(arreglo)
                break
            elif (s[2]<k):
                I = s[2]+1
            else:
                D = s[2]-1
        k=len(arreglo)//2
        I=0
        D = len(arreglo) -1
        lon = len(arreglo)
        while(True):
            pivote = arreglo[(I+D)//2]
            s=split(arreglo,lon,pivote,I,D)
            if(s[2]==k):
                mediana=mediana+s[1]
                tiempo2= time.time()
                return (mediana/2, tiempo2-tiempo1)
                break
            elif (s[2]<k):
                I = s[2]+1
            else:
                D = s[2]-1  




###########################################################################
#Ejemmplo
###########################################################################
arr1 = ran_num(500000)                             ##arreglo desordenado
arr2 = copy.deepcopy(arr1)                               ##arreglo ordenado
arr3= copy.deepcopy(arr1)



print("\n" +"Mediana calculada con funcion de python " + str(numpy.median(arr1 )) )
print("Mediana calculada con funcion de Reynolds y Daniela " + str(mediana1(arr2)))
print("Mediana calculada con funcion de Nerio " + str(mediana2(arr3)))

longitud=[]
tiempo1=[]
tiempo2=[]
for i in range(1, 100005,10000):
    for m in range (20):
        longitud.append(i)
        arr1 = ran_num(i)                             
        arr2= copy.deepcopy(arr1)
        med1=mediana1(arr1)
        med2=mediana2(arr2)
        tiempo1.append(med1[1])
        tiempo2.append(med2[1])
    
    




