import os
def eliminar():
    try :
        print("Eliminar de la lista")
        iterador = 1 
        ruta = os.getcwd()
        lista = os.listdir(ruta)
        cosa_fea = "modulos"
        cosa_fea2 = "reque"
        if cosa_fea in lista:
            lista.remove("modulos")
        if cosa_fea2 in lista:
            lista.remove("reque")
        for i in range(len(lista)):
            lista[i] = os.path.splitext(lista[i])[0]
        for modulos in lista:
            print(iterador,"->",modulos)
        print("\n")
        nombre = input("Ingresa el nombre del elemento a eliminar -> ")
        nombre_mas_extencion = nombre + ".txt"
        juntar = os.path.join(ruta,nombre_mas_extencion)
        existe = os.path.exists(juntar)
        if existe :
            try : 
                opcion2 = int(input("Seguro que deseas eliminar este arichivo \n 1 si \n 2 no \nPor que una vez eliminado no se puede recuperar -> "))
                if opcion2 == 1 :
                    os.remove(nombre_mas_extencion)
                else : 
                    print("ok")
                pass
            except ValueError : 
                print("Solo se admiten numeros")
        else :
            print("no existe el archivo")

        pass
    except OSError :
        print("Erro en el modulo os ")
    