
#Ejericio con decoradoras 

def decoradora(funcion_original):
    def aumentar_saludo():
        print("dia soleado")
        funcion_original()
    return aumentar_saludo
@decoradora
def hola():
    print("hola")

hola()