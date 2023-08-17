#hacer sonidos 
class Animal:
    def sonidos():
        pass
class Perro(Animal):
    def sonidos(self):
        return "gua"
lista = [Perro()]
for animales in lista :
    print(animales.sonidos())