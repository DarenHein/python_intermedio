
#los diccionarios son colecciones de datos que la diferencai con las tuplas o listas estos tiene una llava para acceder a la informacion que se tiene asociada a ella llave 

diccionario = {
    "Luis":"tiene 30 años",
    "kevin":"es un pendejo",
    "kelly":"tiene 29 años"
}
#para acceder a un conteinido del diccionario tenemos que mandar a llamar ala llave y al diccioanrio que esta asociada 
print(diccionario) #imperime el contenido completo del diccionario 
amigos = diccionario["Luis"]
print(amigos) #accedermos solo a un elemento del diccionario 
diccionario["kevin"] = "es mas pendejo aun " #modificar contenido de un elemnto del diccionario 
del diccionario["Luis"] #eliminamos la informacion de un elemento del diccionario 
print(diccionario)

#todo imprimi la infromacion en for 

for nombres,llaves in diccionario.items():
    print(nombres,":",llaves)
    
