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

import random # Python concept: Import the `random` module for various random operations.
from turtle import Turtle # Python concept: Import the `Turtle` class for creating game objects.


# Python concept: Constants improve code readability and make values easily configurable.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # Python concept: A tuple of tuples defining the initial coordinates for snake segments.
MOVE_DISTANCE = 20 # Python concept: The distance each snake segment moves per step.
UP = 90 # Python concept: Angle for moving upwards.
DOWN = 270 # Python concept: Angle for moving downwards.
LEFT = 180 # Python concept: Angle for moving left.
RIGHT = 0 # Python concept: Angle for moving right.


class Snake:
    """Represents the snake in the game, composed of multiple `Turtle` segments.

    Manages the snake's creation, movement, and direction changes.
    """

    def __init__(self):
        """Initializes the snake by creating its initial segments and setting the head reference.

        Args:
            None

        Returns:
            None: Sets up the `self.segments` list and `self.head` attribute.
        """
        self.segments = [] # Python concept: A list to hold all `Turtle` objects that form the snake's body.
        self.create_snake() # Python concept: Call a method to build the initial snake body.
        self.head = self.segments[0] # Python concept: Reference to the first segment, which is the snake's head.

    def create_snake(self):
        """Builds the initial snake body using `Turtle` segments.

        Each segment is a white square and is positioned according to `STARTING_POSITIONS`.

        Args:
            None

        Returns:
            None: Appends each newly created segment to the `self.segments` list.
        """
        for position in STARTING_POSITIONS: # Python concept: Iterate through predefined starting positions.
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake's body at the given position.

        Args:
            position (tuple): A tuple (x, y) representing the coordinates for the new segment.

        Returns:
            None: Appends the new `Turtle` object to `self.segments`.
        """
        s = Turtle("square") # Python concept: Create a new `Turtle` object with a square shape.
        s.color("white") # Python concept: Set the color of the segment.
        s.penup() # Python concept: Lift the pen to prevent drawing when moving.
        s.goto(position) # Python concept: Move the segment to its specified position.
        self.segments.append(s) # Python concept: Add the new segment to the list of segments.

    def extend(self):
        """Adds a new segment to the end of the snake when it eats food.

        The new segment is added at the position of the last segment.

        Args:
            None

        Returns:
            None: Expands the snake by one segment.
        """
        self.add_segment(self.segments[-1].position()) # Python concept: Add a new segment at the position of the last segment.

    def reset_snake(self):
        """Resets the snake to its initial state, clearing all existing segments and rebuilding it.

        This is typically called after a game over to prepare for a new round.

        Args:
            None

        Returns:
            None: Resets the `self.segments` list and `self.head` reference.
        """
        for seg in self.segments: # Python concept: Iterate through existing segments.
            seg.goto(1000, 1000) # Python concept: Move old segments off-screen before clearing.
        self.segments.clear() # Python concept: Remove all segments from the list.
        self.create_snake() # Python concept: Rebuild the snake to its initial length and position.
        self.head = self.segments[0] # Python concept: Re-establish the head reference.

    def move(self):
        """Moves the snake forward by shifting each segment to the position of the segment in front of it.

        The head segment moves forward by `MOVE_DISTANCE`.

        Args:
            None

        Returns:
            None: Updates the positions of all snake segments.
        """
        # Python concept: Iterate from the last segment to the second segment (index 1).
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # Python concept: Get the X-coordinate of the preceding segment.
            new_y = self.segments[seg_num - 1].ycor() # Python concept: Get the Y-coordinate of the preceding segment.
            self.segments[seg_num].goto(new_x, new_y) # Python concept: Move the current segment to the preceding segment's position.
        self.head.forward(MOVE_DISTANCE) # Python concept: Move the head segment forward by the defined distance.

    def up(self):
        """Changes the snake's head direction to upward (90 degrees) if not currently moving downward.

        Prevents the snake from reversing onto itself.

        Args:
            None

        Returns:
            None: Sets the head's heading to `UP` if valid.
        """
        if self.head.heading() != DOWN: # Python concept: Prevent immediate reversal.
            self.head.setheading(UP) # Python concept: Set the head's orientation.

    def down(self):
        """Changes the snake's head direction to downward (270 degrees) if not currently moving upward.

        Prevents the snake from reversing onto itself.

        Args:
            None

        Returns:
            None: Sets the head's heading to `DOWN` if valid.
        """
        if self.head.heading() != UP: # Python concept: Prevent immediate reversal.
            self.head.setheading(DOWN) # Python concept: Set the head's orientation.

    def left(self):
        """Changes the snake's head direction to leftward (180 degrees) if not currently moving rightward.

        Prevents the snake from reversing onto itself.

        Args:
            None

        Returns:
            None: Sets the head's heading to `LEFT` if valid.
        """
        if self.head.heading() != RIGHT: # Python concept: Prevent immediate reversal.
            self.head.setheading(LEFT) # Python concept: Set the head's orientation.

    def right(self):
        """Changes the snake's head direction to rightward (0 degrees) if not currently moving leftward.

        Prevents the snake from reversing onto itself.

        Args:
            None

        Returns:
            None: Sets the head's heading to `RIGHT` if valid.
        """
        if self.head.heading() != LEFT: # Python concept: Prevent immediate reversal.
            self.head.setheading(RIGHT) # Python concept: Set the head's orientation.

    def border_crossing(self):
        """Handles the snake touching the border by repositioning it and changing its heading.

        This keeps the snake on screen and introduces a random turn perpendicular to the border.

        Args:
            None

        Returns:
            None: Adjusts snake's position and direction.
        """
        x = self.head.xcor() # Python concept: Get the current X-coordinate of the snake's head.
        y = self.head.ycor() # Python concept: Get the current Y-coordinate of the snake's head.
        # Python concept: Check if the snake's head has crossed any of the four borders.
        if x > 290 or x < -290 or y > 290 or y < -290:
            # Python concept: Reposition the snake slightly inside the border it crossed.
            if x > 290:
                self.head.setx(290)
            elif x < -290:
                self.head.setx(-290)
            elif y > 290:
                self.head.sety(290)
            elif y < -290:
                self.head.sety(-290)

            current_heading = self.head.heading() # Python concept: Get the snake's current heading.

            # Python concept: Calculate new headings for a 90-degree left or right turn.
            left_turn = (current_heading + 90) % 360 
            right_turn = (current_heading + 270) % 360 

            # Python concept: Randomly choose between a left or right turn after border contact.
            self.head.setheading(random.choice([left_turn, right_turn]))








