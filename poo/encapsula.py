class Perro :
    def __init__(self,nombre ,edad , raza ):
        self.nombre = nombre #todo atributo publico
        self._edad = edad #todo atributo semi_privado 
        self.__raza = raza #todo atributo privado 
obj = Perro("luis",20,"callejero")
print(obj.nombre) #todo nos deja acceder 
print(obj._edad) #todo tambien nos deja acceder 
# print(obj.__raza) #todo nos marcara error
# TODO TAMBIEN SE PUEDE ACCEDER A ALOS ATRIBUTOR PROIVADOS PERO ES UN POCO MAS DIFICIL 
print(obj._Perro__raza) #todo asi accedemos alas atributos privados 