
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_X_LOCATION = 280
MOVE_DISTANCE= 10
starting_y_location = random.randint(-280, 280)

class CarManager(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("square")
        self.shapesize(0.7, 2, 1)
        self.penup()
        self.goto(STARTING_X_LOCATION, starting_y_location)
        self.setheading(180)
        self.speed(5)

    def left(self):
        """Move the turtle up the screen.
        Args:
            None

        Returns:
            None: Moves the snake one step along its current heading.
        """

        self.forward(MOVE_DISTANCE)
