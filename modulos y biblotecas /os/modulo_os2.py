
# eliminar elementos con os 
import os 
ruta = os.getcwd() 
print(ruta)
arichivo_eliminar = "Luis.txt"
nueva_ruta = os.path.join(ruta,arichivo_eliminar)
try :
    os.remove(nueva_ruta)
except OSError :
    print("no se puede eliminar")