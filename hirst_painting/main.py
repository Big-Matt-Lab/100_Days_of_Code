
"""Hirst painting generator using turtle graphics.

This module draws a 10x10 grid of colored dots inspired by Damien
Hirst's spot paintings. It uses a palette of RGB colors and turtle
graphics to render the final artwork.

Python concepts highlighted: module imports, function definitions,
loops, random choice, and turtle screen control.
"""

from color_data import pallette
import random
import turtle

# Configure the turtle screen to use RGB colors in the 0-255 range.
SCREEN = turtle.Screen()
SCREEN.colormode(255)

# Create and configure the drawing turtle.
t = turtle.Turtle()
t.speed('fastest')


def pen_move(color_pallette):
    """Draw a grid of colored dots using the supplied palette.

    Args:
        color_pallette (list[tuple[int, int, int]]): List of RGB tuples
            that the dot grid can select from.

    Returns:
        None: The drawing is rendered directly to the turtle screen.
    """

    x_start = -250
    y_start = 200

    # Move the turtle to the top-left starting position without drawing.
    t.teleport(x_start, y_start)

    for i in range(10):
        for j in range(10):
            # Draw a dot using a random color from the palette.
            t.dot(25, random.choice(color_pallette))

            # Lift the pen so the turtle can move without drawing a line.
            t.penup()
            t.forward(50)

        # Move down one row and reset to the left edge.
        y_start -= 50
        t.teleport(x_start, y_start)


if __name__ == '__main__':
    # Create the artwork using the imported palette and hide the turtle.
    pen_move(pallette)
    t.hideturtle()

    # Keep the window open until the user clicks.
    SCREEN.exitonclick()
