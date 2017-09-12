cnt=0
def selection(arr):
	global cnt
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			cnt=cnt+1
			if arr[j]<arr[val]:
				val=j
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr
#programa principaL
print("ARREGLO DESORDENADO:")
A=[3,7,9,4,0,5,1]
print(A)
print("ARREGLO ORDENADO: \n", selection(A))
input("presione enter para continuar")