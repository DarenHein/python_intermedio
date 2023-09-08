# INTRODUCCION ALA LIBRERIA ZIPFILE QUE CREA ARCHIVOS ZIP 
# EN ESTE EJERICIO VERREMOS COMO CREAR Y AGREGAR ELEMENTOS AL ARICHIVO ZIP 
import zipfile #* IMPORTAMOS LA LIBRERIA 
nombre_del_arichivo = "mi_primer_zip.zip"#todo le damos un nombre a nuestro arichivo zip 
#todo abrimos como si fuera una nota 
archivo = zipfile.ZipFile(nombre_del_arichivo , "w")
#todo ingresamo archivos al zip 
archivo.write("hola.txt",arcname="1.txt") #! arcname es el nombre de como estara dentro del arichivo zip 
#todo cerramos el flujo de datos 
archivo.close()
