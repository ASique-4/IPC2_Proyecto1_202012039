from ListaCasillas import ListaCasillas
class Patron():
    def __init__(self, cod, cadena):
        self.cod = cod
        self.cadena = cadena
        self.casillas = ListaCasillas()
        self.siguiente = None
    
    def getCadena(self):
        return self.cadena
    
    
    def setCadena(self, cadena):
        self.cadena = cadena

    def getCod(self):
        return self.cod
    
    
    def setCod(self, cod):
        self.cod = cod

    def getCasillas(self):
        return self.casillas
    
    
    def setCasillas(self, casillas):
        self.casillas = casillas

    def getSiguiente(self):
        return self.siguiente
    
    
    def setSiguiente(self, patron):
        self.siguiente = patron