import turtle

window = turtle.Screen()
turtle.bgcolor("yellow")
turtle.color("blue","lightblue")

turtle.pensize(5)

turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.pendown()

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(80)
turtle.right(180)
turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.right(180)
turtle.forward(80)
turtle.left(135)
turtle.forward(150)
turtle.right(45)
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

window.exitonclick()