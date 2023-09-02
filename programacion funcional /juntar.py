#Dada una lista de números, tu tarea es calcular la suma de los cuadrados de los números impares utilizando programación funcional. Para ello, primero aplica un cuadrado a los números impares y luego suma los resultados.

from functools import reduce 

def suma_inpares(x,y):
    return x + y 

def reduce1(x): 
    if not x % 2 == 0 : 
        return x  

lista = [1,2,3,4]
nueva_lista = list(map(lambda x : x**2 , lista))
print("Doble de cada elemnto -> " , nueva_lista)
nueva_lista_inpares = list(filter(reduce1,nueva_lista))
ultimo_elemento = reduce(suma_inpares,nueva_lista_inpares)
print("resultados")
print(f"la lista orginal {lista}")
print(f"lista de los nuemros inpares {nueva_lista_inpares}")
print(f"suma de la lista de los inpares el ultimo numero es -> {ultimo_elemento}")

