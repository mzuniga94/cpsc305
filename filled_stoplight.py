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

thomas.begin_fill()
thomas.circle(50)
thomas.end_fill()

sheldon.begin_fill()
sheldon.circle(50)
sheldon.end_fill()

veronica.begin_fill()
veronica.circle(50)
veronica.end_fill()

wn.exitonclick()
