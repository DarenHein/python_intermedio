# a) Abre el archivo 'mi_archivo.txt' en modo escritura y escribe "Hola, mundo!" en él.

def crear():
    try :
        escritura = open("hola.txt" , "w")
        escritura.write("Hola mundo")
        escritura.close()
    except FileNotFoundError :
        print("no se peude abrir el archivo ")

# b) Abre el archivo nuevamente en modo lectura y muestra su contenido.

def Leer():
    try :
        lectura = open("hola.txt" , "r")
        leer = lectura.read()
        print(leer)
        lectura.close()
    except FileNotFoundError :
        print("no se puede abrir el arichivo ")
    
crear()
Leer()
