'''
Crea una aplicación de línea de comandos para gestionar una lista de tareas. Permite agregar, eliminar y mostrar tareas.
'''
tareas =[]
flag = True
while flag :
    print("\n")
    print("Gestor de tareas")
    print('''
1 agregar tareas 
2 eliminar tareas 
3 mostrar tareas 
4 salir 

''')
    op = int(input("Seleccione su opcion "))
    if op == " ":
        print("opcion invalida")
    elif op == 1 : 
        print("Agregar tarea")
        tarea_agregada = input("Ingresa la tarea agregar : ° ")
        if tarea_agregada == " ":
            print("inavalido")
        else :
            tareas.append(tarea_agregada)
            print("Tarea agregada correctamente")
    elif op == 2 :
        if not tareas:
            print("no hay tareas registradas alctualmente ")
        else :
            for tarea in tareas:
                print("Tarea : " , tarea)
                op2 = int(input("deseas eliminar esta tarea 1 si no 2 "))
                if op2 == "" :
                    print("tarea no seleccioanda")
                    break
                elif op2 == 1 : 
                    print("eliminar tarea seleccionada : " , tarea )
                    tareas.remove(tarea)
                    print("tarea eliminadda con exito")
                elif op2 == 2 :
                    print("ok mostramos la siguiente tarea")
                    continue
    elif op == 3 :
        if not tareas:
            print("no hay tareas registradas")
        else :
            print("Mostrar tareas")
            for tarea in tareas:
                print("Tarea : ° ",tarea)
    elif op == 4 : 
        flag = False 
    else :
        print("opcion invalida")
        