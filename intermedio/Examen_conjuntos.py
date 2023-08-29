
#pregunta dos 
conjunto = set([1,2,3,4])
conjunto2 = set([4,5,6,7])
conjunto3 = conjunto & conjunto2
print(conjunto3)
#pregunta 3 
cadena = "Hola"
cadena = cadena.replace("H","*")
print(cadena)
#pregunta 4 
cadena = "Luis come chettos"
lista = cadena.split(" ")
print(lista)
#pregunta 5 = yth
#pregutna 6 esa nome la se 
cadena = " hola "
cadena  = cadena.strip()
print(cadena)
#pregunta 7 
conjunto = set()
#pretunfat 8 
conjunto2 = set([1,2,3])
conjunto = set(conjunto2)
print(conjunto2.issubset)
#pregunta 9 
cadena = "LUIS"
cadena = cadena.lower()
print(cadena)

'''
Dado un conjunto de palabras: palabras = {'hola', 'mundo', 'python', 'programación'}, escribe un programa en Python que itere sobre el conjunto de palabras y genere una nueva lista con las palabras que tienen más de 5 caracteres.

'''
conjunto = set(["hola" , "mundo" , "python" , "programacion"])
lista = []
for elementos in conjunto:
    tamaño = len(elementos)
    if tamaño >= 5 : 
        lista.append(elementos)
for elementos in lista:
    print(elementos)
