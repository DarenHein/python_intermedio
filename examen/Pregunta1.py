# a) Crea una variable 'num1' con el valor 25 y 'num2' con el valor 7.
num = 25
num2 = 7 
# b) Calcula la suma, resta, multiplicación y división de num1 y num2.
suma = num + num2 
resta = num + num2 
multipli = num * num2 
try :
    divi = num / num2 
    pass 
except ZeroDivisionError :
    print (" no se puede dividir entre cero ")

# c) Imprime los resultados.
print(suma)
print(resta)
print(multipli)
print(divi)
