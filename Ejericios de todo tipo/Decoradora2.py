
#Decoradora pasando multiples parametros 

def decoradora(funcion_original):
    def agregar(*args):
        print("Empieza la suma de los numeros : ")
        funcion_original(*args) #pasar simpre el argas en la funcion original 
        print("a terminado la suma de ambos numeros ")
    return agregar
        
@decoradora
def suma(*args):
    numero = args[0]
    numero2 = args[1]
    resultado = numero + numero2
    print("resultado : " , resultado)

numero = int(input("ingresa un numero "))
numero2 = int(input("ingresa un numero "))
suma(numero,numero2)
