#instrucciones:implementar el Algoritmo Dijkstra para la busqueda del camino mas corto entre dos nodos

from heapq import heappop, heappush
def flatten(L):
     while len(L) > 0:
         yield L[0]
         L = L[1]
 
class Grafo:
  
     def __init__(self):
         self.V = set() # un conjunto
         self.E = dict() # un mapeo de pesos de aristas
         self.vecinos = dict() # un mapeo
  
     def agrega(self, v):
         self.V.add(v)
         if not v in self.vecinos: # vecindad de v
             self.vecinos[v] = set() # inicialmente no tiene nada
  
     def conecta(self, v, u, peso=1):
         self.agrega(v)
         self.agrega(u)
         self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
         self.vecinos[v].add(u)
         self.vecinos[u].add(v)
  
     def complemento(self):
         comp= Grafo()
         for v in self.V:
             for w in self.V:
                 if v != w and (v, w) not in self.E:
                     comp.conecta(v, w, 1)
         return comp
     
     def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias
     #Algoritmo Dijkstra
     def shortest1(self,v):
        q= [(0, v, ())]
        dist = dict()
        visited = set()
        while len(q) > 0:
            (l, u, p) = heappop(q)
            if u not in visited:
                visited.add(u)
                dist[u]= (1,u,list(flatten(p))[::-1]+[u])
            p= (u,p)
            for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u,n)]
                    heappush(q, (l+el, n, p))
        return dist
   
# primero 5 nodos con 10 aristas 
print("primer grafo")
g=Grafo()
g.conecta('a','b', 2)
g.conecta('a','c', 3)
g.conecta('a','d', 10)
g.conecta('a','e', 6)
g.conecta('b','c', 5)
g.conecta('b','d', 9)
g.conecta('b','e', 14)
g.conecta('c','d', 7)
g.conecta('d','e', 1)
g.conecta('e','c', 16)
print(g.vecinos['a'])
print(g.shortest('a'))


# primero 10 nodos con 20 aristas
print("segundo grafo")
g1=Grafo()
g1.conecta('a','b', 5)
g1.conecta('a','c', 12)
g1.conecta('a','d', 8)
g1.conecta('a','e', 2)
g1.conecta('a','f', 15)
g1.conecta('a','g', 6)
g1.conecta('a','h', 4)
g1.conecta('a','i', 7)
g1.conecta('a','j', 9)
g1.conecta('b','c', 16)
g1.conecta('b','d', 1)
g1.conecta('b','e', 14)
g1.conecta('b','f', 10)
g1.conecta('b','g', 7)
g1.conecta('b','h', 13)
g1.conecta('b','i', 9)
g1.conecta('b','j', 17)
g1.conecta('c','d', 7)
g1.conecta('c','e', 11)
g1.conecta('c','f', 5)
print(g1.vecinos['b'])
print(g1.shortest('b'))


# primero 15 nodos con 30 aristas
print("tercer grafo")
g2=Grafo() 
g2.conecta('a','b', 2)
g2.conecta('a','c', 3)
g2.conecta('a','d', 10)
g2.conecta('a','e', 6)
g2.conecta('a','f', 5)
g2.conecta('a','g', 9)
g2.conecta('a','h', 14)
g2.conecta('a','i', 7)
g2.conecta('a','j', 1)
g2.conecta('a','k', 16)
g2.conecta('a','l', 2)
g2.conecta('a','m', 3)
g2.conecta('a','n', 10)
g2.conecta('a','o', 6)
g2.conecta('b','c', 5)
g2.conecta('b','d', 9)
g2.conecta('b','e', 14)
g2.conecta('b','f', 7)
g2.conecta('b','g', 1)
g2.conecta('b','h', 16)
g2.conecta('b','i', 2)
g2.conecta('b','j', 3)
g2.conecta('b','k', 10)
g2.conecta('b','l', 6)
g2.conecta('b','m', 5)
g2.conecta('b','n', 9)
g2.conecta('b','o', 14)
g2.conecta('c','d', 7)
g2.conecta('c','e', 1)
g2.conecta('c','f', 16)
print(g2.vecinos['a'])
print(g2.shortest('a'))


# primero 20 nodos con 40 aristas
print("cuarto grafo")
g3=Grafo() 
g3.conecta('a','b', 2)
g3.conecta('a','c', 4)
g3.conecta('a','d', 12)
g3.conecta('a','e', 23)
g3.conecta('a','f', 17)
g3.conecta('a','g', 9)
g3.conecta('a','h', 7)
g3.conecta('a','i', 8)
g3.conecta('a','j', 19)
g3.conecta('a','k', 14)
g3.conecta('a','l', 11)
g3.conecta('a','m', 16)
g3.conecta('a','n', 6)
g3.conecta('a','o', 3)
g3.conecta('a','p', 5)
g3.conecta('a','q', 26)
g3.conecta('a','r', 15)
g3.conecta('a','s', 22)
g3.conecta('a','t', 10)
g3.conecta('b','c', 21)
g3.conecta('b','d', 29)
g3.conecta('b','e', 1)
g3.conecta('b','f', 18)
g3.conecta('b','g', 25)
g3.conecta('b','h', 31)
g3.conecta('b','i', 9)
g3.conecta('b','j', 34)
g3.conecta('b','k', 36)
g3.conecta('b','l', 40)
g3.conecta('b','m', 46)
g3.conecta('b','n', 20)
g3.conecta('b','o', 33)
g3.conecta('b','p', 10)
g3.conecta('b','q', 6)
g3.conecta('b','r', 25)
g3.conecta('b','s', 9)
g3.conecta('b','t', 24)
g3.conecta('c','d', 17)
g3.conecta('c','e', 13)
g3.conecta('c','f', 18)
print(g3.vecinos['a'])
print(g3.shortest('a'))


# primero 25 nodos con 50 aristas
print("quinto grafo")
g4=Grafo() 
g4.conecta('a','b', 2)
g4.conecta('a','c', 4)
g4.conecta('a','d', 10)
g4.conecta('a','e', 13)
g4.conecta('a','f', 17)
g4.conecta('a','g', 11)
g4.conecta('a','h', 27)
g4.conecta('a','i', 8)
g4.conecta('a','j', 9)
g4.conecta('a','k', 24)
g4.conecta('a','l', 31)
g4.conecta('a','m', 26)
g4.conecta('a','n', 5)
g4.conecta('a','o', 21)
g4.conecta('a','p', 34)
g4.conecta('a','q', 16)
g4.conecta('a','r', 35)
g4.conecta('a','s', 32)
g4.conecta('a','t', 28)
g4.conecta('a','v', 17)
g4.conecta('a','w', 3)
g4.conecta('a','x', 7)
g4.conecta('a','y', 8)
g4.conecta('b','c', 23)
g4.conecta('b','d', 29)
g4.conecta('b','e', 33)
g4.conecta('b','f', 18)
g4.conecta('b','g', 35)
g4.conecta('b','h', 36)
g4.conecta('b','i', 42)
g4.conecta('b','j', 28)
g4.conecta('b','k', 13)
g4.conecta('b','l', 32)
g4.conecta('b','m', 11)
g4.conecta('b','n', 34)
g4.conecta('b','o', 21)
g4.conecta('b','p', 4)
g4.conecta('b','q', 9)
g4.conecta('b','r', 7)
g4.conecta('b','s', 12)
g4.conecta('b','t', 19)
g4.conecta('b','v', 20)
g4.conecta('b','w', 30)
g4.conecta('b','x', 15)
g4.conecta('b','y', 5)
g4.conecta('c','d', 8)
g4.conecta('c','e', 19)
g4.conecta('c','f', 37)
g4.conecta('c','g', 39)
g4.conecta('c','h', 13)
print(g4.vecinos['a'])
print(g4.shortest('a'))