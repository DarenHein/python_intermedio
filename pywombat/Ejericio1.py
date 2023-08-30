'''
Una de las operaciones básicas en matemáticas es sin duda calcular el área de un Circulo. Es por ello que en esta ocasión será necesario que crees un programa el cual nos permita conocer el área de un circulo dado su radio. El programa debe cumplir con los siguientes requerimientos.

El usuario debe ser capaz de ingresar (vía teclado) el radio del circulo.
El programa podrá calcular el área del circulo mediante el radio ingresado por el usuario.
El programa podrá aceptar un radio con o sin punto decimal.
El programa debe mostrar en consola, con el siguiente mensaje: El área del circulo es: x, el resultado dela operación.
Ejemplo.

Ingresa el radio del circulo: 8.5
El área del circulo es: 226.9800692218775

'''
def area_circulo(radio): 
    radio = float(radio)
    pi = 3.1415 
    resultado = pi * (radio**2)
    redondeo = round(resultado,2)
    return print("El area del circulo es : " , redondeo)

print("area de un circulo")
try : 
    radio = input("Ingresa el radio -> ")
    print("Radio ingresado -> " , radio)
    area_circulo(radio)
except ValueError : 
    print("Solo ingresa numeros porfavor ")