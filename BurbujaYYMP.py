cnt=0
def burbuja(A):
	global cnt
	for i in range(1,len(A)):
			for j in range(0, len(A)-1):
				cnt+=1
				if(A[j+1]<A[j]):
					aux=A[j]
					A[j]=A[j+1]
					A[j+1]=aux
					#print(A)
	return A

#programa principal
A=[3,6,0,8,10,7,5,4]
print(A)
burbuja(A)

