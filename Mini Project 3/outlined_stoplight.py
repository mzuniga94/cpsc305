import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

thomas = turtle.Turtle()
sheldon = turtle.Turtle()
veronica = turtle.Turtle()

thomas.color((1, 0, 0))
sheldon.color((1, 1, 0))
veronica.color((0, 1, 0))

thomas.penup()
thomas.sety(150)
thomas.pendown()

veronica.penup()
veronica.sety(-150)
veronica.pendown()

thomas.circle(50)
sheldon.circle(50)
veronica.circle(50)

wn.exitonclick()
