# a) Escribe un bucle for que imprima los números pares del 1 al 10 (inclusive).

for numero in range(1,11,1):
    print(numero)

# b) Escribe un condicional que determine si un número ingresado por el usuario es positivo, negativo o cero.
num = int(input("Ingresa un numero :"))
if num > 0 :
    print("el numero es positivo ")
elif num == 0 :
    print("el numero es cero ")
else :
    print("el numero es negativo ")