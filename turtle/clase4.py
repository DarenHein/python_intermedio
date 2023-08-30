import turtle

ventana = turtle.Screen()
ventana.title("colores")
ventana.bgcolor("black")

tortu = turtle.Turtle()
tortu.color("orange")
tortu.forward(100)
tortu.left(90)
tortu.forward(200)

ventana.exitonclick()

#el metodo color nos permite cambiaer el color de la tortuga  a nuestro antojo  
# tambien podemos poner por un rango de rgb mi_tortuga.color(0.2, 0.7, 0)