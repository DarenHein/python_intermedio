
#todo las funciones lambda tambien se pueden mandar como argumento 

lista = [1,2,3,4,5]
calcular = list(map(lambda x : x + 1 , lista))
print(calcular)

'''
que estamos haciendo 
1 -> creamos una lista 
2 -> creamos otra lista ese lista agregamos el metodo map creamos una mini funcion que haga una suma del argumento mas 1 y le mandamos la lista como argumento para que aplique la mini funcion en cada elemento de lsita y a su ves la almacene en la lista nueva llamada calcular 
'''