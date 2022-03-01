
class Matriz():
    def __init__(self):
        pass

    def cambiar_matriz(nombre_piso1,nombre_patron1,nombre_patron2,listaPisos):
        Modo1 = False 
        Modo2 = False
        lista_piso = listaPisos
        costoS = int(lista_piso.search_item(nombre_piso1).getCostoS())
        contadorCostoS1 = 0
        costoF = int(lista_piso.search_item(nombre_piso1).getCostoF())
        contadorCostoF1 = 0
        contadorCostoF2 = 0
        print ("------------------------------------------------------")

        lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron1).getCasillas().showCasillas()
        print ("------------------------------------------------------")

        lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCasillas().showCasillas()
        print ("------------------------------------------------------")
        n = lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron1).getCasillas().primero
        x = 1
        y = 1
        posicion1 = lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron1).getCasillas()
        posicion2 = lista_piso.search_item(nombre_piso1).getPatrones().search_item(nombre_patron2).getCasillas()
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
                                    contadorCostoF2 += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2 += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    if n is None:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2 += 1 
                                    
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2 += 1 
                                    
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
                                    contadorCostoS1 += 1

                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x+1,y).getcolor() != posicion2.search_item(x+1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1 += 1
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y-1).getcolor() != posicion2.search_item(x,y-1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1 += 1
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1 += 1
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1 += 1 

                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1 += 1 
                                    
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
                                    contadorCostoS1 += 1
                                    
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x+1,y).getcolor() != posicion2.search_item(x+1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1 += 1
                                    
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y-1).getcolor() != posicion2.search_item(x,y-1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1 += 1
                                    
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1 += 1
                                    
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1 += 1 
                                    
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1 += 1 
                                    
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
                                    contadorCostoF2 += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2 += 1 
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue          
                        x +=1
                    n = n.siguiente
                    if n is None:
                        if posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y).getcolor():
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF2 += 1 
                                    
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF2 += 1 
                                    
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
                                    contadorCostoS1 += 1

                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1 += 1
                                    print('slide')
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1 += 1
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() :
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1 += 1
                                    
                                    x +=1
                                    n = n.siguiente
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1 += 1 

                                    x +=1
                                    n = n.siguiente
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1 += 1 
                                    
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
                                    contadorCostoS1 += 1
                                    
                                    continue
                            elif (x+1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and posicion1.search_item(x,y).getcolor() != posicion1.search_item(x+1,y).getcolor() and posicion1.search_item(x+1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x+1,y).getcolor() != posicion2.search_item(x+1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x+1,y).getcolor())
                                    posicion1.search_item(x+1,y).setcolor(temp_color)
                                    contadorCostoS1 += 1
                                    print('slide2')
                                    continue
                            elif (y-1) <= int(lista_piso.search_item(nombre_piso1).getFilas()) and (y-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x,y-1).getcolor() and posicion1.search_item(x,y-1).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x,y-1).getcolor() != posicion2.search_item(x,y-1).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x,y-1).getcolor()) 
                                    posicion1.search_item(x,y-1).setcolor(temp_color) 
                                    contadorCostoS1 += 1
                                    
                                    continue
                            elif (x-1) <= int(lista_piso.search_item(nombre_piso1).getColumnas()) and (x-1) > 0 and posicion1.search_item(x,y).getcolor() != posicion2.search_item(x-1,y).getcolor() and posicion1.search_item(x-1,y).getcolor() == posicion2.search_item(x,y).getcolor() and posicion1.search_item(x-1,y).getcolor() != posicion2.search_item(x-1,y).getcolor():
                                    temp_color = posicion1.search_item(x,y).getcolor()
                                    posicion1.search_item(x,y).setcolor(posicion1.search_item(x-1,y).getcolor())   
                                    posicion1.search_item(x-1,y).setcolor(temp_color)   
                                    contadorCostoS1 += 1
                                    
                                    continue
                            else:
                                if posicion1.search_item(x,y).getcolor() == 'B':
                                    posicion1.search_item(x,y).setcolor('W') 
                                    contadorCostoF1 += 1 
                                    
                                    continue
                                elif posicion1.search_item(x,y).getcolor() == 'W':
                                    posicion1.search_item(x,y).setcolor('B') 
                                    contadorCostoF1 += 1 
                                    
                                    continue
        print ("------------------------------------------------------")

        if Modo2 == True:
            posicion1.showCasillas()
            print('Se gasto: ' + str(costoS*contadorCostoS1) + ' de slide')
            print('Se gasto: ' + str(costoF*contadorCostoF1) + ' de flip')
            print('m2')
            print ("------------------------------------------------------")
        elif Modo1 == True:
            posicion1.showCasillas()
            print('Se gasto: 0 de slide')
            print('Se gasto: ' + str(costoF*contadorCostoF2) + ' de flip')
            print('m1')
            print ("------------------------------------------------------")
