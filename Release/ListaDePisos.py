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
                a = None  # anterior
                b = self.primero.siguiente  # siguiente
                cambio = False
                while b != None:
                    if ord(actual.nombre[0])-96 > ord(b.nombre[0])-96:
                        cambio = True
                        if a != None:
                            tmp = b.siguiente
                            a.siguiente = b
                            b.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = b.siguiente
                            self.primero = b
                            b.siguiente = actual
                            actual.siguiente = tmp2
                        a = b
                        b = actual.siguiente
                    else:
                        a = actual
                        actual = b
                        b = b.siguiente
                if not cambio:
                    break

    def showPisos(self):
        tmp = self.primero
        while tmp is not None:
            print('Nombre: ', tmp.nombre, '- Filas: ', tmp.getFilas(), '- Columnas: ', tmp.getColumnas(), '- Costo Flip: ', tmp.getCostoF(), '- Costo Slide: ', tmp.getCostoS())
            tmp = tmp.getSiguiente()

    def showPisosOrdenados(self):
        tmp = self.primero
        while tmp is not None:
            tmp.getPatrones().BubbleSort() 
            
            print('Nombre: ', tmp.nombre )
            tmp.getPatrones().showPatrones()
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