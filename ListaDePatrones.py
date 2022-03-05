
from Patron import Patron
class ListaPatrones():
    def __init__(self):
        self.primero : Patron = None #cabecera
        self.ultimo = None # final
        self.size = 0

    def BubbleSort(self):
        if self.size > 1:
            while True:
                actual = self.primero
                i = None  # anterior
                j = self.primero.siguiente  # siguiente
                cambio = False
                while j != None:
                    if ord(actual.cod[0])-96 > ord(j.cod[0])-96:
                        cambio = True
                        if i != None:
                            tmp = j.siguiente
                            i.siguiente = j
                            j.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = j.siguiente
                            self.primero = j
                            j.siguiente = actual
                            actual.siguiente = tmp2
                        i = j
                        j = actual.siguiente
                    else:
                        i = actual
                        actual = j
                        j = j.siguiente
                if not cambio:
                    break
    
    def insertLastPatron(self, cod,cadena,casillas):
        nuevo_Patron = Patron(cod,cadena)
        nuevo_Patron.setCasillas(casillas)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_Patron
            self.ultimo = nuevo_Patron
        else:
            
            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Patron)
            self.ultimo = nuevo_Patron

    def showPatrones(self):
        tmp = self.primero
        print ("------------------------------------------------------")
        while tmp is not None:
            print('- Codigo: ', tmp.getCod(), '- Cadena: ', tmp.getCadena())
            
            tmp = tmp.getSiguiente()
        print ("------------------------------------------------------")
        
    

    def search_item(self, x):
        if self.primero is None:
            return
        n = self.primero
        while n is not None:
            if n.getCod() == x:
                return n
            n = n.siguiente
        return False