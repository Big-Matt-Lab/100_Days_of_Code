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
# Python concept: Constants for text alignment and font styling improve readability and maintainability.
ALIGNMENT = "center" # Python concept: Define a constant for text alignment.
FONT = ("Arial", 24, "normal") # Python concept: Define a constant for font name, size, and style.


class Scoreboard(Turtle):
    """Manages and displays the game score and high score.

    Inherits from `turtle.Turtle` to utilize its text writing capabilities.
    """

    def __init__(self):
        """Initializes the scoreboard, setting up its position, color, and initial score display.

        Loads the high score from `data.txt` on startup.

        Args:
            None

        Returns:
            None: Sets up the scoreboard appearance and initial values.
        """
        super().__init__()
        self.score = 0 # Python concept: Initialize current score to 0.
        self.high_score = self.load_high_score() # Python concept: Load the high score from a file.
        self.penup() # Python concept: Lift the pen to prevent drawing when moving the Turtle.
        self.color("white") # Python concept: Set the text color to white.
        self.goto(0, 260) # Python concept: Position the scoreboard at the top center of the screen.
        self.hideturtle() # Python concept: Hide the Turtle icon itself, showing only the written text.
        self.update_scoreboard() # Python concept: Display the initial score and high score.

    def update_scoreboard(self):
        """Clears the current scoreboard display and rewrites it with updated scores.

        Displays both the current score and the high score.

        Args:
            None

        Returns:
            None: Refreshes the on-screen score display.
        """
        self.clear() # Python concept: Clear any previous text drawn by this Turtle.
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT) # Python concept: Write the formatted score string to the screen.

    def reset(self):
        """Resets the current score to 0 and updates the high score if the current score surpasses it.

        Saves the new high score to `data.txt`.

        Args:
            None

        Returns:
            None: Resets the score and updates the scoreboard display.
        """
        if self.score > self.high_score: # Python concept: Check if the current score is a new high score.
            self.high_score = self.score # Python concept: Update `high_score` if a new record is set.
            # Python concept: Open `data.txt` in write mode to save the new high score.
            with open("data.txt", "w") as data_file:
                data_file.write(str(self.high_score)) # Python concept: Write the integer high score as a string to the file.
        self.score = 0 # Python concept: Reset the current score for the new game round.
        self.update_scoreboard() # Python concept: Update the display with the reset score and potentially new high score.

    def game_over(self):
        """Displays a 'GAME OVER' message in the center of the screen.

        Args:
            None

        Returns:
            None: Writes the game over message.
        """
        self.goto(0, 0) # Python concept: Move the Turtle to the center of the screen.
        self.write("GAME OVER", align=ALIGNMENT, font=FONT) # Python concept: Write the "GAME OVER" text.

    def increase_score(self):
        """Increments the current score by 1 and updates the scoreboard display.

        Args:
            None

        Returns:
            None: Updates `self.score` and refreshes the display.
        """
        self.score += 1 # Python concept: Increment the current score.
        self.update_scoreboard() # Python concept: Call `update_scoreboard()` to reflect the new score.

    def load_high_score(self):
        """Loads the high score from `data.txt`.

        Handles `FileNotFoundError` by returning 0 if the file does not exist.

        Args:
            None

        Returns:
            int: The loaded high score, or 0 if the file is not found or empty.
        """
        try: # Python concept: Use a `try-except` block to handle potential file errors.
            # Python concept: Open `data.txt` in read mode.
            with open("data.txt", mode="r") as file:
                high_score = file.read() # Python concept: Read the content of the file.
                return int(high_score) # Python concept: Convert the read string to an integer.
        except FileNotFoundError: # Python concept: Catch the error if the file does not exist.
            return 0 # Python concept: Return 0 as default high score if file is not found.





