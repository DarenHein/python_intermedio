
#todo la funcion filtrer es una funcion que filtra de un conjunto de elementos los necesatios y los decurleve a un conjunto mas pqueño 

def par(x): 
    if x % 2 == 0 : 
        return x 

lista = [1,2,3,5]
lista2 = list(filter(par,lista))
print(lista2)