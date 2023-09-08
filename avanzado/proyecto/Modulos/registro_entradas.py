#aqui ira cunatas veces el usuario entra en la app 
# si es ad es usuario 
# User es ususario 
import os 
import datetime
def crearBase(*args):
    #args[0] noombre 
    # argas[1] contraseña 
    # args[2] tipo 
    # argas[5] ultima fecha 
    try :
        ruta = os.getcwd()
        print(ruta)
        nombre = args[0] + "_registro"
        juntar = os.path.join(ruta,nombre)
        print(juntar)
        existe = os.path.exists(juntar)
        if existe : 
            nuevo_nombre = args[0] + ".txt"
            mandar_contraseña = "Contraseña : "+args[1] 
            mandae_nombre = "Administrador : " + args[0]
            mandar_hora = "Hora Ingresada : " + args[2]
            os.chdir(juntar)
            escribir = open(nuevo_nombre,"a")
            escribir.write("\nRegistro : \n"+mandae_nombre + "\n" + mandar_contraseña + "\n" + mandar_hora +"\n-------------------------\n")

        else : 
            print("la ruta no existe")

    except OSError:
        print("error encontrado en os")
    pass



def base1(*args):
    # args[0] usuario
    # argas[1] contraseña 
    # argas[2] tipo de usuario 
    try : 
        nombre = args[0]
        contra = args[1]
        tipo = args[2]
        now = datetime.datetime.now()
        tiempo = str(now)
        ruta = os.getcwd()
        nombre_carpeta = nombre+"_registro"
        ruta_completa = os.path.join(ruta,nombre_carpeta)
        existe = os.path.exists(ruta_completa)
        if existe : 
            pass
            crearBase(nombre,contra,tiempo)
        else : 
            os.mkdir(ruta_completa)

        pass
    except OSError : 
        print("Error en la creacion del archivo")