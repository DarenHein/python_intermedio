'''
el poliformismo es como la sobrescritura de metodos 
una clase padre tiene sus metodo este metodo tiene un nombre es emetodo puede ser ocuado por la clase hija 
asi de sencillo es el polimorfismo 
'''

class Animal:
    def hacer_sonidos(self):
        pass
class Perro(Animal):
    def hacer_sonidos(self):
        return "Guauf"
class Gato(Animal):
    def hacer_sonidos(self):
        return "miua"
class Vaca(Animal):
    def hacer_sonidos(self):
        return "moo"
animales = [Perro() , Gato() , Vaca()]
for animalitos in animales :
    print(animalitos.hacer_sonidos())