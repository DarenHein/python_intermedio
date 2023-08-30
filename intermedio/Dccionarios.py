
#diccionarios 
# coleciones de datos como las tuplas y listas a diferencias de las ultimas dos esta va por clave:valor 
#en python para acceder a un valor necesitamos la llave 
#son mutables que pueden modificarse en el transucsro del programa 

#creacion del diccioanrio

diccionario = {
    "luis":"30 años",
    "kelly":"29 años"
}

#acceso a valores 
print(diccionario["luis"]) #imprime el dato -> "30 años"
#modificacion de datos 
diccionario["luis"] = "ahora tiene 31 años"
print(diccionario["luis"]) #imprime ahora tiene 31 años 
#creacion de nueva llave 
diccionario["kevin"] = "es un pendejo"
print(diccionario["kevin"])#imprime es un pendejo 
#eliminar elementos del diccioanrio 
del diccionario["kevin"] #necesitamos la clave del diccionario 
# otros medoso ocupados 
lista = diccionario.keys() # devuelve una lista con las claves del diccionario 
print(lista)
lista2 = list(diccionario.keys()) #trasnformar a lista 
print(lista2)
#ahora los valores en una lista 
lista3 = diccionario.values()
print(lista3)
#trasnfromar a lista los valores de el diccioario 
lista4 = list(diccionario.values())
print(lista4)

#ahora a tupla la firecincia es que ara una tupla con clave y valor 
tupla = diccionario.items()
print(tupla)
for clave ,valor in diccionario.items():
    print(clave , ":" , valor)
