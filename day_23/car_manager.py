
"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp
*** Day 23: Car Manager Class ***
This script defines the `CarManager` class for the Turtle Crossing game. It is responsible for creating and managing the movement of cars on the screen.

Python Concepts Highlighted:
- `random` module for generating random car attributes (color, starting position).
- Inheritance from `turtle.Turtle` for creating car objects.
- List to store multiple car objects (`self.all_cars`).
- Object methods for car actions (`create_car`, `move_cars`, `level_up`).
- Constants for game parameters (e.g., `COLORS`, `STARTING_MOVE_DISTANCE`, `MOVE_INCREMENT`).
"""

import random
from turtle import Turtle

# Python concept: `COLORS` is a list of strings defining the possible colors for the cars.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Python concept: `STARTING_MOVE_DISTANCE` sets the initial speed of the cars.
STARTING_MOVE_DISTANCE = 5
# Python concept: `CAR_SPEED` is not used directly but was part of a previous iteration, now handled by `self.car_speed`.
CAR_SPEED = 0.5
# Python concept: `MOVE_INCREMENT` defines how much the car speed increases with each level.
MOVE_INCREMENT = 5


class CarManager(Turtle):
    """Manages the creation, movement, and leveling up of cars in the game."""

    def __init__(self):
        """Initializes the CarManager object.

        Args:
            None

        Returns:
            None
        """
        # Python concept: A list to hold all car objects on the screen.
        self.all_cars = []
        # Python concept: The current speed of the cars, which increases with each level.
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        """Creates a new car with a random position and color.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Randomly decides whether to create a new car in this game loop iteration.
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            # Python concept: Creating a new `Turtle` object for the car.
            new_car = Turtle()
            # Python concept: Setting the car's shape to a square.
            new_car.shape("square")
            # Python concept: Stretching the square to make it look like a car.
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Python concept: Lifting the pen so the car doesn't draw lines.
            new_car.penup()
            # Python concept: Assigning a random color from the `COLORS` list to the car.
            new_car.color(random.choice(COLORS))
            # Python concept: Generating a random starting Y-coordinate for the car.
            starting_y_location = random.randint(-250, 250)
            # Python concept: Placing the car at the right edge of the screen with a random Y-coordinate.
            new_car.goto(300, starting_y_location)
            # Python concept: Setting the car's heading to face left.
            new_car.setheading(180)
            # Python concept: Adding the newly created car to the list of all cars.
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars currently on the screen forward.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Iterating through each car in the `all_cars` list.
        for car in self.all_cars:
            # Python concept: Moving the car backward (towards the left of the screen) by `self.car_speed`.
            car.forward(self.car_speed)

    def level_up(self):
        """Increases the speed of the cars when the player levels up.

        Args:
            None

        Returns:
            None
        """
        # Python concept: Increasing `self.car_speed` by `MOVE_INCREMENT`.
        self.car_speed += MOVE_INCREMENT
