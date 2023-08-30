
# todo leer y crear una nota con funciones 

def leer():
    try :
        leer = open("nota.txt","r")
        contenido = leer.read()
        leer.close()
        return print(contenido)
        pass
    except FileNotFoundError:
        print("No se puede abrir la nota")
    pass
def escribir(archivo):
    try :
        escribir = open("nota.txt","a")
        contenido = escribir.write(archivo)
        escribir.close()
        return print("la nota se a escrito con exito ")
        pass
    except FileNotFoundError :
        print("no se puedo abrir la nota")
    pass

while True :
    print('''
1 escribir en la nota
2 leer la nota 
''')
    op = int(input("ingresa tu opcion : "))
    if op == 1 :
        mensaje = input("ingresa el mensaje en la nota ")
        mandar = escribir(mensaje)
        print(mandar)
    elif op == 2 :
        leer()

