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
thomas.right(300)
thomas.forward(80)
thomas.pendown()
thomas.circle(25)

#right eye
thomas.penup()
thomas.right(-300)
thomas.forward(80)
thomas.pendown()
thomas.circle(25)

#nose
thomas.penup()
thomas.right(120)
thomas.forward(60)
thomas.pendown()
thomas.right(60)

wn.exitonclick()
