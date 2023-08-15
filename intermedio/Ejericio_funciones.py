'''
Supongamos que quieres calcular el área de un rectángulo. Puedes escribir una función que tome el ancho y la altura como argumentos, realice el cálculo y devuelva el área. Luego, puedes llamar a esa función con diferentes valores para obtener diferentes áreas de rectángulos.

'''
#funcion 
def area(a,b):
    resultado2 = (a * b)/2
    return resultado2
#main
print('''

Programa que calcula el area de un triangulo 

''')
altura = float(input("ingresa la altura : "))
base = float(input("ingresa la base : "))
resultado = area(altura,base)
print("el resultado es : " , resultado)
