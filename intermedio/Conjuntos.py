
#conjuntos en python son una colaccion de fatos unicos en python no puede haber duplicados 

# como se declararan 
conjunto = {"Luis" , "kelly" , "adobo"}
# o 
conjuntos = set(["Luis" , "Kelly" , "adobo"])
# en lo personal me gusta mas la primera 

#OPERACIONES BASICAS EN CONJUNTOS 

#agregar conjuntos 
conjunto.add("axel")
print(conjunto)

#eliminar elementos del conjunto 
conjunto.remove("adobo")
print(conjunto)

#verifificar si en un conjunto existe algo 
if "axel" in conjunto: 
    print("existe el puto del axel")
else : 
    print("no existe el puto del axel")

#-> operaciones con conjuntos 
#-> une dos conjuntos solo que omite los duplicados y solo deja uno 
conjunto1 = {1,2,3,4}
conjunto2 = {4,5,6}
# cimbolo de la operacion "|"
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

#inserction 
#-> encunetra elementos duplicados en ambos conjuntos y es lo que muestra 
# simbolo & 
conjunto4 = conjunto1 & conjunto2
print(conjunto4)

#diferencia 
#encuentra los elementos que se encuentran en un conjunto pero no el el otro 
# no es lo mimos conjunto - conjunto2 a 
# conjunto2 - conjunto 
conjunto5 = conjunto1 - conjunto2
conjunto6 = conjunto2 - conjunto1
print(conjunto1)
print(conjunto2)

#transformar listas y tuplas a conjuntos 

lista= [1,2,3,4]
tupla = (1,2,3,4)
conjuntoL = set(lista)
conjuntot = set(tupla)
print(conjuntoL) 
print(conjuntot)

#recorrer datos con un for 
# como los conjuntos son desorndenados siempre saldran en orden difentes 
for elementos in conjuntoL:
    print(elementos)

#notas 
'''
los conjuntos son deserdenados asi que no podemos acceder por indicies a ellos 
se ocupan para eliminar duplicados en listas 
'''