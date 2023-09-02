
# isalpha nos ayuda verificar si un dato recibido as albabetido o no 
# devuelve true si es alfabetico 
# devuelve false si no 

letra = "a"
numero =  "5"
print(letra.isalpha())
print("5".isalpha())

#si le mandamos caracteres aunque sea numero en str manda false 
# si mandammos un int o float mandara error 

cadena = "hola mundo"
print(cadena.isalpha())

#hasta los espacios los manda como false 

cadena = "hola"
print(cadena.isalpha())