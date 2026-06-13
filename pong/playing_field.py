"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Playing Field (Midline) ***
This module draws the dashed centerline that visually separates the Pong
court into left and right halves.

Python Concepts Highlighted:
- Using a `Turtle` instance for static drawing.
- Procedural drawing with loops and pen up/down control.
"""

from turtle import Turtle


class PlayingField(Turtle):
    """Draws the center dashed line for a Pong playing field.

    The `PlayingField` is implemented as a `Turtle` that draws once on
    initialization and then hides itself to leave only the static midline.
    """

    def __init__(self):
        """Initialize the playing field turtle and draw the midline.

        The turtle is positioned at the top-center and then draws downward
        using `pendown()`/`penup()` to create a dashed appearance.
        """
        super().__init__()
        self.color("white")
        self.penup()
        # Python concept: Move to top center to start drawing downward.
        self.goto(0, 490)
        self.setheading(270)
        self.speed("fastest")
        self.pensize(5)
        self.draw_midline()
        self.hideturtle()

    def draw_midline(self):
        """Draw a dashed center line down the middle of the screen.

        Python concept: Use a loop to alternate `pendown()` and `penup()`
        creating a dashed stroke rather than continuous line drawing.
        """
        for _ in range(20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(40)
