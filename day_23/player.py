

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed(2)

    def go_up(self):
        """Move the turtle up the screen.
        Args:
            None

        Returns:
            None: Moves the snake one step along its current heading.
        """

        self.forward(MOVE_DISTANCE)

