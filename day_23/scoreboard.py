"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp
*** Day 23: Scoreboard Class ***
This script defines the `Scoreboard` class for the Turtle Crossing game. It is responsible for displaying the current level and the "GAME OVER" message.

Python Concepts Highlighted:
- Inheritance from `turtle.Turtle` for creating a text-displaying object.
- Constants for font style (`FONT`).
- Object methods for updating the display (`update_scoreboard`, `increase_level`, `game_over`).
- `write()` method for displaying text on the screen.
- `clear()` method to remove previous text before updating.
"""

import time
from turtle import Turtle

# Python concept: `FONT` is a tuple defining the font family, size, and style for the scoreboard text.
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Manages the display of the game level and game over messages."""

    def __init__(self):
        """Initializes the Scoreboard object.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        # Python concept: Initializing the game level.
        self.level = 1
        # Python concept: Hiding the turtle icon itself, as only its writing capability is needed.
        self.hideturtle()
        # Python concept: Lifting the pen so no lines are drawn when moving.
        self.penup()
        # Python concept: Positioning the scoreboard text on the screen.
        self.goto(-280, 250)
        # Python concept: Calling `update_scoreboard` to display the initial level.
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the current scoreboard and writes the updated level.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Clearing any previously written text on the screen.
        self.clear()
        # Python concept: Writing the current level to the screen, aligned to the left.
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increments the level and updates the scoreboard.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Incrementing the `level` attribute.
        self.level += 1
        # Python concept: Calling `update_scoreboard` to display the new level.
        self.update_scoreboard()

    def game_over(self):
        """Displays the "GAME OVER" message in the center of the screen.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Moving the turtle to the center of the screen to display the game over message.
        self.goto(0, 0)
        # Python concept: Writing the "GAME OVER" message, centered, using the defined font.
        self.write(f"GAME OVER", align="center", font=FONT)
        time.sleep(2)

