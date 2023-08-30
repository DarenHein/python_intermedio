
#todo metodo readlines 
# todo recibe la noyta y la trasnforma en lista 

try :
    leer = open("hola.txt","r")
    contenido = leer.readlines()
    leer.close
    print(type(contenido))
    for lectura in contenido:
        print(lectura)
    pass
except FileNotFoundError :
    print("no se puede abrir un arichivo")
finally :
    print("programa finalizado")