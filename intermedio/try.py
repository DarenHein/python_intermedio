
#todo excepciones

def numero(a):
    print(a)
    

try :
    a = int(input("ingresa un numero : "))
    mostrar = numero(a)
except ValueError:
    print("te dije un numero pendejo")
finally :
    print("programa terminado gracias")