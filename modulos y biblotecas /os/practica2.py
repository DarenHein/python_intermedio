import os 
try :
    extencion = ".py"
    extencion2 = ".txt"
    nombre = input("ingresa el nombre del archivo a buscar : ")
    nombre_extencion = nombre + extencion
    nombre_extencion2 = nombre + extencion2
    nueva_ruta = os.path.abspath(nombre_extencion)
    nueva_ruta2 = os.path.abspath(nombre_extencion2)
    existe = os.path.exists(nueva_ruta)
    existe2 = os.path.exists(nueva_ruta2)
    if existe :
        print(f"el arichivo existe y se encuentra en {nueva_ruta}")
    else :
        print(f"el arichivo no existe {nombre_extencion}")
    if existe2 :
        print(f"el archivo se encuentra en {nueva_ruta2}")
    else :
        print(f"El archivo no existe {nombre_extencion2}")
    

except OSError :
    print("error")