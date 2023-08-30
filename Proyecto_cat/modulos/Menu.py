from modulos.Agregar import agregar
from modulos.Buscar import buscar
from modulos.Eliminar import eliminar
from modulos.Mostrar import mostrar
def menu():
    bandera = True 
    while bandera :
        print("Lista de tareas")
        print('''
1 Agregar 
2 Buscar 
3 Ver tareas
4 eliminar 
5 Salir 

''')
        try :
            opcion = int(input("Ingresa la opcion deseada -> "))
            if opcion == 1 :
                nombre_tarea = input("Ingresa el nombre de la tarea a gardar -> ")
                tarea = input("ingresa la tarea ")
                dia = input("ingresa el dia limite a cumplir la tarea ")
                if nombre_tarea == "" or tarea == "" or dia == "":
                    print("campos sin llenar")
                else :
                    agregar(nombre_tarea,tarea,dia)
                pass
            elif opcion == 2 :
                nombre_a_buscar = input("Ingresa el nombre de la Tarea qu estas buscando -> " )
                if nombre_a_buscar == "" :
                    print("Nombre incompleto o erroneo")
                else :
                    buscar(nombre_a_buscar)
                pass 
            elif opcion == 3 :
                mostrar()
                pass 
            elif opcion == 4 : 
                eliminar()
            elif opcion == 5 :
                bandera = False 
            else :
                print("opcion invalida ")
            pass
        except ValueError :
            print("Opcion invalida intenta otra vez")
