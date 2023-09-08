# aqui va estar el menu 
import os 
import sys
def borrar(): 
     if os.name == "posix" : 
        os.system("clear")
     elif os.name == "nt" : 
        os.system("cls")
def menu(*args):
    #args[0] -> nombre 
    borrar()
    print('''
 ##   ##  #######  ##   ##  ##   ##
 ### ###   ##   #  ###  ##  ##   ##
 #######   ## #    #### ##  ##   ##
 #######   ####    ## ####  ##   ##
 ## # ##   ## #    ##  ###  ##   ##
 ##   ##   ##   #  ##   ##  ##   ##
 ##   ##  #######  ##   ##   #####
''')
    print(f'''
    Encargada -> {args[0]}
    1 -> Agregar Libros 
    2 -> Buscar Libros
    3 -> Ver Libros Disponibles 
    4 -> Devolver Libro 
    5 -> Estadisticas
''')
    try : 
      while True : 
        opcion = int(input("Ingresa la opcion -> "))
        if opcion == 1 : 
             print("Agregar Libro ala base de datos ")
             nombre = input("Ingresa el nombre del libro ")
             if nombre == "": 
                 print("Ingresa un nombre valido")
             else :
                nombre = nombre.capitalize()
                autor = input("Ingresa el autor del libro ")
                if autor == "": 
                    print("Ingresa un nombre valido ")
                else : 
                    autor = autor.capitalize()
                    try :
                        año = int(input("Ingresa el año de publicacion -> "))
                        if año == "" or año <= 0 :
                            print("Año invalido intentalo otra vez ")
                        pass
                    except ValueError :
                        print("Ingresa solamente numeros en el apartado de numeros ")
                    
             pass
        elif opcion == 2 : 
            pass
        elif opcion == 3 : 
            pass 
        elif opcion == 4 : 
            pass 
        elif opcion == 5 : 
            pass 
        elif opcion == 6 :
            sys.exit()
        else : 
            print("Opcion invalida")
    except ValueError :
        borrar()
        print("Ingresa solamente numeros")
        from Modulos.modulo import login
        login()
    
    pass 