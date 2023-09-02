# repaso de las minifunciones lambda 

funcion = lambda x : x**5
lista = [1,2,4,5]
resultado = list(map(funcion,lista))
print(resultado)

#o tmabien 

lista = [1,2,3]
resultado = list(map(lambda x : x**2 , lista) )
print(resultado)