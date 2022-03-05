
from time import sleep
from ListaDeCasillas import ListaCasillas


class Matriz():
    def __init__(self):
        pass

    

    def cambiar_matriz(nombre_piso1,nombre_patron1,nombre_patron2,listaPisos):
        texto = ''
        texto2 = ''
        Modo1 = False 
        Modo2 = False
        lista_piso = listaPisos
        costoS = int(lista_piso.search_item(nombre_piso1).getCostoS())
        contadorCostoS1_primero = 0
        contadorCostoS1_segundo = 0
        costoF = int(lista_piso.search_item(nombre_piso1).getCostoF())
        contadorCostoF1_primero = 0
        contadorCostoF2_primero = 0
        contadorCostoF1_segundo = 0
        contadorCostoF2_segundo = 0
        if lista_piso.search_item(nombre_piso1).getPatrones().search_item('NuevoPatron') == False:
            lista_piso.search_item(nombre_piso1).getPatrones().insertLastPatron('NuevoPatron',lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCadena(),llenar_matriz1(lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron1).getCadena(),lista_piso.search_item(nombre_piso1).getColumnas(),lista_piso.search_item(nombre_piso1).getFilas()))
        posicion1 = lista_piso.search_item(nombre_piso1).getPatrones().search_item('NuevoPatron').getCasillas()
        posicion2 = lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCasillas()
        print ("------------------------------------------------------")
        print ("Patron inicial")

        posicion1.showCasillas()
        sleep(2)
        print ("------------------------------------------------------")
        print ("Patron deseado")
        posicion2.showCasillas()
        n = lista_piso.search_item(nombre_piso1).getPatrones().search_item('NuevoPatron').getCasillas().primero
        x = 1
        y = 1
        #Ordenar
        if int(lista_piso.search_item(nombre_piso1).getFilas()) > 1:
            if costoF < costoS:
                Modo1 = True
                while n is not None: #while 2
                    if x > int(lista_piso.search_item(nombre_piso1).getColumnas()):
                        y +=1
                        x = 1
                    else:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    if n is None:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    continue 
            else:
                Modo2 = True
                while n is not None: #while 1
                    if x > int(lista_piso.search_item(nombre_piso1).getColumnas()):
                        y +=1
                        x = 1
                    else:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                            if (y+1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x,y+1).getcolor() and posicion1.search_item(x,y+1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y+1).getcolor() != posicion2.search_item(x,y+1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y+1).getcolor()) 
                                    posicion1.search_item(x,y+1).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y+1,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x+1,y).getcolor() != posicion2.search_item(x+1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x+1)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y-1).getcolor() != posicion2.search_item(x,y-1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y-1,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x-1)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    if n is None:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                            if (y+1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x,y+1).getcolor() and posicion1.search_item(x,y+1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y+1).getcolor() != posicion2.search_item(x,y+1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y+1).getcolor()) 
                                    posicion1.search_item(x,y+1).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y+1,x)
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x+1,y).getcolor() != posicion2.search_item(x+1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x+1)
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y-1).getcolor() != posicion2.search_item(x,y-1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y-1,x)
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x-1)
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    continue   
        elif int(lista_piso.search_item(nombre_piso1).getFilas()) <= 1:
            if costoF < costoS:
                Modo1 = True
                while n is not None: #while 2
                    if x > int(lista_piso.search_item(nombre_piso1).getColumnas()):
                        y +=1
                        x = 1
                    else:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2_primero += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2_primero += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    if n is None:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2_primero += 1 
                                    
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2_primero += 1 
                                    
                                    continue 
            else:
                Modo2 = True
                while n is not None: #while 1
                    if x > int(lista_piso.search_item(nombre_piso1).getColumnas()):
                        y +=1
                        x = 1
                    else:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                            if (y+1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x,y+1).getcolor() and posicion1.search_item(x,y+1).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y+1).getcolor()) 
                                    posicion1.search_item(x,y+1).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y+1,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x+1)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y-1,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1_primero += 1
                                    texto += '---Se hizo un slide en el azulejo en la fila {} y columna {} con el azulejo en el azulejo en la fila {} y columna {} \n'.format(y,x,y,x-1)
                                    x +=1
                                    n = n.siguiente
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1_primero += 1 
                                    texto += '---Se hizo un flip en el azulejo en la fila {} y columna {} \n'.format(y,x)
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    
        print ("------------------------------------------------------")
        sleep(2)
        print ("Ya casi...")
        sleep(2)
        print ("¡Listo! :D")
        sleep(2)
        if Modo2 == True:
            print('1. Mostrar instrucciones en consola ')
            print('2. Mostrar instrucciones en txt ')
            opcion = int(input('Escoja un número: '))
            if opcion == 1:
                posicion1.showCasillas()
                lista_piso.search_item(nombre_piso1).getPatrones().search_item('NuevoPatron').setCadena(lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCadena())
                print(texto)
                print('---Se gasto: ' + str(costoS*contadorCostoS1_primero) + ' de slide')
                print('---Se gasto: ' + str(costoF*contadorCostoF1_primero) + ' de flip')
                print('---El total es de: '+str(int(costoF*contadorCostoF1_primero)+int(costoS*contadorCostoS1_primero))+ ' Quetzales')
                print ("------------------------------------------------------")
            elif opcion == 2:
                a = open('Instrucciones.txt','w')
                a.write(texto)
                a.write('---Se gasto: ' + str(costoS*contadorCostoS1_primero) + ' de slide \n')
                a.write('---Se gasto: ' + str(costoF*contadorCostoF1_primero) + ' de flip \n')
                a.write('---El total es de: '+str(int(costoF*contadorCostoF1_primero)+int(costoS*contadorCostoS1_primero))+ ' Quetzales \n')
                a.close()
                print ("Se ha creado el archivo Instrucciones.txt :D")
                print ("------------------------------------------------------")
        elif Modo1 == True:
            print('1. Mostrar instrucciones en consola ')
            print('2. Mostrar instrucciones en txt ')
            opcion = int(input('Escoja un número: '))
            if opcion == 1:
                posicion1.showCasillas()
                lista_piso.search_item(nombre_piso1).getPatrones().search_item('NuevoPatron').setCadena(lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCadena())
                print(texto)
                print('---Se gasto: 0 de slide')
                print('---Se gasto: ' + str(costoF*contadorCostoF2_primero) + ' de flip')
                print('---El total es de: ' + str(costoF*contadorCostoF2_primero)+ ' Quetzales')
                print ("------------------------------------------------------")
            elif opcion == 2:
                a = open('Instrucciones.txt','w')
                a.write(texto)
                a.write('---Se gasto: ' + str(costoS*contadorCostoS1_primero) + ' de slide \n')
                a.write('---Se gasto: ' + str(costoF*contadorCostoF1_primero) + ' de flip \n')
                a.write('---El total es de: '+str(int(costoF*contadorCostoF1_primero)+int(costoS*contadorCostoS1_primero))+ ' Quetzales \n')
                a.close()
                print ("Se ha creado el archivo Instrucciones.txt :D")
                print ("------------------------------------------------------")
def llenar_matriz1(cadena,columnas,filas):
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