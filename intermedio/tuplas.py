
#las tuplas son colecciones de datos en python 

#creacion de una tupla 
tupla = ("Luis" , 2  ,"kelly")
otra_tupla = "luis" , 2, "kelly" #las 2 formas son validas apra las tuplas 

#sacar elementos 
nombre = tupla[0] #devuelve "Luis"

#tamaño de la tupla 
tamaño = len(tupla)

#nota tambien tiene desempaquetado de variables las tuplas 
a,b,c = tupla
#a-> devuelve luis
#b-> devuelve 2
#c-> devuelve kelly

#saber cuantas veces se rpite un elemto en una tupla 
repite = tupla.count("Luis")
print(repite)

#saber el indice donde se encuentra el valor 
saber = tupla.index("Luis")
print(saber)

#todo las tuplas se ocupan cunado sabemos que los datos no cambiaran nunca siempre se mantendran 

#tuplas anidadas 
# podemos juntar mas tuplas en una sola o combianarlas con listas y diccionarios 

tupla2 = (
    "Luis",[1,3,4],
    "kelly",[1,3,4]
)
print(tupla2[0]) #solo acceeder al primer elemento 
#ocuapmaos desempaquetado de variables para la lista que esta anidada 
matematicas , español , ingles = tupla2[1]
print(matematicas)
print(español)
print(ingles)
#recorrido de una tupla con for 
for elementos in tupla2:
    print(elementos)
