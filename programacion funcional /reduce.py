# tema reduce 
#reduce en python lo que hace es que toma una funcion y un conjunto de elementos(lista) y va tomando de dods en dos para hacer una operacion 
from functools import reduce

def suma(a,b):
    return a + b 

lista = [1,2,3,4,5]
'''
que es lo que hace : 
1+2 = 3 
        3 + 7 = 10 y al final 10 + 5 = 15 resultado final 
3+4 = 7 

'''
nueva_lista = reduce(suma,lista)
print(nueva_lista) #imprime -> 15 