'''
**Ejercicio 1: Contar Vocales**
Escribe una función que cuente el número de vocales (mayúsculas y minúsculas) en una cadena dada.
'''
def contador(palabra):
    cantidad = len(palabra)
    mayus = 0 
    minus = 0
    for letras in palabra:
        if letras.isupper() : 
            mayus += 1 
        else : 
            minus += 1 
    print("Palabra :" , palabra)
    print("cantidad de caracteres : ", cantidad)
    print("cantidad de mayusculas : " ,mayus)
    print("cantidad de minusculas : " , minus)

palabra = input("ingresa una palabra -> ")
contador(palabra)
