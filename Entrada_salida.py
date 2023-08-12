
#todo entrada y salida de datos en python 
#todo ahora veremos la lectura de un archivo de txt en python 

try:
    leer = open("hola.txt","r")#todo abrimos la nota con open indicamos el nombre y r para read (leer)
    contenido = leer.read() #lee todo el documento 
    contenido2 = leer.readlines() #lee el codumento y lo devuelve como lista 
    contenido3 = leer.readline()#lee solo la primera liena 
    pass 
except FileNotFoundError :
    print("no se puede abrir el arichivo")
finally :
    print("programa finalizado gracias")