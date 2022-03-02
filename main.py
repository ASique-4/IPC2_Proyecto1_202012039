
from time import sleep
from Matriz import Matriz
from ListaDeCasillas import ListaCasillas
from ListaDePatrones import ListaPatrones
from ListaDePisos import ListaPisos
import PySimpleGUI as sg
import xml.etree.ElementTree as ET

lista_pisos = ListaPisos()
datos_glob = ''
Archivo_Cargado = False
print ("------------------------------------------------------")

        
def elementTree(ruta):

    tree = ET.parse(ruta)
    lista_patrones = ListaPatrones()
    raiz = tree.getroot()
    count3 = 0
    for r in raiz:
        count3 = 0
        for subchild in r: 
            if subchild.tag == 'patrones':
                lista_patrones = ListaPatrones()
                for subsubchild in subchild:
                    if subsubchild.tag == 'patron':
                        casillas = llenar_matriz(subsubchild.text,r[1].text,r[0].text)
                        lista_patrones.insertLastPatron(subsubchild.attrib['codigo'], subsubchild.text,casillas)
                        count3 += 1
        lista_pisos.insertLast(r.attrib['nombre'], r[0].text, r[1].text, r[2].text, r[3].text,lista_patrones) 
    


def llenar_matriz(cadena,columnas,filas):
    lista_casillas = ListaCasillas()
    count = 0
    columnas = int(columnas)
    count_fila = 1
    count_columnas = 0
    for n in cadena:

        if count_columnas >= columnas:
            count_fila +=1
            count_columnas = 1
        else:
            count_columnas +=1

        
        lista_casillas.insertLastCasilla(n,count_columnas,count_fila,columnas,filas)
         
        count += 1
        
    return lista_casillas

def pedirPiso():
    lista_pisos.showPisos()
    correcto=False
    while(not correcto):
        cadena = lista_pisos.search_item(str(input("Introduce un piso: ")))
        try:
            if cadena != False:
                correcto=True
                return cadena
            else:
                print('Error, introduce un piso valido')
        except ValueError:
                print('Error, introduce un piso valido')

def pedirPatron(piso):
    lista_pisos.search_item(str(piso)).getPatrones().showPatrones()
    correcto=False
    while(not correcto):
        cadena = lista_pisos.search_item(str(piso)).getPatrones().search_item(str(input("Introduce un patron: ")))
        try:
            if cadena != False:
                correcto=True
                return cadena
            else:
                print('Error, introduce un piso valido')
        except ValueError:
                print('Error, introduce un piso valido')

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Cargar Archivo")
    print ("2. Analizar pisos")
    print ("3. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("------------------------------------------------------")
        sg.theme('Dark Grey 13')   

        layout = [[sg.Text('Escoge el archivo .xml')],
          [sg.Input(disabled = True , text_color='black' ), sg.FileBrowse(file_types=(("xml Files", "*.xml"),))],
          [sg.OK(), sg.Cancel()]]

        window = sg.Window('Datos', layout)


        event, Datos = window.read()
        
        if Datos[0] == '' or Datos[0] == None or event == 'Cancel' or event == sg.WIN_CLOSED:
            print('No escogiste ningún archivo .xml')
        else:
            print('Escogiste el archivo: ',Datos[0])
            Archivo_Cargado = True
            datos_glob = Datos[0]
        window.close()
        elementTree(datos_glob)
        
        print ("------------------------------------------------------")
    elif opcion == 2:
        print ("------------------------------------------------------")
        if Archivo_Cargado == True:
            lista_casillas = ListaCasillas()
        
            piso = pedirPiso()
            patron = pedirPatron(piso.nombre)
            print ("Calculando la mejor manera de ordenar...")
            sleep(3)
            Matriz.cambiar_matriz(str(piso.nombre),str(piso.getPatrones().primero.getCod()),str(patron.getCod()),lista_pisos)
            print ("Convirtiendo a PDF...")
            sleep(3)
            lista_pisos.search_item(str(piso.nombre)).getPatrones().search_item(str(patron.getCod())).getCasillas().imprimirEnPdf()

        else:
            print('---No has cargado el archivo')
        print ("------------------------------------------------------")
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
