
class Casilla():
    def __init__(self,color,columna,fila,columnas,filas):
        self.color = color
        self.columna = columna 
        self.fila = fila
        self.columnas = columnas
        self.filas = filas
        self.siguiente = None

    def getcolor(self):
        return self.color
    
    
    def setcolor(self, color):
        self.color = color

    def getcolumna(self):
        return self.columna
    
    
    def setcolumna(self, columna):
        self.columna = columna
    
    def getfila(self):
        return self.fila
    
    
    def setfila(self, fila):
        self.fila = fila

    def getSiguiente(self):
        return self.siguiente
    
    
    def setSiguiente(self, casilla):
        self.siguiente = casilla

    def getFilas(self):
        return self.filas
    
    
    def setFilas(self, filas):
        self.filas = filas

    def getSColumnas(self):
        return self.columnas
    
    
    def setColumnas(self, columnas):
        self.columnas = columnas

