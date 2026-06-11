"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Scoreboard Module ***
Displays the current score during gameplay and a final banner at game over.

Python Concepts Highlighted:
- class inheritance for reusing Turtle features
- instance attributes for tracking state
- formatted string output for display labels
"""

from turtle import Turtle

class Scoreboard(Turtle):
    """Displays the score and final game-over message."""

    def __init__(self):
        """Initialize the scoreboard and write the starting score.

        Args:
            None

        Returns:
            None: Sets up the score display at the top of the screen.
        """
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increment the score and refresh the on-screen text.

        Args:
            None

        Returns:
            None: Updates the score display with the new value.
        """
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        """Show the final game-over banner with the player's score.

        Args:
            None

        Returns:
            None: Clears the previous score and displays game-over text.
        """
        self.clear()
        self.goto(0, 0)
        self.write(
            f"Game Over\nFinal Score: {self.score}\nPress any key to close",
            align="center",
            font=("Arial", 24, "bold"),
        )
