# Evaluacion 2 "fibonacci"
ley = {0: 0, 1: 1} #Declaracion de los primeros elementos
def fib(x):
    if x not in ley: #Proceso
        ley[x] = fib(x- 1) + fib(x - 2)
    return ley[x]
for w in range(1,51): #Rango a valorar 
	print(w,fib(w)) #Imprime valor de ( x) y su posicion 