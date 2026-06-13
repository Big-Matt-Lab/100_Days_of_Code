"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Players (Paddles & Player State) ***
This module defines the `Paddle` drawable and the `Player`/`Players`
containers that manage control bindings and score tracking for both players.

Python Concepts Highlighted:
- `Turtle` subclassing to create a reusable `Paddle` actor.
- Using module-level `constants` to centralize configuration.
- Binding keyboard events to methods via `screen.onkey()`.
"""

from turtle import Turtle

# Python concept: define constants for reusable configuration values.
PADDLE_MARGIN = 100
PLAYER_START_Y = 0
PADDLE_MOVE_DISTANCE = 30
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_STRETCH_WID = 5
PADDLE_STRETCH_LEN = 1

class Paddle(Turtle):
    """Represents a Pong paddle that can move up and down."""

    def __init__(self, start_x: int, start_y: int):
        """Create a paddle at a specific starting position.

        Args:
            start_x (int): Starting x-coordinate for the paddle.
            start_y (int): Starting y-coordinate for the paddle.

        Returns:
            None
        """
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_STRETCH_WID, stretch_len=PADDLE_STRETCH_LEN)
        self.penup()
        self.goto(start_x, start_y)
        self.speed("fastest")

    def move_up(self):
        """Move the paddle upward by a fixed distance.

        Python concept: Using `ycor()` and `goto()` to update the turtle's
        position without drawing (the paddle uses `penup()`).
        """
        new_y = self.ycor() + PADDLE_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Move the paddle downward by a fixed distance.

        Python concept: Symmetric to `move_up()`; encapsulates motion so
        key bindings can call a simple method reference.
        """
        new_y = self.ycor() - PADDLE_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


class Player:
    """Tracks a Pong player's paddle, controls, and score."""

    def __init__(self, name: str, start_x: int, start_y: int, up_key: str, down_key: str):
        """Initialize player state and create the paddle.

        Args:
            name (str): Player name.
            start_x (int): Paddle starting x-coordinate.
            start_y (int): Paddle starting y-coordinate.
            up_key (str): Keyboard key for moving up.
            down_key (str): Keyboard key for moving down.

        Returns:
            None
        """
        self.name = name
        self.paddle = Paddle(start_x, start_y)
        self.score = 0
        self.up_key = up_key
        self.down_key = down_key

    def score_point(self):
        """Increment the player's `score` counter by one.

        Python concept: Simple attribute mutation to track game state.
        """
        self.score += 1


class Players:
    """Holds both Pong players and their paddles."""

    def __init__(self, screen):
        """Create both players with their paddles and control keys.

        Args:
            screen: The Turtle screen instance used to compute paddle positions.

        Returns:
            None
        """
        half_width = screen.window_width() / 2
        paddle_x = half_width - PADDLE_MARGIN
        self.player1 = Player("Player 1", -paddle_x, PLAYER_START_Y, "w", "s")
        self.player2 = Player("Player 2", paddle_x, PLAYER_START_Y, "Up", "Down")

    def bind_controls(self, screen):
        """Bind keyboard controls for both players to the given screen.

        Args:
            screen: The Turtle screen object to bind keys to.

        Returns:
            None
        """
        # Python concept: Bind a callable (method reference) to a key event.
        screen.onkey(self.player1.paddle.move_up, self.player1.up_key)
        screen.onkey(self.player1.paddle.move_down, self.player1.down_key)
        screen.onkey(self.player2.paddle.move_up, self.player2.up_key)
        screen.onkey(self.player2.paddle.move_down, self.player2.down_key)

    def get_scores(self):
        """Return the current scores for both players.

        Returns:
            tuple[int, int]: Scores for player1 and player2.
        """
        return self.player1.score, self.player2.score
