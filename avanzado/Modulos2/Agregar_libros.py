#aqui se agregaran los libros 
import os 
def agregar(*args):
    # args[0] -> Titulo
    # args[1] -> año de creacion 
    # args[2] -> autor
    # args[3] -> unidades
    # args[4] -> hojas
    nombre_carpeta = args[0] + "_historial" 
    titulo = args[0]
    año_creacion = args[1]
    autor = args[2]
    unidades = args[3]
    hojas = args[4]
    try : 
        ruta = os.getcwd()
        nueva_ruta = os.path.join(ruta,nombre_carpeta)
        existe = os.path.exists(nueva_ruta)
        if existe : 
            print("Historial que intenta agregar ya existe en el sistema ")
            #aqui podemos que redireccione ala seccion en un modulo aparte que bsuque el libro 
        else : 
            os.mkdir(nombre_carpeta)
        pass
    except OSError : 
        print("Error en modulo Agregar")

    pass