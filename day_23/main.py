
"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp
*** Day 23: Turtle Crossing Game ***
This script implements a classic Turtle Crossing game where a turtle (player) tries to cross a road filled with moving cars. The player earns a level up by reaching the other side and loses a life if it collides with a car.

Python Concepts Highlighted:
- `turtle` module for graphical game development (creating screen, shapes, listening for key presses).
- Object-Oriented Programming (OOP) for structuring game entities (`Player`, `CarManager`, `Scoreboard`).
- Game loop for continuous updates and drawing (`while game_is_on:`).
- Collision detection using `distance()` method.
- Event handling for player movement (`SCREEN.onkey()`).
- `time` module for controlling game speed (`time.sleep()`).
- Managing multiple game objects (cars) within a list (`car_manager.all_cars`).
- Game state management (player lives, game over condition).
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Python concept: `Screen` class from the `turtle` module for setting up the game window.
SCREEN = Screen()
# Python concept: Setting the title of the game window.
SCREEN.title("Frogger Game")
# Python concept: Setting the dimensions of the game window.
SCREEN.setup(width=600, height=600)
# Python concept: Turning off screen updates to manually control animation, preventing flickering.
SCREEN.tracer(0)

# Python concept: Instantiating the `Player` object, representing the turtle.
player = Player()
# Python concept: Instantiating the `CarManager` object to handle car creation and movement.
car_manager = CarManager()
# Python concept: Instantiating the `Scoreboard` object to display game level and status.
level = Scoreboard()


# Python concept: Setting up the screen to listen for keyboard input.
SCREEN.listen()

# Python concept: Binding the "Up" arrow key to the `player.go_up` method for player movement.
SCREEN.onkey(player.go_up, "Up")


# Python concept: Boolean flag to control the main game loop.
game_is_on = True
# Python concept: The main game loop that runs as long as `game_is_on` is `True`.
while game_is_on:
    # Python concept: Pausing the game for a short duration to control frame rate.
    time.sleep(0.1)
    # Python concept: Manually updating the screen to show all changes made since the last `tracer(0)`.
    SCREEN.update()

    # Python concept: Calling methods to create new cars and move existing cars.
    car_manager.create_car()
    car_manager.move_cars()

    # Python concept: Iterating through each car to check for collisions with the player.
    for car in car_manager.all_cars:
        # Python concept: Checking for collision using the `distance()` method between the player and a car.
        if player.distance(car) < 20:
            # Python concept: Decrementing player's lives upon collision.
            player.lose_a_life()
            # Python concept: Checking if the player has run out of lives.
            if player.lives < 1:
                # Python concept: Ending the game if no lives are left.
                game_is_on = False
                # Python concept: Displaying the "GAME OVER" message on the scoreboard.
                level.game_over()
            else:
                # Python concept: Resetting the player to the starting position after losing a life.
                player.go_to_start()

    # Python concept: Checking if the player has reached the finish line.
    if player.is_at_finish_line():
        # Python concept: Resetting the player to the starting position upon reaching the finish line.
        player.go_to_start()
        # Python concept: Increasing the speed of cars for the next level.
        car_manager.level_up()
        # Python concept: Incrementing the level on the scoreboard.
        level.increase_level()

