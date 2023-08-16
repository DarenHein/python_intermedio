
#todo encapsulamiento en metodos 

class Persona :
    def __init__(self,nombre , edad , cuenta):
        self.nombre = nombre 
        self.edad = edad 
        self.cuenta = cuenta
        pass
    def publico(self):
        print("hola soy publico")
        self.__privado()
    def __privado(self):
        print(self.cuenta)
        print("soyprivado")
obj = Persona("luis" , 30 , 12345)
obj.publico()

#todo la unica forma de acceder a un metodo privado es llmarlo desde otro metodo 
