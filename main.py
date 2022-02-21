import graphviz
from ListaPatrones import ListaPatrones
from ListaPisos import ListaPisos
import PySimpleGUI as sg
import xml.etree.ElementTree as ET

lista_pisos = ListaPisos()
datos_glob = ''

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
                        lista_patrones.insertLastPatron(subsubchild.attrib['codigo'], subsubchild.text)
                        count3 += 1
        lista_pisos.insertLast(r.attrib['nombre'], r[0].text, r[1].text, r[2].text, r[3].text,lista_patrones) 



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
        lista_pisos.showPisos()
        print ("------------------------------------------------------")
    elif opcion == 3:
        print ("------------------------------------------------------")
        #grafo = graphviz.Graph()
        
        print ("------------------------------------------------------")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")