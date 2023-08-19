import os 

nombre = "luis.txt" #viejo nombre 
newnombre = "kelly.txt" # nuevo nombre 

try :
    os.rename(nombre , newnombre) # pasamos como argumento el viejo nombre y el nuevo ombre 
    pass
except OSError :
    print("error")