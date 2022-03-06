import os
import webbrowser
from Casilla import Casilla
class ListaCasillas():
    def __init__(self):
        self.primero : Casilla = None #cabecera
        self.ultimo = None # final
        self.size = 0

    
    
    def insertLastCasilla(self, color,columna,fila,columnas,filas):
        nuevo_Casilla = Casilla(color,columna,fila,columnas,filas)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_Casilla
            self.ultimo = nuevo_Casilla
        else:

            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_Casilla)
            self.ultimo = nuevo_Casilla

    def showCasillas(self):
        tmp = self.primero
        while tmp is not None:
            print('- color: ', tmp.getcolor(), '- fila: ', tmp.getfila(), '- columna: ', tmp.getcolumna())
            tmp = tmp.getSiguiente()
    
    def imprimirEnPdf(self,nombre):
        nodoCasillas = self.primero
        count_columnas = 0
        count_fila = 1
        strGrafica= 'graph G { \n ranksep = 0; \n nodesep = 0;\n rankdir = "TB";\n'
        ##----------while para crear nodos
        while nodoCasillas is not None:
            if nodoCasillas.getcolor() == 'B':
                color_casilla = 'Black'
                color_casilla2 = 'Black'
                
            if nodoCasillas.getcolor() == 'W':
                color_casilla = 'White'
                color_casilla2 = 'Black'
            strGrafica += str(nodoCasillas.getcolumna())+str(nodoCasillas.getfila())+'[label="",color = "'+color_casilla2+'",fillcolor="'+color_casilla+'",style="filled",shape="box"];\n'
            nodoCasillas=nodoCasillas.siguiente
        ##----------while para Unir nodos
        nodoCasillas=self.primero
        strRank = '    { rank=same; '
        while nodoCasillas is not None:
            if nodoCasillas.siguiente is None:
                None
            else: 
                count = 0
                while count <= int(nodoCasillas.getFilas())*int(nodoCasillas.getSColumnas()):
                    if count_fila < int(nodoCasillas.getFilas()):
                        if count_columnas >= int(nodoCasillas.getSColumnas()):
                            count_fila +=1
                            count_columnas = 1
                            
                            strRank += '    }; \n'
                            strRank += '    { rank=same; '
                            
                        else:
                            count_columnas += 1
                        if int(count_fila+1) <= int(nodoCasillas.getFilas()):
                            strGrafica += '{}--{}[color = "White"];\n'.format(str(count_columnas)+str(count_fila),str(count_columnas)+str(count_fila+1))
                            strRank += str(count_columnas)+str(count_fila) + ' '
                        if count_columnas+1 <= int(nodoCasillas.getSColumnas()):
                            strGrafica += '{}--{}[color = "White"];\n'.format(str(count_columnas)+str(count_fila),str(count_columnas+1)+str(count_fila))
                            strRank += str(count_columnas)+str(count_fila) + ' '
                    else:
                        if count_columnas <= int(nodoCasillas.getSColumnas()):
                            count_columnas += 1
                        if count_columnas+1 <= int(nodoCasillas.getSColumnas()):
                            strGrafica += '{}--{}[color = "White"];\n'.format(str(count_columnas)+str(count_fila),str(count_columnas+1)+str(count_fila))
                            strRank += str(count_columnas)+str(count_fila) + ' '
                    count += 1
            if nodoCasillas.siguiente is None:
                strRank += str(nodoCasillas.getSColumnas()).strip()+str(nodoCasillas.getFilas()).strip() + ' '
            nodoCasillas=nodoCasillas.siguiente
        
        strRank += '    }; '
        strGrafica += strRank
        strGrafica+="}"
        documentotxt="Resultado.txt"
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf=nombre + ".pdf"
        os.system("dot -Tpdf "+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)

    def search_item(self, x,y):
        if self.primero is None:
            return
        n = self.primero
        while n is not None:
            if n.getfila() == y and n.getcolumna() == x:
                return n
                
            n = n.siguiente
        print("Casilla no encontrada")
        print(x,y)
        return False
