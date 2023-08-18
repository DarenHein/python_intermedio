import os 

nombre = "luis.txt"
newnombre = "kelly.txt"

try :
    os.rename(nombre , newnombre)
    pass
except OSError :
    print("error")