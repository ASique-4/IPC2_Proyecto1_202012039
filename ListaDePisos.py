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

            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Piso)
            self.ultimo = nuevo_Piso

    def BubbleSort(self):
        if self.size > 1:
            while True:
                actual = self.primero
                i = None  # anterior
                j = self.primero.siguiente  # siguiente
                cambio = False
                while j != None:
                    if ord(actual.nombre[0])-96 > ord(j.nombre[0])-96:
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
        return False