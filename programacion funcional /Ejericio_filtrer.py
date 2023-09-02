#Dada una lista de palabras, tu objetivo es filtrar y obtener una nueva lista que contenga solo las palabras que tengan una longitud mayor que un valor dado.

def longitud(palabra): 
    tamaño = len(palabra)
    if tamaño > 5 : 
        return palabra

palabras = ["manzana" , "arroz" , "carne" , "ojo"]
nueva_lista = list(filter(longitud,palabras))
print(nueva_lista)
    