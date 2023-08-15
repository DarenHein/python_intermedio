
class perro: #todo clase 
    def __init__(self,nombre,edad) : #todo constructor de la clase 
        self.nombre = nombre 
        self.edad = edad
        pass
    def saludar(self): #todo metodo de la clase 
        print("mi nombre es " , self.nombre , " y tiene " , self.edad) 

mi_perro = perro("luis",27) #todo mandamos a llamr ala clase y le mandamos dos parametros 
mi_perro.saludar()#todo con el objeto creado podemos ocuapr los metodos de la clase 
