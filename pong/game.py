"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Pong Game Controller ***
This module composes the playing field, player paddles, ball, and scoreboard
into a single `Game` controller that runs the main animation loop.

Python Concepts Highlighted:
- `Turtle` drawing with a manual animation loop (`screen.update()` + `time.sleep()`).
- Event binding for keyboard controls via `screen.onkey()`.
- Simple collision detection and score management in an OOP design.
"""

import time
from players import Players
from playing_field import PlayingField
from ball import Ball
from scoreboard import Scoreboard

# Python concept: Constant used to configure a play-to score threshold.
MAX_SCORE = 7

class Game:
    """Controls the overall Pong game state and component wiring."""

    def __init__(self, screen):
        """Initialize the game controller with screen, field, and players.

        Args:
            screen: The Turtle screen instance that renders the game.

        Returns:
            None
        """
        self.screen = screen
        self.field = PlayingField()
        # create players using the screen so paddle positions are computed dynamically
        self.players = Players(self.screen)
        # scoreboard shows names and scores for both players
        self.scoreboard = Scoreboard(self.screen, self.players.player1.name, self.players.player2.name)
        self.ball = Ball()

        self.players.bind_controls(self.screen)

    def run(self):
        """Start the Pong game loop: animate ball, check collisions, update scores."""
        half_w = self.screen.window_width() / 2
        half_h = self.screen.window_height() / 2

        self.screen.tracer(0)
        self.screen.listen()
        while True:
            # Python concept: Manual animation loop using `screen.update()` to redraw
            # all turtles and `time.sleep()` to limit frame rate.
            self.screen.update()
            time.sleep(0.03)

            # move ball each frame by its velocity vector
            self.ball.move()

            # bounce on top/bottom walls
            # Python concept: Boundary collision check using screen half-height.
            if self.ball.ycor() >= half_h - 10 or self.ball.ycor() <= -half_h + 10:
                self.ball.bounce_y()

            # paddle collisions (simple distance + position check)
            p1 = self.players.player1.paddle
            p2 = self.players.player2.paddle
            # Python concept: Simple paddle collision using `distance()` combined
            # with positional checks to reduce false positives.
            if self.ball.distance(p1) < 50 and self.ball.xcor() < p1.xcor() + 50:
                self.ball.bounce_x()
            if self.ball.distance(p2) < 50 and self.ball.xcor() > p2.xcor() - 50:
                self.ball.bounce_x()

            # scoring: ball passed the right or left edge
            if self.ball.xcor() > half_w:
                # left player scores
                self.players.player1.score_point()
                self.scoreboard.increase_left()
                self.ball.reset_position()
                # check for win and display game-over when threshold reached
                if self.scoreboard.left_score >= MAX_SCORE:
                    self.scoreboard.game_over()
                    # Python concept: Bind a global key event at the Tk canvas level
                    # so that *any* keypress triggers `screen.bye()`. Fallback to
                    # `screen.onkey()` if the canvas binding is unavailable.
                    try:
                        self.screen.getcanvas().bind_all("<Key>", lambda e: self.screen.bye())
                    except Exception:
                        self.screen.onkey(self.screen.bye, "q")
                    break
            if self.ball.xcor() < -half_w:
                # right player scores
                self.players.player2.score_point()
                self.scoreboard.increase_right()
                self.ball.reset_position()
                # check for win and display game-over
                if self.scoreboard.right_score >= MAX_SCORE:
                    self.scoreboard.game_over()
                    try:
                        self.screen.getcanvas().bind_all("<Key>", lambda e: self.screen.bye())
                    except Exception:
                        self.screen.onkey(self.screen.bye, "q")
                    break

        # Python concept: Enter the Tk event loop to allow the bound key event
        # to be received while the window is shown after the game loop exits.
        self.screen.mainloop()
