# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:55:39 2017

@author: Angies computer
"""

class fila(object):
    def __init__(self):
        self.fila=[]
    def obtener(self):
        return self.fila.pop(0)
    def meter(self,e):
        self.fila.append(e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)
    
class Grafo: 
   
     def __init__(self): 
         self.V = set()  
         self.E = dict()  
         self.vecinos = dict() 
   
     def agrega(self, v): 
         self.V.add(v) 
         if not v in self.vecinos: 
             self.vecinos[v] = set()     
     def conecta(self, v, u, peso=1): 
         self.agrega(v) 
         self.agrega(u) 
         self.E[(v, u)] = self.E[(u, v)] = peso  
         self.vecinos[v].add(u) 
         self.vecinos[u].add(v) 
   
     def complemento(self): 
         comp= Grafo() 
         for v in self.V: 
             for w in self.V: 
                 if v != w and (v, w) not in self.E: 
                     comp.conecta(v, w, 1) 
         return comp 

def BFS(self,ni):
        visitados =[]
        f=fila()
        f.meter(ni)
        while(f.longitud>0):
            na =f.obtener()
            visitados.append(na)
            vecinos = self.vecinos[na]
            for nodo in vecinos:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados