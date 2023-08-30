
#Dada una lista de frases, utiliza map() y lambda para crear una nueva lista que contenga las mismas frases en mayúsculas.

lista = ["hola" , "adios" , "ayer"]
lista2 = list(map(lambda x : x.upper() , lista))
print(lista2)