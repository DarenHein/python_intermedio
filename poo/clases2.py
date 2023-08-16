class Perro :
    def __init__(self,nombre ,edad ):
        self.nombre = nombre 
        self.edad = edad 
    def Saludar(self):
        print(f"{self.nombre} , se llama mi perrito ")
    def Edad(self):
        self.edad += 1
        print(self.edad)

obj = Perro("Luis" , 12 )
obj.Edad()
obj.Saludar()
