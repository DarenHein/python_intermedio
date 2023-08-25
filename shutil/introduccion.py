
#introduccion ala libreria shutil 
import shutil #importamos 
import os #importamos os para obtener rutas de acceso etx 

try:
    ruta = os.getcwd()
    lista = os.listdir(ruta)
    print(lista[0])
    unir = os.path.join(ruta,lista[0])
    ruta_destino = "/Users/luismanjarrezcarbajal/Downloads/python/shutil/carpeta/"
    shutil.move(unir,ruta_destino)
    pass
except OSError as e : 
    print(e)

#todo lo que hace este sript es mover un archivo a una caeprta lo que aun no etniendo es como puedo ontener la ruta relativa de una carpeta 