'''
Escribe una función recursiva que calcule la suma de los primeros N números naturales. Por ejemplo, la suma de los primeros 5 números naturales sería 1 + 2 + 3 + 4 + 5 = 15.

numero = 0 
i = 1 
while i <= 5 :
    numero = numero + i
    print(numero)
    i = i + 1
'''
acumulador = 0 
def suma(n):
    global acumulador 
    if n == 0 : 
        print(acumulador)
    else : 
        acumulador += n
        suma(n-1)
suma(5)

        



