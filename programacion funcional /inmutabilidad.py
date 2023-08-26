
#la inmutabilidad en python es no modificar los datos creados si no crear uno nuevos para no crear paralelislmos 

lista = ["luis" , "kelly "]

for personas in lista:
    print(personas)

nueva_lista = lista + ["kevin"]

for personas in nueva_lista:
    print(personas)