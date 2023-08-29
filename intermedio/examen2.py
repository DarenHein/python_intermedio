#pregunta 1 -> los datos inmutables son las tuplas 
#pregunta 2 -> 
frutas = {'manzana': 5, 'plátano': 2, 'naranja': 3}
print(frutas['manzana'])
#pregunta 3 -> lista.append("elemento")
lista = []
lista.append("luis")
#pregunta 4 -> el metodo join()
lista2 = ["hola","como" , "estas"]
cadena = " ".join(lista2)
print(cadena)
#pregunta 5 
cadena = "hola mundo"
print(cadena.upper())
#pregunta 6 
#que es una tupla 
#datos ordenados e inmutable 
#pregunta 7 
tupla = ()
#pregunta 8 
diccionario = {"Luis":12,"kelly":2}
del diccionario["Luis"]
print(diccionario)
#pregunta 9 
cadena = "hola"
tamaño = len(cadena)
print(tamaño)
# Pregunta 10 
lista = ["luis" , "Kevin" , "axel " , "kelly"]
ultimo = lista[-1]
print(ultimo)

'''
Supongamos que tienes una lista de nombres: nombres = ['Ana', 'Juan', 'María', 'Carlos']. Escribe un programa en Python que itere sobre la lista de nombres y cree un diccionario donde las claves sean los nombres y los valores sean la longitud de cada nombre.
'''

nombre = ["ana" , "juan" , "maria" , "carlos"]
diccionario = {}
for personas in nombre:
    tamaño = len(personas)
    diccionario[personas] = tamaño
print("diccionario terminado")
for llave , valor in diccionario.items():
    print(llave,":",valor)
    