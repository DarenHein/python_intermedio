'''
creacion de carpteas en python 

'''
import os
nombre = "luis"
try:
    creacion = os.mkdir(nombre)
    print("carpeta creadda con exito")
    pass
except FileExistsError:
    print("carpeta con el mismo nombre")
finally :
    print("adios")
