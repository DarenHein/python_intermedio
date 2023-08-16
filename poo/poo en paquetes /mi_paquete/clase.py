class Persona :
    def __init__(self,nombre ,edad ,sexo):
        self.__nombre = nombre 
        self.__edad = edad
        self.__sexo = sexo 
    def mostrar_persona(self):
        print(f"El nombre de la persona es {self.__nombre} , La edad es {self.__edad} el sexlo de la persona es {self.__sexo}")
