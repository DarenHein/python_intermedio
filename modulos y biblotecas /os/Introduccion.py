
# todo el modulo os nos ayuda a que nos progrmas puedan trabajar con  nuestro sistema operativo 
import os 

print(os.getcwd()) #nos devuelve la direccion actual donde nos encontramos 
ruta = os.getcwd()
lista = os.listdir(ruta) #todo ve lo que esta en la ruta indicada y lo devuelve como lista 
print(lista)
print(lista[0])
#os.chdir() 
#todo cambia la ruta de trabajo desde este puto asia abajo ocuapremos eotra ruta 
try :
    nombre = "Luis"
    ruta_completa = os.path.join(ruta,nombre)
# todo os.path.join() junta dos rutas en este caso creamos una carpeta y la juntamos ala ruta que ya teniamos antes 
    os.mkdir(ruta_completa) #todo creamos la carpeta 
except OSError :
    print("carpeta ya existe ")