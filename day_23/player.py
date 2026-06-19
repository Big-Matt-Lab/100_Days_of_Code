"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp
*** Day 23: Player Class ***
This script defines the `Player` class for the Turtle Crossing game. The player is a turtle that can move up, reset its position, and detect if it has reached the finish line.

Python Concepts Highlighted:
- Inheritance from `turtle.Turtle` for creating a player object.
- Constants for game parameters (e.g., `STARTING_POSITION`, `MOVE_DISTANCE`, `FINISH_LINE_Y`).
- Object methods for player actions (`go_up`, `go_to_start`, `is_at_finish_line`).
- `ycor()` method to get the turtle's Y-coordinate.
"""

from turtle import Turtle

# Python concept: Constants for game configuration. `STARTING_POSITION` defines the initial coordinates for the player.
STARTING_POSITION = (0, -280)
# Python concept: `MOVE_DISTANCE` determines how many pixels the player moves with each step.
MOVE_DISTANCE = 10
# Python concept: `FINISH_LINE_Y` sets the Y-coordinate that the player must reach to level up.
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player turtle in the game."""

    def __init__(self):
        """Initializes the Player object.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        # Python concept: Setting the shape of the turtle to "turtle".
        self.shape("turtle")
        # Python concept: Lifting the pen so no lines are drawn when moving.
        self.penup()
        # Python concept: Moving the turtle to its starting position.
        self.goto(STARTING_POSITION)
        # Python concept: Setting the turtle's heading to face upwards.
        self.setheading(90)
        # Python concept: Setting the animation speed of the turtle.
        self.speed(2)
        # Python concept: Initializing the number of lives the player has.
        self.lives = 5

    def lose_a_life(self):
        """Decrements the player's lives.

        Args:
            None

        Returns:
            None
        """
        self.lives -= 1

    def go_up(self):
        """Moves the turtle forward by `MOVE_DISTANCE`.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Moving the turtle forward in its current direction.
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Resets the turtle to the `STARTING_POSITION`.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Moving the turtle to the predefined starting position.
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the turtle has reached the finish line.

        Args:
            None

        Returns:
            bool: `True` if the turtle's Y-coordinate is greater than `FINISH_LINE_Y`, `False` otherwise.
        """
        # Python concept: Returning a boolean based on the turtle's Y-coordinate relative to the finish line.
        return self.ycor() > FINISH_LINE_Y
