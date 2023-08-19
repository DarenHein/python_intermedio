import os 

try :
    print("busquda de archivo")
    nombre = input("ingresa el nombre -> ")
    extencion = input("ingresa la extencion -> ")
    ruta_relativa = nombre + extencion
    ruta = os.path.abspath(ruta_relativa)
    existe = os.path.exists(ruta)
    if existe :
        print(f"el arichivo existe y se encueuntra en {ruta}")
    else :
        print("el archivo no existe")
    pass
except OSError :
    print("Error")