'''
Supongamos que tienes una lista de calificaciones de un estudiante y quieres calcular su promedio. Puedes escribir una función que tome la lista de calificaciones como argumento, calcule el promedio y lo devuelva. Luego, puedes llamar a esa función con diferentes conjuntos de calificaciones.

'''
def calcular_calificaciones(lista,cantidad):
    iterador = 0 
    for i in lista:
        iterador = iterador + i 
    resultado = iterador/cantidad
    return resultado
    
lista = [10,9,8,7,5,6]
cantidad = len(lista)
promedio = calcular_calificaciones(lista,cantidad)
print("el resultado es : ", promedio)