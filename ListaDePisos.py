from Piso import Piso
class ListaPisos():
    def __init__(self):
        self.primero : Piso = None #cabecera
        self.ultimo = None # final
        self.size = 0

    
    def insertLast(self, nombre, r, c, f, s,patrones):
        nuevo_Piso = Piso(nombre, r, c, f, s)
        nuevo_Piso.setPatrones(patrones)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_Piso
            self.ultimo = nuevo_Piso
        else:
            # Inserción con un solo apuntador "primero"
            '''tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(nuevo_Piso) '''
            
            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Piso)
            self.ultimo = nuevo_Piso


    def showPisos(self):
        tmp = self.primero
        while tmp is not None:
            print('Nombre: ', tmp.nombre, '- Filas: ', tmp.getFilas(), '- Columnas: ', tmp.getColumnas(), '- Costo Flip: ', tmp.getCostoF(), '- Costo Slide: ', tmp.getCostoS())
            tmp = tmp.getSiguiente()
    
    def search_item(self, x):
        if self.primero is None:
            return
        n = self.primero
        while n is not None:
            if n.nombre == x:
                return n
            n = n.siguiente
        print("Piso no encontrado")
        return False