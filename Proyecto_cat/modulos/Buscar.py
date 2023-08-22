import os 

def buscar(*args):
    nombre = args[0]
    try :
        ruta = os.getcwd()
        nombre_extencion = nombre + ".txt"
        sumar = os.path.join(ruta,nombre_extencion)
        existe = os.path.exists(sumar)
        if existe :
            print("El archivo existe y se encuentra en la ruta ->" , sumar)
            opcion = int(input("deseas abrir la\n1-> si \n2-> no "))
            if opcion == 1 :
                mostrar(nombre_extencion)
                pass
            elif opcion == 2 :
                print("Ok que tengas un exelente dia ")
                pass
            else : 
                print("opcion invalida")
        else :
            print("No se encontro el archivo en la base de datos ")
        pass
    except OSError :
        print("Error en la busqueda del archivo")

def mostrar(nombre):
    try :
        tarea = open(nombre,"r")
        mostrar = tarea.read()
        return print(mostrar)
    except FileNotFoundError :
        print("No se a podido abrir el archivo ")
    pass