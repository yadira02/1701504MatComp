contador=0
def insercion(arreglo): 
	global contador
	for indice in range(1,len(arreglo)):
		valor=arreglo[indice] #valor es el elemento que vamos a comparar
		i=indice-1 #i es el valor anterior al elemento que estamos comparando
		while i>=0: 
			contador+=1
			if valor<arreglo[i]: #compraramos valor con el elemento anterior 
				arreglo[i+1]=arreglo[i] #intercambiamos los valores 
				arreglo[i]=valor
				i-=1 #decremento en 1 el valor de i
			else:
				break
	return arreglo
#programa principaL
print("ARREGLO DESORDENADO:")
A=[3,6,8,2,0,7,9,4]
print(A)
print("ARREGLO ORDENADO: \n", insercion(A))
input("presione enter para continuar")