import random
import turtle

# This function draws the entire night sky using turtle turt.
def draw_sky(turt):

    # draw 200 random stars, one by one
    for speck in range(200):

        # choose random x and y coordinates
        # TODO: you need to rewrite these statements to generate coordinates
        # over the entire window, not just near the origin
        x = random.randrange(-400, 400)
        y = random.randrange(-400, 400)

        # choose random star type; first generate an integer between
        # 0 and 99 inclusive
        #percent = random.randrange(0, 100)
        percent = 1
        # TODO: now use if statement(s) on percent, to decide whether to
        if percent == 1:
            blue_star(turt, x, y)
        # call blue_star, red_star, or big_star

# Draw a small blue star at x, y, using turt.
def blue_star(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(0, 0, random.uniform(0.5, 1))
    turt.circle(5)
    #turt.color(random.uniform(0.9, 1.0),random.uniform(0.7, 1.0), 1)

    # TODO: add statements to pick a random blue-white color, and random
    # radius, and then draw a dot using that color and radius

# Draw a medium-sized red star at x, y using turt.
def red_star(turt, x, y):
    turt.goto(x, y)
    # TODO: add statements to pick a random red-white color, and random
    # radius, and then draw a dot using that color and radius

# Draw a large four-pointed star at x, y using turt.
def big_star(turt, x, y):
    turt.goto(x, y)
    # TODO: add statements to draw a four-pointed white star

turtle.setup(800, 800)

# dark navy blue background
turtle.bgcolor((0, 0, .1))

wn = turtle.Screen()
turt = turtle.Turtle()
draw_sky(turt)
wn.exitonclick()
