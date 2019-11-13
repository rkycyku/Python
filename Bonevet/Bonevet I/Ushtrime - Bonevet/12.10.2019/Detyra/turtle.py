import turtle

wn = turtle.Screen()
wn.bgcolor("black")

lapsi = turtle.Turtle()
lapsi.color("red")
lapsi.pensize(3)

lapsi.forward(150)
lapsi.left(90)
lapsi.forward(150)
lapsi.left(90)
lapsi.forward(150)
lapsi.left(90)
lapsi.forward(150)

lapsi.penup()
lapsi.forward(150)
lapsi.pendown()
lapsi.forward(100)
lapsi.left(90)
lapsi.forward(150)
lapsi.left(90)
lapsi.forward(100)
lapsi.left(90)
lapsi.forward(150)

wn.exitonclick()