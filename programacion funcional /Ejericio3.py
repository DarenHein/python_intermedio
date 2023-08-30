#Dada una lista de precios, utiliza map() y lambda para incrementar cada precio en un 10%.

precios = [10,20,30,40]
porcentajes = list(map(lambda x : ((x/10) * 100) , precios))
print(porcentajes)

