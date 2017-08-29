cnt=0

def minimo(arr):
    y=arr[0]
    global cnt
    for x in arr:
        cnt+=1
        if(x<y):
            y=x
    return y

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for y in range(len(aux)):
        x=minimo(aux)
        aux.remove(x)
        arrsort.append(x)
    return arrsort

import random
p=random.sample(range(0,100),50)
print("Arreglo desordenado: ", p)
psort=ordenar(p)
print("\nNumero de operaciones: ", cnt)
print("\nArreglo ordenado:", psort)
input("Presione Enter para continuar")