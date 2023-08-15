
#todo escribir en una nora txt 

mensaje = "hola desde python"
mensaje2 = "\nhola desde python sin eliminar"

# todo w = sobreescribir en la nota osea elimina lo que se encuentra en la nota 
# todo a = proviene de apend sirve para agregar sin eliminar en la nota 

nota = open("hola.txt","a")
#todo nota = open("hola.txt","w")
nota.write(mensaje2)
nota.close