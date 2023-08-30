'''
Desarrolla un programa el cual nos permita conocer todos los números pares que se encuentren dentro del rango de de x y y.

El programa debe cumplir con los siguiente requerimientos.

Definir una función llamada rango_pares.
La función debe poseer dos parámetros, x y y.
la función debe recibir como argumentos los valores para x y y.
siendo x un número positivo mayor a 0 dado por el usuario.
siendo y un número positivo mayor a x dado por el usuario.
La función debe retornar una lista con todos los números pares que existan entre el rango x y y.
Para probar el programar puedes pedir los valores de x y y al usuario vía teclado. Los valores deben ser pedidos fuera de la función.
'''

def rango_pares(x): 
    if x % 2 == 0 : 
        return x

lista = [1,2,3,4,5]
pares = list(map(rango_pares,lista))
for elementos in pares : 
    if elementos == None:
        pares.remove(elementos)
    else : 
        pares.append(elementos)

for elementos in pares: 
    print(elementos)