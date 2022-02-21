from Matriz import Matriz
from ListaPatrones import ListaPatrones

class Piso(): 
    def __init__(self, nombre, r, c, f, s):
        self.nombre = nombre
        self.filas = r
        self.columnas = c
        self.flip_costo = f
        self.slide_costo = s
        self.siguiente = None
        self.patrones = ListaPatrones()
        self.casillas = Matriz() #Matriz
        
    def getPatrones(self):
        return self.patrones

    def setPatrones(self, patrones):
        self.patrones = patrones

    def getColumnas(self):
        return self.columnas

    def setColumnas(self, Columnas):
        self.columnas = Columnas
    
    def getFilas(self):
        return self.filas

    
    def setFilas(self, Filas):
        self.filas = Filas

    def getCostoF(self):
        return self.filas
    
    def setCostoF(self, Flip):
        self.flip_costo = Flip
    
    def getCostoS(self):
        return self.slide_costo
    
    def setCostoF(self, Slide):
        self.slide_costo = Slide
    
    def getSiguiente(self):
        return self.siguiente
    
    
    def setSiguiente(self, piso):
        self.siguiente = piso