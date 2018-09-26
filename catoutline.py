import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

thomas = turtle.Turtle()

#no color yet bc outline is black

#head
thomas.circle(150)
thomas.penup()
thomas.left(90)
thomas.forward(250)
thomas.left(90)
thomas.forward(111)
thomas.right(90)

#left ear
thomas.pendown()
thomas.forward(110)
thomas.right(130)
thomas.forward(110)

thomas.left(40)
thomas.penup()
thomas.forward(60)

#right ear
thomas.pendown()
thomas.left(40)
thomas.forward(110)
thomas.right(130)
thomas.forward(120)

thomas.penup()
thomas.forward(120)
thomas.left(100)

#whiskers
thomas.pendown()
thomas.forward(150)
thomas.penup()
thomas.right(110)
thomas.forward(70)
thomas.pendown()
thomas.right(90)
thomas.forward(140)

#other whiskers
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

#left eye
thomas.penup()
thomas.setheading(45)
thomas.forward(80)
thomas.pendown()
thomas.circle(25)

#right eye
thomas.penup()
thomas.setheading(0) # sets the direction of the turtle object
thomas.forward(90)
thomas.pendown()
thomas.circle(25)

#nose
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

#mouth
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
