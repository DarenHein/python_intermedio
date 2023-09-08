#pdb es una herrramienta de depuracion que nos sirve para saber el estado de nuestro codigo apra detectar errores 
import pdb; #primero importamos libreria 

def suma(a,b):
    resultado = a+b
    pdb.set_trace() #aqui pausamos la ejecuacuin de nuestro codigo para ver que esta pasando 
    print("EL resultado de la suma es " , resultado)

suma(4,5)
nombre = input("Ingresa tu nombre ")
pdb.set_trace()
print(nombre)

'''
comandos mas usados en pdb 
n -> para avabzar ala siguiente linea de codigo 
c -> para continuar al siguiente punto de control 
q -> para salir del depurador 
p variable -> para imprimir el valor de la variable indicada 

ESTE TEMA ES IMPORTANTE PARA PODER HACER PRUEBAS DE NUESTRO SOFTWARE 

aunque hay otros metodos que se pueden combianr con esto 
como  imprimir las variables con print(para saber que pasa en el codigo ) 
uso de try except 

'''