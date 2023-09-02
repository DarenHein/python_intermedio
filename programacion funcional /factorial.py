#calcular el factorial de un numero con recursion 

def factorial(x):
    if x == 0 or x == 1 : 
        return x 
    else : 
        return x * factorial(x-1)
resultado = factorial(5)
print(resultado)
