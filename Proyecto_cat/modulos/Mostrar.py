# Mostrar las listas registradas 
import os
def mostrar():
    
    try:
        iterador = 1
        ruta = os.getcwd()
        lista = os.listdir(ruta)
        print("Ahora mostrarremos las listas que se tienen registradas ")
        cosa_fea = "modulos"
        cosa_fea2 = "main"
        if cosa_fea in lista :
            lista.remove(cosa_fea)
        if cosa_fea2 in lista :
            lista.remove(cosa_fea2)
        if "reque" in lista:
            lista.remove("reque")
        for i in range(len(lista)):
            lista[i] = os.path.splitext(lista[i])[0]
        for listas in lista:
            print(iterador,"-> ",listas)
            iterador += 1 
        try :
            opcion = int(input("Deseas modificar alguna \n1 si \n2 no \n Digita tu opcion -> "))
            if opcion == 1 :
                ingresar_nota()
            else : 
                print("ok")
            pass
        except ValueError :
            print("Ingresa solamante numeros ")
    except OSError :
        print("Error de tipo os ")
        
def ingresar_nota():
   try :
        nombre = input("Ingrese el nombre de la nota que deseas modificar -> ")
        nombre_sin_espacios = nombre.strip()
        nombre_extencion = nombre_sin_espacios + ".txt"
        ruta = os.getcwd()
        ruta_completa = os.path.join(ruta,nombre_extencion)
        existe = os.path.exists(ruta_completa)
        if existe : 
            try :
                leer = open(nombre_extencion , "r")
                leer2 = leer.readlines()
                print("La Tarea es :  \n" , leer2 )
                abrir = open(nombre_extencion,"w")
                nueva_tarea = input("Ahora ingresa la nueva tarea -> ")
                fecha = input("Ingresa la nueva fecha de cumplimiento -> ")
                juntar = nueva_tarea + "\n" + fecha
                abrir.write(juntar)
            except FileNotFoundError:
                print("Por alguna razon no se puede abrir el archivo")
        else :
            pass
    
   except OSError:
       print("Error en Modulo Os")