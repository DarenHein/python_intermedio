# el map nos ayuda a la modifcacion de grandes cantidades de datos 

def multiplicar(numero):
    return numero * 2

lista = [1,2,3,4,5,6,7]
nueva_lista = list(map(multiplicar , lista))
print(nueva_lista)