'''
Dado un número entero n, escribe una función llamada sum_even_numbers que calcule la suma de todos los números pares desde 2 hasta n (incluyendo n si es par). Luego, llama a esta función con el valor 10 e imprime el resultado.
'''
def sum_even_numbers(n):
    contador = 0 
    contador2 = 0 
    for numeros in range (n) :
        if  numeros % 2 == 0 :
            contador = contador + numeros
        else :
            contador2 = contador2 + numeros 
    return print("la suma de los numeros pares es : " , contador ,"\nLa suma de los numeros inpares es : ",contador2)
    pass

try :
    while True :
        num = int(input("ingresa un numero : "))
        resultado = sum_even_numbers(num)
        print(resultado)
    pass
except ValueError :
    print("No se a ingresado un numero correcto")