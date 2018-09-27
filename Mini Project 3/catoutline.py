# We are creating an outline of a cat using turtle library.

import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

thomas = turtle.Turtle()

# drawing head
thomas.circle(150)
thomas.penup()
thomas.left(90)
thomas.forward(250)
thomas.left(90)
thomas.forward(111)
thomas.right(90)

# drawing left ear
thomas.pendown()
thomas.forward(110)
thomas.right(130)
thomas.forward(110)

thomas.left(40)
thomas.penup()
thomas.forward(60)

# drawing right ear
thomas.pendown()
thomas.left(40)
thomas.forward(110)
thomas.right(130)
thomas.forward(120)

thomas.penup()
thomas.forward(120)
thomas.left(100)

# drawing whiskers
thomas.pendown()
thomas.forward(150)
thomas.penup()
thomas.right(110)
thomas.forward(70)
thomas.pendown()
thomas.right(90)
thomas.forward(140)

# drawing other whiskers
thomas.penup()
thomas.left(10)
thomas.forward(220)
thomas.pendown()
thomas.left(10)
thomas.forward(145)
thomas.penup()
thomas.right(110)
thomas.forward(70)
thomas.pendown()
thomas.right(90)
thomas.forward(140)

# drawing left eye
thomas.penup()
thomas.setheading(45)
thomas.forward(80)
thomas.pendown()
thomas.circle(25)

# drawing right eye
thomas.penup()
thomas.setheading(0)
thomas.forward(90)
thomas.pendown()
thomas.circle(25)

# drawing nose
thomas.penup()
thomas.setheading(210)
thomas.forward(60)
thomas.setheading(180)
thomas.pendown()
thomas.forward(20)
thomas.setheading(300)
thomas.forward(15)
thomas.setheading(45)
thomas.forward(15)
thomas.setheading(210)
thomas.penup()
thomas.forward(10)
thomas.setheading(270)
thomas.forward(10)

# drawing mouth
thomas.pendown()
thomas.forward(25)
thomas.setheading(210)
thomas.forward(25)
thomas.setheading(30)
thomas.penup()
thomas.forward(25)
thomas.pendown()
thomas.setheading(330)
thomas.forward(35)

wn.exitonclick()
