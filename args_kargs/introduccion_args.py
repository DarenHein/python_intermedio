
# args nos sirve para ´pder mandar multiples variames como argumentos a un funcion los devolvera como tupla 

def funcion(*args):
    for elementos in args:
        print(elementos)

funcion("amarillo" , "azul" , "verde" , "rojo")
funcion(1,2,3,4,5)