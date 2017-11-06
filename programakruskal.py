from copy import deepcopy
import random
import math

class grafo:
    def __init__(self):
        self.V =set() #un conjunto
        self.E = dict() #un mapeo de pesos a aritstas
        self.vecinos = dict() #un mapeo
        
    def agrega(self, v ):
        self.V.add(v)
        if not  v in self.vecinos: # vecindad de v
            self.vecinos[v]= set() #inicialmente no tiene nada
    def conecta(self, v , u , peso = 1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)] = self.E[(u,v)] = peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        
    def complemento(self):
        comp= grafo()
        for v in self.V:
            for w in self.V:
                if v != w  and (v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp
    
    def aristas(self):
        return self.E
    
    def vertices(self):
        return self.V
    
    def __str__(self):
        return "Aristas= " + str(self.E)+"\nVertices = " +str(self.V)
    
    def BFS_n(self, ni):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=fila()      ##fila con los nodos por visitar          
        Xvisitar.meter( ni )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados

    def DFS_n(self, ni):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=pila()      ##fila con los nodos por visitar          
        Xvisitar.meter( ni )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados
#    def BFS_N(self, ni):
#        visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
#        Xvisitar=fila()
#        Xvisitar.meter(  (ni,0)   )   
#        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
#            nodo = Xvisitar.obtener()
#            if nodo[0] not in visitados:
#                visitados[nodo[0]]=nodo[1]
#                for vecino in self.vecinos[nodo[0]]:
#                    #vecinos_d.append( (e,nodo[1]+1) )
#                    Xvisitar.meter((vecino,nodo[1]+1))
#                #for v in vecinos_d:
#                    #f.meter(v)
#        return visitados
 
    @property
    def diametro(self):
        maximo = 0
        for vertice in self.V:
            dic_bfs = BFS_N(self, vertice)
            if max(dic_bfs.values())>maximo:
                maximo = max(dic_bfs.values())
        return maximo
    
    @property
    def centrales(self):
        di_ma=dict()  #distancias maximas de cada vertice
        nodos_centrales=[]
        for v in self.V:
            diccionario = BFS_N(self, v)
            di_ma[v]= max(diccionario.values()  )
        radio = min(di_ma.values())
        for valor in di_ma:
            if di_ma[valor] == radio:
                nodos_centrales.append(valor)
        return nodos_centrales
    
    def dijkstra(self, actual):
        distancia = dict()
        previo = dict()
        vertices = self.V.copy()
        for v in vertices:
            distancia[v] = math.inf
            previo[v]="indefinido"
            
        distancia[actual]= 0
        
        while len(vertices)!= 0:
            minimo = math.inf
            for e in vertices:
                aux = distancia[e]
                if aux < minimo:
                    u = e
                    minimo=distancia[e]
            vertices.remove(u)
            
            for v in self.vecinos[u]:
                alternativa = distancia[u]+self.E[(u,v)]
                if alternativa < distancia[v]:
                    distancia[v]=alternativa
                    previo[v]=u   
        return (distancia,previo)    
    
    
    def kruskal(self):
        e = deepcopy(self.E)
        arbol = grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol
    
    def DFS(self,ni):
        visitados =[]
        f=pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def vecinoMasCercano(self):
        lv = list(self.V)   ##lista de vertices
        random.shuffle(lv)
        ni = lv.pop()
        inicial = ni
        lv2=list()
        lv2.append(ni)
        peso=0
        while len(lv2)<len(self.V):
            le = list()
            ln=list()
            ln = self.vecinos[ni]
            for nv in ln:
                if nv not in lv2:
                    le.append((nv,self.E[(ni,nv)]))
            sorted(le, key = lambda le: le[1] )
            t=le[0]
            lv2.append(t[0])
            peso=peso+t[1]
            ni=t[0]
        peso=peso+self.E[lv2[-1], inicial]
        lv2.append(inicial)
        return (lv2,peso)
    

def BFS_N(g, ni):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=fila()
    Xvisitar.meter(  (ni,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados

def DFS_N(g, ni):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=pila()
    Xvisitar.meter(  (ni,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados


class pila(object):##quitas el mas nuevo STACK
    def __init__(self):
        self.a=[]
    
    def obtener(self):
        return self.a.pop()
    
    def meter(self, e):
        self.a.append(e)
        
    @property
    def longitud(self):
        return len(self.a)
    
    def __str__(self):
        return "<" + str(self.a)+ ">"
    
    



class fila(pila):##quitas el que ha estado mas tiempo QUEUE
    def obtener(self):
        return self.a.pop(0)

g= grafo()
g.conecta('a','b', 4)
g.conecta('a','c', 2)
g.conecta('a','d', 8)
g.conecta('a','e', 1)
g.conecta('b','c', 10)
g.conecta('b','d', 2)
g.conecta('b','e', 15)
g.conecta('c','e', 3)
g.conecta('c','d', 6)
g.conecta('d','e', 11)

print(g)
k = g.kruskal()

for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)
    
    
    
m = grafo()
m.conecta('allende', 'montemorelos', 24)
m.conecta('allende', 'congregacion calles', 14)
m.conecta('allende', 'cola de caballo', 20)
m.conecta('allende', 'general teran', 42)
m.conecta('allende', 'estanzuela', 44)
m.conecta('allende', 'rayones', 66)
m.conecta('allende', 'laguna de sanchez', 61)
m.conecta('allende', 'linares', 72)
m.conecta('allende', 'uni', 70)

m.conecta('montemorelos','congregacion calles', 13)
m.conecta('montemorelos','cola de caballo', 45)
m.conecta('montemorelos','general teran', 18)
m.conecta('montemorelos','estanzuela', 67)
m.conecta('montemorelos','rayones', 61)
m.conecta('montemorelos','laguna de sanchez', 84)
m.conecta('montemorelos','linares',51)
m.conecta('montemorelos','uni', 93)

m.conecta('congregacion calles','cola de caballo',32 )
m.conecta('congregacion calles','general teran', 31)
m.conecta('congregacion calles','estanzuela', 55)
m.conecta('congregacion calles','rayones', 56)
m.conecta('congregacion calles','laguna de sanchez',71)
m.conecta('congregacion calles','linares', 61)
m.conecta('congregacion calles','uni', 81)

m.conecta('cola de caballo','general teran', 62)
m.conecta('cola de caballo','estanzuela', 26)
m.conecta('cola de caballo','rayones',86 )
m.conecta('cola de caballo','laguna de sanchez', 39)
m.conecta('cola de caballo','linares', 92)
m.conecta('cola de caballo','uni', 52)

m.conecta('general teran','estanzuela', 85)
m.conecta('general teran','rayones',79)
m.conecta('general teran','laguna de sanchez', 101)
m.conecta('general teran','linares', 67)
m.conecta('general teran','uni', 111)

m.conecta('estanzuela','rayones', 109)
m.conecta('estanzuela','laguna de sanchez', 65)
m.conecta('estanzuela','linares', 116)
m.conecta('estanzuela','uni', 24)

m.conecta('rayones','laguna de sanchez', 126)
m.conecta('rayones','linares', 110)
m.conecta('rayones','uni', 133 )

m.conecta('laguna de sanchez','linares', 131)
m.conecta('laguna de sanchez','uni', 89)

m.conecta('linares','uni', 140)




k = m.kruskal()
for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += m.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], m.E[(dfs[f],dfs[f+1])] )
            
    c += m.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], m.E[(dfs[-1],dfs[0])])
    print('costo',c,'\n')



import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

data = list('abcdefghij')
tim=time.clock()
per = permutation(data)
print(time.clock()-tim) 
