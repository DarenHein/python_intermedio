'''
Escribe un programa en Python que realice lo siguiente:

Crea una lista de calificaciones llamada calificaciones con al menos 10 calificaciones (pueden ser números enteros).
Calcula el promedio de las calificaciones en la lista.
Cuenta cuántos estudiantes han aprobado (calificación mayor o igual a 60) y cuántos han reprobado (calificación menor a 60).
Imprime la lista de calificaciones, el promedio, el número de estudiantes aprobados y el número de estudiantes reprobados.
'''
calificaiones = [10,20,30,40,44,12,50,60]
tamaño = len(calificaiones)
print(tamaño)
kevins = 0 
aprobados = 0 
for cali in calificaiones:
    if cali >= 60 : 
        aprobados += 1
    elif cali < 60  :
        kevins += 1
print("Aprobados : " , aprobados)
print("kevins : " , kevins)

