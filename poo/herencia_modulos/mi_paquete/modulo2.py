from mi_paquete.modulo1 import Persona
class Hija(Persona):
    def __init__(self, nombre, apellido, hobbie):
        super().__init__(nombre, apellido)
        self.hobbie = hobbie
    def mostrar(self):
        super().mostrar()
        print(f"El hobbir es {self.hobbie}")
