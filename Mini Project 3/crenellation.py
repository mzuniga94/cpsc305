import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

thomas = turtle.Turtle()

thomas.left(180)
thomas.penup()
thomas.setx(-400)
thomas.pendown()
thomas.left(180)

#left, right, right, left
for x in range(0, 20):
    thomas.forward(20)
    thomas.left(90)
    thomas.forward(20)
    thomas.right(90)
    thomas.forward(20)
    thomas.right(90)
    thomas.forward(20)
    thomas.left(90)

wn.exitonclick()
