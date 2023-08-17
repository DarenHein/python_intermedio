class Persona :
    def __init__(self,nombre,apellido):
        self.nombre = nombre 
        self.apellido = apellido
        pass
    def mostrar(self):
        print(f"mi nombre es : {self.nombre}" )
        print(f"mi epllido es {self.apellido}")
        