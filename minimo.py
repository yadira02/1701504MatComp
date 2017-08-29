cnt=0

def minimo(arr):
    k=arr[0]
    global cnt
    for w in arr:
        cnt+=1
        if(w<k):
            k=w
    return k

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for k in range(len(aux)):
        w=minimo(aux)
        aux.remove(w)
        arrsort.append(w)
    return arrsort

import random
p=random.sample(range(0,100),40)
print("Arreglo desordenado: ", p)
psort=ordenar(p)
print("\nNumero de operaciones: ", cnt)
print("\nArreglo ordenado:", psort)
input("Presione Enter para continuar")