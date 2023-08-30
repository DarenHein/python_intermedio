# a) Define una función llamada 'area_circulo' que calcule el área de un círculo.
# La función debe recibir el radio como argumento y retornar el área.

def area_circulo(radio):
    area = 3.1416 * (radio*radio)
    return area

# b) Calcula y muestra el área de un círculo con radio 5.
print(area_circulo(5))