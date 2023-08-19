'''
vamos a crear un ejericio que sea un ruleta rusa con un archivo de txt si cae en cierto numero elimina el arichivo si no lo vuelve a intentar 
'''
import os 
import random
def creacion(): 
    try :
        crear = open("Luis.txt" , "w")
        crear.write("voy a morir ")
        pass
    except FileNotFoundError :
        print("no se peude crear el arichivo ")

# todo main 
salvadas = 0 
perdidas = 0 
bandera = True
print("Ruleta rusa de un arichivo")
try :
    ruta = os.getcwd()
    print("nos encontramos en = " , ruta )
    nombre = input("ingresa el nombre del archivo que deseas buscar : ")
    nuevo_nombre = nombre+".txt"
    nueva_ruta = os.path.join(ruta,nuevo_nombre)
    existe = os.path.exists(nueva_ruta)
    if existe :
        print("El archivo existe")
        while bandera :
            numero = random.randint(1,5)
            if numero == 1 or numero == 2 or numero == 3 or numero == 4 :
                print("te salvaste perro")
                bandera = True
                salvadas += 1 
            else :
                os.remove(nuevo_nombre)
                print("perdiste")
                perdidas += 1 
                bandera = False 
        pass
    else : 
        print("el archivo no existe")
    pass
except OSError as e:
    print(e)
finally :
    print(f'''
salvadas = {salvadas}
perdidas = {perdidas}

''')
