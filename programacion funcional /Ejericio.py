
#Dada una lista de palabras, crea una nueva lista con la longitud de cada palabra.

lista = ["Luis" , "kelly" , "adobo"]
cantidad = list(map(lambda x : len(x) , lista))
print(cantidad)