'''
**Parte 1: Cadenas**

1. Escribe un código que tome una cadena como entrada y devuelva la longitud de la cadena (número de caracteres).

2. Convierte la siguiente cadena a mayúsculas: `"Hola, esto es un ejemplo."`.

3. Dada la siguiente cadena: `"python es genial"`, convierte la primera letra en mayúscula.

4. Escribe un código que tome una cadena con espacios al principio y al final y la devuelva sin esos espacios.

**Parte 2: Tuplas**

5. Crea una tupla que contenga los números del 1 al 5.

6. Accede al tercer elemento de la siguiente tupla: `(10, 20, 30, 40, 50)`.

7. Crea una tupla con tres elementos: tu nombre, tu edad y tu ciudad.

**Parte 3: Diccionarios**

8. Crea un diccionario que represente información sobre una película. Debe incluir claves como `"titulo"`, `"año"`, `"director"` y `"genero"`.

9. Accede al valor asociado con la clave `"año"` en el diccionario de la pregunta anterior.

10. Agrega una nueva clave `"actor_principal"` con el nombre de un actor al diccionario de la pregunta 8.
'''
cadena = "hola mundo"
longitud = len(cadena)
print(longitud)
cadena = "hola esto es un ejemplo"
print(cadena.upper())
cadena = "python es genial"
print(cadena.capitalize())
cadena = " hola mundo "
print(cadena.strip())
#parte dos 
tupla = (1,2,3,4,5)
print(tupla)
tupla = (10,20,30,40,50)
print(tupla[3])
tupla = ("Luis" , 30 , "Mexico")
print(tupla)
#parte 3 
diccionario = {
    "pelicula" : "El exorcista",
    "año" : "1970",
    "director" : "Luis",
    "genero" : "terror"
}
print(diccionario["año"])
diccionario["actor"] = "Luis"
for clave , valor in diccionario.items():
    print(clave , ":" , valor )