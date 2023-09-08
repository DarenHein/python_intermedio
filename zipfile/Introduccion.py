
# todo introduccion zipfile de python 
#todo libreria de python que ayuda con la comprecion de datos en python 
# todo puede crear y extraer datos de un zip 

import zipfile #todo importamos la libreria 

nombre_archivo = "comprimir.zip" #todo nombre del archivo con su extencion 

zip = zipfile.ZipFile(nombre_archivo,"w") #todo creamos el archivo y seleccionamos la opcion de escritura = "w"

zip.write("hola.txt",arcname="hola.txt") #todo indicamos el archivo que deseamos comprimir y el nombre que tendra dentro de el zip arcname 

zip.close() #todo cerramos el flujo de datos 
