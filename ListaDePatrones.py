import os
import webbrowser
from Casilla import Casilla
from Patron import Patron
class ListaPatrones():
    def __init__(self):
        self.primero : Patron = None #cabecera
        self.ultimo = None # final
        self.size = 0
        #self.codigo = codigo
        #self.patron = Patron().getSiguiente()
    
    
    def insertLastPatron(self, cod,cadena,casillas):
        nuevo_Patron = Patron(cod,cadena)
        nuevo_Patron.setCasillas(casillas)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_Patron
            self.ultimo = nuevo_Patron
        else:
            # Inserción con un solo apuntador "primero"
            '''tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(nuevo_Patron) '''
            
            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Patron)
            self.ultimo = nuevo_Patron

    def showPatrones(self):
        tmp = self.primero
        print ("------------------------------------------------------")
        while tmp is not None:
            print('- Codigo: ', tmp.getCod(), '- Cadena: ', tmp.getCadena())
            print ("------------------------------------------------------")
            tmp = tmp.getSiguiente()
        
    

    def search_item(self, x):
        if self.primero is None:
            return
        n = self.primero
        while n is not None:
            if n.getCod() == x:
                return n
            n = n.siguiente
        print("Patron no encontrado")
        return False