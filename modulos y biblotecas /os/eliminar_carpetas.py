import os 
#todo eliminar carpetas vacias

ruta = os.getcwd()
nombre = "Luis"
nueva_ruta = os.path.join(ruta,nombre)
try :
    os.rmdir(nueva_ruta)
    pass
except OSError :
    print("No se peude eliminar ")