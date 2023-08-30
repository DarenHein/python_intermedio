
#metodos para las cadenas 
# todo en python hay metodos que nos ayudan a mejorar la implementacion con cadenas de caracteres (string)

cadena = "CADENA EN MAYUSCULAS"
pregunta = cadena.islower() #-> pregunta si la cadena esta en minusculas devilvera un booleano 
print(pregunta) #-> devuelve un false 
print(cadena.lower())#-> convierte la cadena en minuscula

#! metodo 2 
cadena = "cadena en minusculas "
pregunta = cadena.isupper() #-> pregunta si al cadena esta en MAYUSCULAS 
print(cadena.upper()) #-> trasnforma la cadena en mayusculas 

#! metodo3 
cadena = "hola mundo" #-> trasnforma la primera letra de la cadena en mayuscula 
print(cadena.capitalize())#-> imprime Hola mundo

#! metodo 4 
cadena = "hola mundo" #-> trasnsfoma cada primera letra de la cadena a msyusculas 
print(cadena.title()) #-> devolvera Hola Mundo

#! metodo 5 
cadena = " hola mundo " #-> elimina los espacios al principio y al final de la cadena 
print(cadena.strip()) #-> devolvera hola mundo sin espacios 

#! metodo 6 
# este esta buenoo sepra las palabras y las vuelve una lista pero debemos indicar el indicador que sea como el seprador 
# este ejemplo ocupe una tipica ruta de pc / para seprar las cadenas pero 
# puede ser lo queremos como un espacio un punto etc 
cadena = "c/user/decargas"
lista = cadena.split("/") 
print(lista)

#! metodo 5 
# al contratio del split este junta una lista como una sola cadena 
lista = ["Luis" , "le" , "gusta" , "kelly"] 
cadena = " ".join(lista)
print(cadena) #-> devuelve luis le gusta kelly como cadena 

#!metodo 6 
# modifica o cambia una cadena que indiquemos por una nueva 
cadena = "Hola mundo "
remplazar = cadena.replace("Hola" , "Adios") #-> devuelve adios mundo 
print(remplazar)

#!metodo 7 
#devuelve la ubicaion donde inicia la sub cadena 
cadena = "hola mundo"
print(cadena.find("mundo"))