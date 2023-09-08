
#lectura de archivos zip 

import zipfile #todo importamos la libreria 

nombre = "comprimir.zip" #todo ponemos el nombre del archivo que deseamos leer por dentro 
zf = zipfile.ZipFile(nombre,"r") #todo creamos el objeto y mandamos como aprametro el nombre y el modo en este caso lectura "r"
lista = zf.namelist() #todo creamos una lista y le asginamos el meto namelist paar que regrese todosno los nomrbres de los archivos dentro del zip 

for elementos in lista : #todo imprimimos los archivos 
    print(elementos)

zf.close() #todo cerramos el fluko de datos 