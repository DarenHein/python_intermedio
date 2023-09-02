
#tambien hay una exepcion en pywhatkit 
import pywhatkit as kit

try:
    kit.search("perros cafes")
    pass
except kit.exception.InternetException : 
    print("no se puede conectar")

'''
hay exepciones en python que son de gran ayuda para manejoar este framework 
'''