from Patron import Patron
class ListaPatrones():
    def __init__(self):
        self.primero : Patron = None #cabecera
        self.ultimo = None # final
        self.size = 0
        #self.codigo = codigo
        #self.patron = Patron().getSiguiente()
    
    
    def insertLastPatron(self, cod,cadena):
        nuevo_Patron = Patron(cod,cadena)
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
        for i in range(self.size):
            print(i, '- Codigo: ', tmp.getCod(), '- Cadena: ', tmp.getCadena())
            tmp = tmp.getSiguiente()