import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

thomas = turtle.Turtle()

thomas.color((0,0,1))
gradient = 0

for x in range(0, 72):
    thomas.forward(200)
    thomas.left(180)
    thomas.forward(200)
    thomas.left(185)
    thomas.color((gradient + 1/72, 0, 1))
    gradient += 1/72

wn.exitonclick()
