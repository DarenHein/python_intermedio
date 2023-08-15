'''

## Ejercicio: Clase de Cuenta Bancaria
Crea una clase llamada `CuentaBancaria` que represente una cuenta bancaria básica. La clase debe tener los siguientes atributos y métodos:
### Atributos:
- `titular`: El titular de la cuenta (cadena).
- `saldo`: El saldo actual de la cuenta (número).
### Métodos:
1. `__init__(self, titular, saldo_inicial)`: Constructor que inicializa el titular y el saldo inicial de la cuenta.
2. `depositar(self, cantidad)`: Método que recibe una cantidad positiva y la suma al saldo de la cuenta. Debe imprimir un mensaje indicando el depósito exitoso o que la cantidad no es válida.
3. `retirar(self, cantidad)`: Método que recibe una cantidad positiva y la resta del saldo de la cuenta, siempre y cuando haya suficiente saldo disponible. Debe imprimir un mensaje indicando el retiro exitoso o que la cantidad no es válida.
4. `obtener_saldo(self)`: Método que retorna el saldo actual de la cuenta.
Crea una instancia de la clase `CuentaBancaria`, realiza algunas operaciones de depósito y retiro, y muestra el saldo actual después de las operaciones.
---
¡Ahora es tu turno! Intenta resolver el ejercicio por ti mismo. Si tienes alguna pregunta o necesitas ayuda, estaré aquí para ayudarte.
'''
class CB:
    def __init__(self,saldo,titular):
        self.saldo = saldo
        self.titular = titular
    def deposito(self,saldo_retiro):
       saldo_str = int(self.saldo)
       saldo_retiro2 = int(saldo_retiro)
       saldo_final = saldo_str - saldo_retiro2
       return print("El saldo actual es de : " , saldo_final)
         
       pass
    def retiro(self,saldo_retiro):
         if self.saldo == "" :
            print("no se puede sacar dinero probre ")
         else :
             saldo_final = self.saldo - saldo_retiro
             return print("el saldo actual es de : $" ,saldo_final )
            
#main
print("banco los pobres")
bandera = True
while bandera : 
    print('''
1 sacar dinero 
2 ingresar dinero 
3 salir 
''')     
    op = int(input("Ingresa tu opcion :") )
    if op == 1 :
        try :
            print("ingresa el salfo a retirar :")
            dinero = int(input("$ : "))
            obj = CB("","")
            obj.retiro(dinero)
        except ValueError :
            print("no se acepta caracteres ingresa un numero valido ")
        pass
    elif op ==2 :
        print("Ingresa la cantidad que deseas depositar ")
        dinero = float(input("$ :"))
        obj = CB("","")
        obj.deposito(dinero)

        pass 
    elif op == 3 :
        print("adios")
        bandera = False
    else :
        print("opcion incorrecta")     