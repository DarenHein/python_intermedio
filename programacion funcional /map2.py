
#todo la funcion map es uno de los pilares de la programacion funcional 
# este recibe una funcion como argumento y una estructura de control aplica la funcion a cada uno de los elementos d la funcion 

def suma(x): 
    return x + 1 

lista = [1,2,3,4]
calcular = list(map(suma,lista))
print(calcular)

