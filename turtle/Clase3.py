
#levantar y poner la tortuga
import turtle

ventana = turtle.Screen()
ventana.title("hola")
ventana.bgcolor("white")

tortu = turtle.Turtle()
tortu.forward(200)
tortu.left(90)
tortu.forward(100)
tortu.left(90)
tortu.forward(100)
tortu.penup()
tortu.forward(200)
tortu.pendown()

ventana.exitonclick()

#penup -> levanta la pluma en el ultimo lugar donde se quedo la tortuga 
#pendown -> naja la pluma 
#aqui subimos la pluna y despues la bajamos 200 pixeles mas adelante 