class Vehiculo:
    def __init__(self,marca,precio):
        self.marca = marca 
        self.precio = precio 
    def caracteristicas(self):
        print(f"El vehiculo es de la marca {self.marca} y Tiene un coste de {self.precio} ")
class Audi(Vehiculo):
    def __init__(self,marca , precio , color ):
        super().__init__(marca,precio)
        self.color = color 
    def caracteristicas(self):
        print(f"color {self.color}")
        super().caracteristicas()
obj = Vehiculo("Audi" , "1234")
obj.caracteristicas()
obj2 = Audi("audi" , "Rojo" , "123456")    
obj2.caracteristicas()
    