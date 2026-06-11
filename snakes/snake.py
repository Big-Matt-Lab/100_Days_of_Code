"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Snake Module ***
Defines the snake body, movement, and border reaction for the Snake game.

Python Concepts Highlighted:
- constants for readable direction control
- list traversal for moving snake segments
- class methods for organizing behavior
- random choice for border direction changes
"""

import random
from turtle import Turtle

# Python concept: constants improve readability and avoid magic numbers.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the snake composed of Turtle segments."""

    def __init__(self):
        """Create the initial snake body and set the head segment.

        Args:
            None

        Returns:
            None: Initializes the snake segments and head reference.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Build the initial snake by creating Turtle segments.

        Args:
            None

        Returns:
            None: Appends each segment to `self.segments`.
        """
        for position in STARTING_POSITIONS:
            s = Turtle()
            s.shape("square")
            s.color("white")
            s.penup()
            s.goto(position)
            s.speed(2)
            self.segments.append(s)

    def move(self):
        """Move the snake forward by shifting each segment.

        Args:
            None

        Returns:
            None: Moves the snake one step along its current heading.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake head direction upward if not moving downward.

        Args:
            None

        Returns:
            None: Updates the head heading to `UP` if valid.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake head direction downward if not moving upward.

        Args:
            None

        Returns:
            None: Updates the head heading to `DOWN` if valid.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake head direction leftward if not moving rightward.

        Args:
            None

        Returns:
            None: Updates the head heading to `LEFT` if valid.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake head direction rightward if not moving leftward.

        Args:
            None

        Returns:
            None: Updates the head heading to `RIGHT` if valid.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def border_crossing(self):
        """Handle the snake touching the border and change its heading.

        Args:
            None

        Returns:
            None: Keeps the snake on screen and changes direction.
        """
        x = self.head.xcor()
        y = self.head.ycor()
        if x > 290 or x < -290 or y > 290 or y < -290:
            if x > 290:
                self.head.setx(290)
            elif x < -290:
                self.head.setx(-290)
            elif y > 290:
                self.head.sety(290)
            elif y < -290:
                self.head.sety(-290)

            current_heading = self.head.heading()

            left_turn = (current_heading + 90) % 360
            right_turn = (current_heading + 270) % 360

            # Python concept: choose a perpendicular direction after border contact.
            self.head.setheading(random.choice([left_turn, right_turn]))