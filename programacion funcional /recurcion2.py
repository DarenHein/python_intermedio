#recurcion en python 
# la recurcion es como un bucle pero con funciones 
# en pocas palabras hacemos que la funcion se llame asi misma las veces qeu sea necesario hasy cumplir el objetivo 

def ovejas(numero): #creamos la funcion 
    if numero == 0 : #indicamos un condicional para porder realizar la recurcion 
        print("te dormiste") #cuando acabe la recurcion 
    else : # en caso contrario 
        print(numero) #imprimimos el numero con fines mas visuales 
        return ovejas(numero - 1) #mandamos a llamar ala funcion y le descontamos uno apra que asi no sea infinita 
numero_de_ovejas = 100 #creamos una variable con la conatidad a mandar 
ovejas(numero_de_ovejas) # hacemos la intancia con la funcion y mandamos como parametro la cantidad 