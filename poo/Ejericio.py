'''
Crea una clase llamada Libro que represente un libro en una biblioteca. Los libros tienen un título, un autor y una cantidad de copias disponibles. Implementa métodos para prestar y devolver un libro, y para obtener la información del libro.

'''
class Libro:
    def __init__(self,nombre,autor,copias,año):
        self.__nombre = nombre 
        self.__autor = autor 
        self.__copias = copias 
        self.__año = año
    def prestar (self):
        if self.__copias < 0 :
            print("ya no hay libros ")
        else : 
            print(f"libros disponibles son  {self.__copias}" )
obj = Libro ("el llano en llamas " , "Gael G.M" , 12 , 1999)
obj.prestar()