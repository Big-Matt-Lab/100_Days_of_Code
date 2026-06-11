"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Food Module ***
Provides the `Food` class for the Snake game and handles random food placement.

Python Concepts Highlighted:
- class inheritance for extending `Turtle`
- random number generation for dynamic placement (`randint`)
- method encapsulation for refresh behavior
"""

import random
from turtle import Turtle

class Food(Turtle):
    """Represents the food item that the snake must collect."""

    def __init__(self):
        """Initialize the food sprite and place it randomly on screen.

        Args:
            None

        Returns:
            None: Initializes the `Food` object with Turtle properties.
        """
        super().__init__()

        # Python concept: configuring Turtle graphics appearance with methods.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random location within screen bounds.

        Args:
            None

        Returns:
            None: Repositions the food using `goto()`.
        """
        # Python concept: using `random.randint()` to choose random coordinates.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

