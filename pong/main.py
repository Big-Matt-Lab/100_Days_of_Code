
"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Pong Main Launcher ***
Entry point for the Pong application. This script creates the Turtle
`Screen`, configures the window, instantiates the `Game` controller, and
starts the game loop via `game.run()`.

Python Concepts Highlighted:
- `Screen` for window and event handling.
- Module-level orchestration: creating and wiring objects.
"""

from turtle import Screen
from game import Game

# Python concept: The `Screen` object is the drawing canvas for all `Turtle` objects.
screen = Screen()
# Python concept: Window appearance configuration (title, background color, size).
screen.bgcolor("black")
screen.title("PONG Game")
screen.setup(width=2000, height=1100)
screen.screensize(1900, 1000)

# Python concept: Compose the `Game` controller with the shared `screen`.
game = Game(screen)
# Python concept: Start the game loop which runs until a winner is declared.
game.run()
