import turtle

window = turtle.Screen()
turtle.bgcolor("yellow")

turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("blue")

for i in range(5):
    turtle.forward(150)
    turtle.right(144)

turtle.end_fill()

window.exitonclick()


