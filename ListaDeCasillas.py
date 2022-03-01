from Casilla import Casilla
class ListaCasillas():
    def __init__(self):
        self.primero : Casilla = None #cabecera
        self.ultimo = None # final
        self.size = 0
        #self.codigo = codigo
        #self.Casilla = Casilla().getSiguiente()
    
    
    def insertLastCasilla(self, color,columna,fila):
        nuevo_Casilla = Casilla(color,columna,fila)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_Casilla
            self.ultimo = nuevo_Casilla
        else:
            # Inserción con un solo apuntador "primero"
            '''tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(nuevo_Casilla) '''
            
            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Casilla)
            self.ultimo = nuevo_Casilla

    def showCasillas(self):
        tmp = self.primero
        while tmp is not None:
            print('- color: ', tmp.getcolor(), '- fila: ', tmp.getfila(), '- columna: ', tmp.getcolumna())
            tmp = tmp.getSiguiente()
    
    def search_item(self, x,y):
        if self.primero is None:
            return
        n = self.primero
        while n is not None:
            if n.getfila() == y and n.getcolumna() == x:
                print(x,y)
                return n
                
            n = n.siguiente
        print("item not found")
        print(x,y)
        return False
