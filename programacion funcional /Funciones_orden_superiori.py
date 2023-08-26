
#funciones de orden superior

def funcion(lista , operacion):
    lista2 =[]
    for numeros in lista :
        ope = operacion(numeros)
        lista2.append(ope)
    return print(lista2)

def suma(numero):
    return numero + 2 
def multiplicacion(numero):
    return numero * 2

lista = [1,2,3,4]
numero = funcion(lista,suma) 
numero2 = funcion(lista , multiplicacion)

print(numero)
print(numero2)