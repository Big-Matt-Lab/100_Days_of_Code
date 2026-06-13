"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Ball Actor ***
Defines the `Ball` used in Pong: a `Turtle` subclass that stores a
velocity vector (`dx`, `dy`) and provides movement and bounce helpers.

Python Concepts Highlighted:
- `Turtle` subclassing for visual game objects.
- Randomized initial state via `random.choice()`.
"""

from turtle import Turtle
import random


class Ball(Turtle):
    """Ball object for Pong. Inherits from `turtle.Turtle` for rendering.

    Responsibilities:
    - Track position and velocity (`dx`, `dy`).
    - Move each frame via `move()`.
    - Bounce on X/Y axes and reset position on score.
    """

    def __init__(self):
        """Create and configure the ball's appearance and initial velocity.

        The horizontal (`dx`) and vertical (`dy`) velocities are randomized
        in direction using `random.choice([1, -1])` so each serve differs.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        # Python concept: initial velocity (pixels per frame)
        self.dx = 10 * random.choice([1, -1])
        self.dy = 8 * random.choice([1, -1])

    def move(self):
        """Advance the ball by its velocity vector.

        Returns:
            None
        """
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        """Invert vertical velocity (bounce off top/bottom walls).

        This flips the sign of `dy` to reflect vertical motion.
        """
        self.dy *= -1

    def bounce_x(self):
        """Invert horizontal velocity (bounce off paddles) and slightly increase speed.

        We slightly scale the velocities to make the game progressively harder
        after successful paddle hits.
        """
        self.dx *= -1.05
        self.dy *= 1.05

    def reset_position(self):
        """Return the ball to center and randomize initial direction/speed.

        This is called after a score to prepare for the next serve.
        """
        self.goto(0, 0)
        self.dx = 10 * random.choice([1, -1])
        self.dy = 8 * random.choice([1, -1])
