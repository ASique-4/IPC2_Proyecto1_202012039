from graphviz import Graph

def leer():
    palabra = 'WBWBWWWB'
    c = Graph(name='child', node_attr={'shape': 'box','style': 'filled','fillcolor': 'black'})
    palabra = list(palabra)
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

leer()