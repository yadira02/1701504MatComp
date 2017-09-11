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

#Programa principal
>>> A=[5,7,3,1,0,9]
>>> A
[5, 7, 3, 1, 0, 9]
>>> selection(A)
[0, 1, 3, 5, 7, 9]
>>> 