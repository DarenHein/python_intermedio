def generadora(start, stop):
    for numeros in range(start,stop +1 ):
        yield numeros

generador = generadora(1,10)
for numeros in generador:
    print(numeros)

'''
en este ejemplo simplificamos la generadora en ves de poner la palabra reservda yield yield yield en cada elemento podemos ocupar el bucle for apra optimizar la rapizas ala hora de escribir codigo 
'''