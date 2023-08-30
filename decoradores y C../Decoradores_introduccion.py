'''
En resumen, los decoradores te permiten extender o modificar el comportamiento de una función sin tener que cambiar su código original. 

'''
def decorador(funcion_original):
    def funcion_decorada():
        print("hola antes de decorar")
        funcion_original()
        print("funcion despues de decorar")
    return funcion_decorada

@decorador
def invitado():
    print("me van a decorar")

invitado()



