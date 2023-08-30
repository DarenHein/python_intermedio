
#la recursividad es cunado una funcion se llama asi misma 
#hasta cumplir una tarea en especifico 


def funcion(a):
    if a == 100 :
        print("llegamos a a ")
    else : 
        print(a)
        a += 1 
        funcion(a) 
        

funcion(1)
    