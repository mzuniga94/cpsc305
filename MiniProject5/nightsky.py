#Programmers: Oli Patane, Matthew Zuniga

import random
import turtle

# This function draws the entire night sky using turtle turt.
def draw_sky(turt):

    # draw 200 random stars, one by one
    for speck in range(200):

        # choose random x and y coordinates
        # TODO: you need to rewrite these statements to generate coordinates
        # over the entire window, not just near the origins
        x = random.randrange(-400, 400)
        y = random.randrange(-400, 400)

        # choose random star type; first generate an integer between
        # 0 and 99 inclusive

        percent = random.randrange(0, 99)
        # TODO: now use if statement(s) on percent, to decide whether to
        if percent <= 40:
            blue_star(turt, x, y)
        elif percent >= 55 and percent < 88:
            red_star(turt, x, y)
        elif percent >= 88:
            big_star(turt, x, y)


# Draw a small blue star at x, y, using turt.
def blue_star(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(random.uniform(0.71, 1), random.uniform(0.87, 1), 1)
    turt.begin_fill()
    turt.circle(random.uniform(0.1, 2))
    turt.end_fill()

# Draw a medium-sized red star at x, y using turt.
def red_star(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(1, random.uniform(0.67, 1), random.uniform(0.70, 1))
    turt.begin_fill()
    turt.circle(random.uniform(1.5, 3.5))
    turt.end_fill()

# Draw a large four-pointed star at x, y using turt.
def big_star(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(1, 1, 1)
    turt.begin_fill()
    turt.forward(20)
    turt.left(160)
    turt.forward(20)
    turt.left(20)
    turt.forward(20)
    turt.left(160)
    turt.forward(20)
    turt.left(100)
    turt.end_fill()
    turt.begin_fill()
    turt.forward(3.47)
    turt.right(90)
    turt.forward(3.7)
    turt.left(120)
    turt.forward(15)
    turt.left(150)
    turt.forward(15)
    turt.left(30)
    turt.forward(15)
    turt.left(150)
    turt.forward(15)
    turt.end_fill()

# Draw yellow moon and city skyline
def draw_embellishment(turt):
    turt.goto(-300, 300)
    turt.color("yellow")
    turt.begin_fill()
    turt.circle(25)
    turt.end_fill()
    turt.penup()
    turt.color("white")
    turt.pendown()
    turt.penup()
    turt.goto(-400, -400)
    turt.pendown()

    #Begin drawing cityline
    #Begin building 2
    turt.begin_fill()
    turt.forward(25)
    turt.setheading(90)
    turt.forward(75)
    turt.setheading(0)
    turt.forward(50)
    turt.setheading(270)
    turt.forward(35)

    #Begin building 2
    turt.setheading(0)
    turt.forward(50)
    turt.setheading(90)
    turt.forward(75)
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(45)
    turt.forward(25)
    turt.setheading(90)
    turt.forward(20)
    turt.setheading(0)
    turt.forward(20)
    turt.setheading(270)
    turt.forward(20)
    turt.setheading(315)
    turt.forward(20)
    turt.setheading(0)
    turt.forward(25)

    #Begin building 3
    turt.setheading(270)
    turt.forward(75)
    turt.setheading(0)
    turt.forward(50)
    turt.setheading(90)
    turt.forward(50)
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(270)
    turt.forward(50)

    #Begin building 4
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(45)
    turt.forward(50)
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(90)
    turt.forward(25)
    turt.setheading(0)
    turt.forward(10)
    turt.setheading(270)
    turt.forward(25)
    turt.setheading(315)
    turt.forward(50)

    #Begin building 5
    for i in range(1, 5):
        turt.setheading(0)
        turt.forward(25)
        turt.setheading(90)
        turt.forward(25)
    turt.setheading(90)
    turt.forward(25)
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(270)
    turt.forward(25)
    for i in range(1, 5):
        turt.setheading(0)
        turt.forward(25)
        turt.setheading(270)
        turt.forward(25)

    #Begin building 6
    turt.setheading(0)
    turt.forward(25)
    turt.setheading(90)
    turt.forward(50)
    turt.setheading(0)
    turt.forward(50)
    turt.setheading(270)
    turt.forward(50)

    #Begin building 7
    turt.setheading(45)
    turt.forward(50)
    turt.setheading(315)
    turt.forward(50)
    turt.end_fill()

turtle.setup(800, 800)

# dark navy blue background
turtle.bgcolor((0, 0, .1))

wn = turtle.Screen()
turt = turtle.Turtle()
# Call draw_embellishment first so you don't have to see all the stars generate
draw_embellishment(turt)
draw_sky(turt)
wn.exitonclick()
