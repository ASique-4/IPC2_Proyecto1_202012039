from graphviz import Graph
from Patron import Patron
class Matriz():
    def __init__(self,f,c):
        self.filas = f
        self.columnas = c

def llenar_matriz(cadena,columnas):
    c = Graph(name='child', node_attr={'shape': 'box','style': 'filled','fillcolor': 'black'})
    palabra = list(cadena)
    count = 0
    columnas = 4
    count_columnas = 0

    while count < len(palabra):
        nodo1 = str(count_columnas)
        nodo2 = str(count)
        if palabra[count] == 'B':
            if count < columnas:
                c.node(str(count),'',fillcolor='black')
            else:
                c.node(str(count),'',fillcolor='black')
                c.edge(nodo1,nodo2)
                count_columnas += 1
        if palabra[count] == 'W':
            if count < columnas:
                c.node(str(count),'',fillcolor='white')
            else:
                c.node(str(count),'',fillcolor='white')
                c.edge(nodo1,nodo2)
                count_columnas += 1 
        count += 1
    c.view()

def cambiar_matriz(cadena1,cadena2,columnas,precio_flip,precio_slide):
    palabra2 = list(cadena2)
    palabra = list(cadena1)
    