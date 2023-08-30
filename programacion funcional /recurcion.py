
#recurcion en python : 
#la recuercion la ocupamos para evitar bucles en python 
#hacemos que ua funcion se llame a si misma veces hasta cumplir el objetivo 

def recu(a):
    if a == 1 :
        print("se acaba")
    else : 
        return recu(a-1)

numero = recu(10)
print(numero)