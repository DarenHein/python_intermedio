
#todo lectura de datos 

try :
    leer = open("hola.txt","r")
    contenido = leer.readline() #todo linea uno 
    contenido2 = leer.readline() #todo linea dos 
    contenido3 = leer.readline() #todo linea tres
    print(contenido)
    print(contenido2)
    print(contenido3)
    leer.close
except FileNotFoundError :
    print("no se peude abrir el archivo ")
finally :
    print("programa finalizado")