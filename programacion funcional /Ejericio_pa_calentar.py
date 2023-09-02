'''
Dado una lista de números, realiza los siguientes pasos utilizando programación funcional:

Utiliza map() para elevar al cuadrado cada número en la lista.
Utiliza filter() para seleccionar solo los números pares de la lista.
Utiliza reduce() para encontrar la suma de todos los números en la lista resultante de paso 
'''
 
from functools import reduce #importamot para ocupar el reduce 
lista = [1,2,3,4] #creamos la lista 
nueva_lista = list(map(lambda x : x**2 , lista)) #elevamos al cuadrado con el metodo map y una funcion lambda 
print(nueva_lista)
nueva_lista2 = list(filter(lambda x : x % 2 == 0, nueva_lista ))#filtramos los numeros pares con filtrer para ue no devuelve none y lo almacenamos en una nueva lista 
print(nueva_lista2)
nueva_lista3 = reduce(lambda x , y : x +y , nueva_lista2) #reducimos la lista con un reduce y una funcion lambda que sume los numeros que se encuentran en la lista y lo almacenamos en una variable 
print(nueva_lista3)