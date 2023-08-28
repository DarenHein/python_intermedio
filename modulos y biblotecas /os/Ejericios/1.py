#mirar los directorios de una carpeta especificada 
import os 
def decoradora(funcion_original):
    def secundaria():
        while True :
            funcion_original()
    return secundaria

@decoradora
def funcion():
    try:
        print( " ")
        ruta = os.getcwd()
        lista = os.listdir(ruta)
        for elementos in lista : 
            print("-> " , elementos)
        nombre = input("ingresa el nombre del directorio a entrar -> ")
        nueva_ruta = os.path.join(ruta,nombre)
        lista_nuevo = os.listdir(nueva_ruta)
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        for elementos in lista_nuevo:
            print(elementos)
    except OSError:
        print("error en modulo os ")

funcion()