import turtle

ventana = turtle.Screen()
ventana.title("mover ala tortuga")
ventana.bgcolor("white")

tortu = turtle.Turtle()
tortu.forward(100) #mover hacia delante 
tortu.backward(30) #mover hacia atras 
tortu.left(90) #mueve ala izquierda el aprametro son grados no pixeles 
tortu.forward(200)
tortu.right(75) #mover en grados ala izquierda 
tortu.forward(100)
ventana.exitonclick()

# se pasa como parametros la cantidad de pixeles 
# rigth y lefth son para mover ala tortuhga tantos grados como parametros mandemos 
