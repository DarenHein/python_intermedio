
#framework date time 
import datetime #-> importamos la bibloteca 

tiempo = datetime.datetime.now() #saca la fecha hora en tiempo real 
print(tiempo)

# si solo ocupamos el año mes o dia o segundo 
print(tiempo.year) #-> daca el año 
print(tiempo.month)#-> saca el mes 
print(tiempo.hour) #-> saca la hoara 
print(tiempo.minute) #-> saca el minuto 
print(tiempo.second)#-> saca el sedundo exacto 
