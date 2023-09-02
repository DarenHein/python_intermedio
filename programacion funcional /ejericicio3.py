#Dada una lista de números, tu tarea es crear una nueva lista que contenga el doble de cada número en la lista original utilizando programación funcional.

lista = [1,2,3,4]
nueva_funcion = list(map(lambda x : x**2 , lista))
print(nueva_funcion)