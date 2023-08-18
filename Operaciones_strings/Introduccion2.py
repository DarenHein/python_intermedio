
#todo upper() , lower()

cadena = "hola mundo"
cadena_mayusculas = cadena.upper() # trasnfroma a muayusculas 
cadena_minusculas = cadena.lower() #trasnfroma a minusculas 
print(cadena_mayusculas)
print(cadena_minusculas)

#todo strip() , lstrip() , rstrip() 

cadena = "   hola mundo "
cadena_corregida = cadena.strip() #elimina los espacios inesesarios del comienso 
print(cadena_corregida) 

#todo split() 
frase = "esto es una oracion "
frase_convertida = frase.split() #trasnforma una string a lista 
print(frase_convertida)
print(type(frase_convertida))

#todo join()
lista = ["hola" , "mundo"] 
cadena = " " . join(lista)# convierte una lista en cadena 
print(cadena)

# todo replace
texto = "Python es genial"
nuevo_texto = texto.replace("genial", "increíble")  # "Python es increíble" cuando vea la aplara genial la cambiara por la palabra increible 
