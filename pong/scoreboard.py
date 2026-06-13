from turtle import Turtle


"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Scoreboard (Score Displays) ***
Manages on-screen score displays for left and right players and provides a
`game_over()` helper to present final results.

Python Concepts Highlighted:
- Text rendering with `Turtle` writers.
- Keeping UI state synchronized with underlying model (`left_score`, `right_score`).
"""

from turtle import Turtle


class Scoreboard:
    """Displays and manages the scores for both Pong players.

    Args:
        screen: The Turtle `Screen` used to compute text positions.
        left_name (str): Label for left player.
        right_name (str): Label for right player.
    """

    def __init__(self, screen, left_name: str = "Player 1", right_name: str = "Player 2"):
        self.screen = screen
        self.left_name = left_name
        self.right_name = right_name
        self.left_score = 0
        self.right_score = 0

        half_w = self.screen.window_width() / 2
        top_y = self.screen.window_height() / 2 - 40

        # left score writer
        self.left_writer = Turtle()
        self.left_writer.hideturtle()
        self.left_writer.penup()
        self.left_writer.color("white")
        self.left_writer.goto(-half_w + 150, top_y)

        # right score writer
        self.right_writer = Turtle()
        self.right_writer.hideturtle()
        self.right_writer.penup()
        self.right_writer.color("white")
        self.right_writer.goto(half_w - 150, top_y)

        # Draw initial scores
        self.update()

    def update(self):
        """Redraw the scores on screen.

        Clears the previous text and writes the latest score values.
        """
        self.left_writer.clear()
        self.right_writer.clear()
        self.left_writer.write(f"{self.left_name}: {self.left_score}", align="center", font=("Arial", 20, "normal"))
        self.right_writer.write(f"{self.right_name}: {self.right_score}", align="center", font=("Arial", 20, "normal"))

    def increase_left(self):
        """Increase left player's score by one and update display.

        Python concept: Mutating the model (`left_score`) and updating the UI
        keeps the display in sync with state changes.
        """
        self.left_score += 1
        self.update()

    def increase_right(self):
        """Increase right player's score by one and update display."""
        self.right_score += 1
        self.update()

    def game_over(self):
        """Display final result and instructions to close the window.

        Writes a winner message plus the final scores and leaves the
        screen open for the user to press any key to close.
        """
        go = Turtle()
        go.hideturtle()
        go.color("white")
        go.penup()
        go.goto(0, 20)
        # Determine winner text
        if self.left_score > self.right_score:
            winner_text = f"Winner: {self.left_name}"
        elif self.right_score > self.left_score:
            winner_text = f"Winner: {self.right_name}"
        else:
            winner_text = "Draw"

        go.write(f"{winner_text}\nFinal: {self.left_name} {self.left_score}  {self.right_name} {self.right_score}", align="center", font=("Arial", 24, "bold"))

        instr = Turtle()
        instr.hideturtle()
        instr.color("white")
        instr.penup()
        instr.goto(0, -30)
        instr.write("Press any key to close", align="center", font=("Arial", 16, "normal"))
        # Determine winner text
        if self.left_score > self.right_score:
            winner_text = f"Winner: {self.left_name}"
        elif self.right_score > self.left_score:
            winner_text = f"Winner: {self.right_name}"
        else:
            winner_text = "Draw"

        go.write(f"{winner_text}\nFinal: {self.left_name} {self.left_score}  {self.right_name} {self.right_score}", align="center", font=("Arial", 24, "bold"))

        instr = Turtle()
        instr.hideturtle()
        instr.color("white")
        instr.penup()
        instr.goto(0, -30)
        instr.write("Press any key to close", align="center", font=("Arial", 16, "normal"))
