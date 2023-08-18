'''
Supongamos que tienes un archivo en la carpeta "documentos" en tu computadora. Pero para acceder a él, necesitas saber dónde está esa carpeta en tu sistema de archivos. os.path.abspath(ruta) te proporciona la ubicación precisa de esa carpeta para que puedas llegar al archivo correctamente.

'''
import os
nombre = "kevin"
try :
    rutaabs = os.path.abspath(nombre)
    print("aqui se encuntra = " , rutaabs)
    pass
except OSError :
    print("Error")