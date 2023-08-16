class Perro :
    def __init__(self,nombre , edad , raza ):
        self.nombre = nombre 
        self.edad = edad 
        self.raza = raza 
    def mostrar_mascota(self):
        print(f"El nombre de mi amscota {self.nombre} Su edad es de {self.edad} y su raza es {self.raza}")