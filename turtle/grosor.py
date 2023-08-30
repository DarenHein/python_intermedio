#cambair el grosot de la pluma 
import turtle

ventana = turtle.Screen()
ventana.title("grosor")
ventana.bgcolor("black")

tortu = turtle.Turtle()
tortu.color("orange")
tortu.forward(100)
tortu.penup()
tortu.backward(100)
tortu.left(90)
tortu.forward(50)
tortu.right(90)
tortu.pendown()
tortu.pensize(3)
tortu.forward(100)
ventana.exitonclick()

#el metodo size crea el aunmenta el grsor de el trazo de la tortuga 