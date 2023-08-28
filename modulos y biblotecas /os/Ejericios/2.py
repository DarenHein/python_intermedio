
# para poderse mover entre carpetas principales como 
# documentos y dscargas por que momento soolo lo are asi 
# proyecto starship v1 
import os 
import shutil
def funcion():
    iterador = 0
    descargas = "/Users/luismanjarrezcarbajal/Downloads"
    print("\n")
    print("\nMenu Principal")
    print('''
Lee las opciones y escoje la de tu agrado  -> 
          
          1 -> Documentos
          2 -> Descargas
''')
    opcion = int(input("Ingresa el numero al directorio desea ir -> "))
    print("\n")
    if opcion == 1 : 
        pass 
    elif opcion == 2 : 
        ruta = descargas 
        lista = os.listdir(ruta)
        for elementos in lista : 
            print("-> ",iterador , elementos)
            iterador += 1 
        print("")
        nombre = input("ingresa el nombre del arichivo mas su extencion -> ")
        print("")
        nueva_ruta = os.path.join(ruta,nombre)
        lista2 = os.listdir(nueva_ruta)
        for elementos in lista2 : 
            print("->",iterador,elementos)
            iterador += 1 

while True : 
    print('''

  #####   ######     ##     ######    #####   ##   ##   ####    ######
 ##   ##  # ## #    ####     ##  ##  ##   ##  ##   ##    ##      ##  ##
 #          ##     ##  ##    ##  ##  #        ##   ##    ##      ##  ##
  #####     ##     ##  ##    #####    #####   #######    ##      #####
      ##    ##     ######    ## ##        ##  ##   ##    ##      ##
 ##   ##    ##     ##  ##    ##  ##  ##   ##  ##   ##    ##      ##
  #####    ####    ##  ##   #### ##   #####   ##   ##   ####    ####



''')
    funcion()
    