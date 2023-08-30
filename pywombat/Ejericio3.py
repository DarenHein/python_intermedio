#Escribir una función que tome una lista de palabras como argumento y devuelva una lista con las palabras que tienen una longitud de más de 5 caracteres.

def contador(palabras): 
    resultado = len(palabras)
    return print("la palabra contiene -> " , resultado, " caracteres ")

try : 
    palabra = input("Ingresa una palbra ")
    sin_espacios =  palabra.strip()
    contador(sin_espacios)
    pass
except ValueError: 
    print("Solo caracteres abc")
