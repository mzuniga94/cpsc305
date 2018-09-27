
import turtle

# Draw an entire mosaic.
def draw_mosaic():
    # you should be able to leave this function unchanged

    turt = turtle.Turtle()

    # speed up the turtle, otherwise this takes way too long
    turt.speed(10)

    # 4 corners
    # top-left
    draw_corner(turt, 0, 0, tile_x(0), tile_y(0))
    # top-right
    draw_corner(turt, 0, 19, tile_x(19), tile_y(0))
    # bottom-left
    draw_corner(turt, 19, 0, tile_x(0), tile_y(19))
    # bottom-right
    draw_corner(turt, 19, 19, tile_x(19), tile_y(19))

    # horizontal borders
    for col in range(1, 19):
        # top row
        draw_border_tile(turt, 0, col, tile_x(col), tile_y(0))
        # bottom row
        draw_border_tile(turt, 19, col, tile_x(col), tile_y(19))

    # vertical borders
    for row in range(1, 19):
        # left column
        draw_border_tile(turt, row, 0, tile_x(0), tile_y(row))
        # right column
        draw_border_tile(turt, row, 19, tile_x(19), tile_y(row))

    # inset
    for row in range(1, 19):
        for col in range(1, 19):
            draw_inset_tile(turt, row, col, tile_x(col), tile_y(row))
    
    # centerpiece
    draw_centerpiece(turt, 0, 0)

# Compute the x-coordinate of the tile on column number col.
def tile_x(col):
    # you should be able to leave this function unchanged
    return -300 + (30 * col)

# Compute the y-coordinate of the tile on row number row.
def tile_y(row):
    # you should be able to leave this function unchanged
    return -300 + (30 * row)

# Draw a corner tile at the given row, column, x-coordinate, and y-coordinate.
def draw_corner(turt, row, col, x, y):
    # you need to rewrite this function
    turt.setpos(x, y)

# Draw a border tile at the given row, column, x-coordinate, and y-coordinate.
def draw_border_tile(turt, row, col, x, y):
    turt.setpos(x, y)

# Draw an inset tile at the given row, column, x-coordinate, and y-coordinate.
def draw_inset_tile(turt, row, col, x, y):
    turt.setpos(x, y)

# Draw the centerpiece at the given x-coordinate and y-coordinate. This is
# done by drawing the same shape 36 times, overlapping, each draw separated
# by 10 degrees.
def draw_centerpiece(turt, x, y):
    for angle in range(0, 360, 10):
        draw_centerpiece_stencil(turt, x, y, angle)

# Draw a shape in the centerpiece, starting at the given x-coordinate and
# y-coordinate, and rotated by angle degrees.
def draw_centerpiece_stencil(turt, x, y, angle):
    turt.setpos(x, y)
    turt.setheading(angle)
    turt.forward(100)
    turt.backward(100)

turtle.setup(800, 800)
wn = turtle.Screen()
draw_mosaic()
wn.exitonclick()
