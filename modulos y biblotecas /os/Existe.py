
#todo verificar si un arichivo exite en nuestra pc 
import os 
try :
    ruta = os.getcwd()
    print(ruta)
    nombre = "Luis.txt"
    nueva_ruta = os.path.join(ruta,nombre)
    existe = os.path.exists(nueva_ruta)
    if existe :
        print("el archivo existe")
    else : 
        print("el arichivo no existe")

    pass
except OSError :
    print("error")