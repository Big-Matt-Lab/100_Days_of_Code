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
        # Attributes - standards of the object
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))
    # Methods - Actions of the object
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

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
