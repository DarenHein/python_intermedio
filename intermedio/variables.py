#variables globales en python 
#las variables gloabales en python son un variable que tiene acceso a todo el programa 

#nota importante si se decea modificar la variable global dentro de una funcion necesitamos declarar el global dentro de la funcion que valla a modificar la variable local 

variable_global = 10 

def funcion():
    global variable_global
    variable_global = 2 
    print(variable_global)

print(variable_global , "aqui vale 10 ")
funcion() # aqui vale 2  oir que se modifico dentro de la funcion