import random

#todo el modulo ramdom nos permite crear numeros aleatorios y otras funciones siguientes 

print(random.random()) #todo genera un numero decimal entrre 0 y 1 

print(random.randint(0,199)) #todo genera un numero aleatorio entre a y b entre dos numeros 

lista = ["Luis" , "kelly" , "kevin"] #todo genera un elemento en alaetorio en la lista 
print(random.choice(lista))

random.shuffle(lista)#todo desordena los elementos de una lista selccionada 
print(lista)