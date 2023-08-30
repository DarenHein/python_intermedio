import turtle
import random

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("white")

# Crear el objeto Turtle para el tallo
stems = turtle.Turtle()
stems.shape("square")
stems.color("green")
stems.shapesize(stretch_wid=15, outline=None)

# Crear el objeto Turtle para los pétalos
petals = turtle.Turtle()
petals.shape("circle")
petals.color("red")
petals.speed(0)

# Función para dibujar un pétalo
def draw_petal():
    petals.penup()
    petals.goto(random.randint(-100, 100), random.randint(0, 100))
    petals.pendown()
    petals.begin_fill()
    for _ in range(6):
        petals.forward(50)
        petals.right(60)
    petals.end_fill()

# Animación
for _ in range(12):
    draw_petal()

stems.penup()
stems.goto(0, -180)
stems.pendown()

# Cierra la ventana al hacer clic
wn.exitonclick()
