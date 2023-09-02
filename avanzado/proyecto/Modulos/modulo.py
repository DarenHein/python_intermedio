#login 
# dependiendo de quien entre tendra diferentes funcionalidades 
from Modulos.registro_entradas import base1
from Modulos.Registro import registro
import os 
nombre_adminitrador = "Luis"
contraseña_administrador = "5882"
def borrar(): 
     if os.name == "posix" : 
        os.system("clear")
     elif os.name == "nt" : 
        os.system("cls")
     
def login():
    print('''
##        #####    #####    ######  ##  ##
##       #######  #######   ######  ### ##
##       ##   ##  ##          ##    ######
##       ##   ##  ##  ###     ##    ######
##       ##   ##  ##   ##     ##    ## ###
#######  #######  #######   ######  ##  ##
######   #####    #####    ######  ##  ##
''')
    try : 
         nombre = input("-> Ingresa tu nombre -> ")
         if nombre == "r" or nombre == "R" :
             registro()
         if nombre != nombre_adminitrador :
              borrar() 
              login()
         else : 
              contra = input("-> Ingresa la contraseña -> ")
              if contraseña_administrador != contra :
                  borrar()
                  login()
              else : 
                  borrar()
                  base1(nombre,contra,"Admin")
    except ValueError : 
         print("-> caracteres invalidos")
    
