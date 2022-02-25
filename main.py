from Matriz import Matriz
from ListaCasillas import ListaCasillas
from ListaPatrones import ListaPatrones
from ListaPisos import ListaPisos
import PySimpleGUI as sg
import xml.etree.ElementTree as ET

lista_pisos = ListaPisos()
datos_glob = 'pisos.xml'

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
                        casillas = llenar_matriz(subsubchild.text,r[1].text)
                        lista_patrones.insertLastPatron(subsubchild.attrib['codigo'], subsubchild.text,casillas)
                        count3 += 1
        lista_pisos.insertLast(r.attrib['nombre'], r[0].text, r[1].text, r[2].text, r[3].text,lista_patrones) 
    


def llenar_matriz(cadena,columnas):
    lista_casillas = ListaCasillas()
    palabra = list(cadena)
    count = 0
    columnas = int(columnas)
    count_fila = 1
    count_columnas = 0
    while count < len(palabra):

        if count_columnas >= columnas:
            count_fila +=1
            count_columnas = 1
        else:
            count_columnas +=1

        
        lista_casillas.insertLastCasilla(palabra[count],count_columnas,count_fila)
         
        count += 1
        
    return lista_casillas


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
    print ("3. Hacer grafico")
    print ("4. Salir")
     
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
            datos_glob = Datos[0]
        window.close()
        print ("------------------------------------------------------")
    elif opcion == 2:
        print ("------------------------------------------------------")
        elementTree(datos_glob)
        Matriz.cambiar_matriz('ejemplo01','cod11','ejemplo01','cod12',lista_pisos)
        #lista_pisos.search_item('ejemplo01').getPatrones().search_item('cod11').getCasillas().search_item(4,1)
        #lista_pisos.showPisos()
        print ("------------------------------------------------------")
    elif opcion == 3:
        print ("------------------------------------------------------")
        
        print ("------------------------------------------------------")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
