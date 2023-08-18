
# todo hay varias operaciones con string 
#! concatenacion 
palabras = "Hola" + "Mundo"
#! replicacion 
asteristicos = "*" * 10 
print(asteristicos) #todo mustra 10 asteriscos
#! Identaxion y segmentacion 
cadena = "Palabra"
print(cadena[0]) #todo muestra "P"
print(cadena[1]) #todo muestra "A"
# todo es tomas cada letra como si fuera una array 
#! format 
nombre = "Luis"
edad = 30 
mensaje = "mi nombre es {} mi edad es {} ".format(nombre , edad )
print(mensaje)
#! F-strings 
nombre = "kelly"
print(f"sot {nombre} y soy un raton ")
#! quitar decimales 
numero = 3.1415
print(f"el numero es {numero :.2f}")