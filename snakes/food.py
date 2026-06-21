"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Food Module ***
Provides the `Food` class for the Snake game and handles random food placement.

Python Concepts Highlighted:
- class inheritance for extending `Turtle`
- random number generation for dynamic placement (`randint`)
- method encapsulation for refresh behavior
"""

import random # Python concept: Import the `random` module for generating random numbers.
from turtle import Turtle # Python concept: Import the `Turtle` class for creating game objects.


class Food(Turtle):
    """Represents the food item that the snake must collect.

    Inherits from `turtle.Turtle` to leverage its drawing and movement functionalities.
    """

    def __init__(self):
        """Initializes the food sprite and places it randomly on screen.

        Calls the `super().__init__()` to properly initialize the `Turtle` base class.
        Sets up the visual properties of the food and its initial position.

        Args:
            None

        Returns:
            None: Initializes the `Food` object with specific Turtle properties.
        """
        super().__init__()

        # Python concept: Configure Turtle graphics appearance using various methods.
        self.shape("circle") # Python concept: Set the shape of the food to a circle.
        self.penup() # Python concept: Lift the pen to prevent drawing when moving.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Python concept: Shrink the circle size.
        self.color("blue") # Python concept: Set the color of the food.
        self.speed("fastest") # Python concept: Set the animation speed to the fastest.
        self.refresh() # Python concept: Immediately place the food at a random starting position.

    def refresh(self):
        """Moves the food to a new random location within the screen bounds.

        This method is called when the snake eats the food, repositioning it for the next round.

        Args:
            None

        Returns:
            None: Repositions the food using the `goto()` method.
        """
        # Python concept: Use `random.randint()` to generate random integer coordinates.
        random_x = random.randint(-280, 280) # Python concept: Generate a random X coordinate within game bounds.
        random_y = random.randint(-280, 280) # Python concept: Generate a random Y coordinate within game bounds.
        self.goto(random_x, random_y) # Python concept: Move the food Turtle to the new random coordinates.







