class Padre:
    def __init__(self,nombre,apellido):
        self.nombre = nombre 
        self.apellido = apellido
    def caracteristicas(self):
        print(f"Mi nombre es {self.nombre } y mi epllido es {self.apellido}")
class Hija(Padre):
    def __init__(self, nombre, apellido, hobbi):
        super().__init__(nombre, apellido)
        self.hobbi = hobbi
    def caracteristicas(self):
        super().caracteristicas()
        print(f" mi hobbir es {self.hobbi}")
obj = Padre("luis","manjarrez")
obj.caracteristicas()
obj2 = Hija("Zelda" , "Manjarrez","leer")
obj2.caracteristicas()
