def despedir(x):
    if x >= 0 : 
        print("adios mundo")
        x = x -1 
        despedir(x)

    pass 

def saludar(x): 
    if x >= 0 : 
        print("hola mundo")
        x = x - 1
        saludar(x)
        if x == 0 : 
            x += 10 
            despedir(10)

cantidad = 10
saludar(cantidad)