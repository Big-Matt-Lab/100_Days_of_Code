"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Snake Game Main ***
Runs the main Snake game loop and handles keyboard input for gameplay.

Python Concepts Highlighted:
- event-driven programming using `screen.onkey`
- loop control with `while`
- module-level state management using `global`
- Turtle graphics window setup and display refresh
"""

from turtle import Screen, Turtle # Python concept: Import specific classes from a module.
import time # Python concept: Import the `time` module for time-related functions.
from food import Food # Python concept: Import the `Food` class from the `food` module.
from scoreboard import Scoreboard # Python concept: Import the `Scoreboard` class from the `scoreboard` module.
from snake import Snake # Python concept: Import the `Snake` class from the `snake` module.

# Python concept: Initialize the Turtle graphics window for the game.
screen = Screen()
screen.setup(width=600, height=600) # Python concept: Set up the dimensions of the game window.
screen.bgcolor("black") # Python concept: Set the background color of the screen.
screen.title("Snake Game") # Python concept: Set the title of the game window.

# Python concept: Disable automatic screen updates for manual control to manage animations.
screen.tracer(0)

# Initialize game objects.
snake = Snake() # Python concept: Create an instance of the `Snake` class.
food = Food() # Python concept: Create an instance of the `Food` class.
scoreboard = Scoreboard() # Python concept: Create an instance of the `Scoreboard` class.

# Python concept: Module-level flag to control the main game loop.
game_is_on = True


def end_game():
    """Stop the game loop when the quit key is pressed.

    Args:
        None

    Returns:
        None: Updates `game_is_on` to terminate the loop.
    """
    # Python concept: Modify a module-level variable from inside a function using `global`.
    global game_is_on
    game_is_on = False

# Python concept: Set up event listening for key presses.
screen.listen()

# Python concept: Bind arrow keys to snake movement methods for interactive control.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Python concept: Bind the `q` key to the `end_game` function to gracefully exit.
screen.onkey(end_game, 'q')

# Main game loop.
while game_is_on:
    # Python concept: Update the screen manually and introduce a small delay for animation.
    screen.update()
    time.sleep(.1)

    # Move the snake and check for border crossing.
    snake.move()
    snake.border_crossing()

    # Python concept: Detect collision between the snake's head and the food.
    if snake.head.distance(food) < 20:
        food.refresh() # Python concept: Move the food to a new random location.
        scoreboard.increase_score() # Python concept: Increase the score and update the scoreboard display.

    # Detect collision with wall
    # Python concept: Check if the snake's head has gone beyond the screen boundaries.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False # Python concept: End the game if a wall collision occurs.
        scoreboard.reset() # Python concept: Reset the scoreboard and update high score.
        snake.reset_snake() # Python concept: Reset the snake to its starting state.
    
    # Detect collision with tail
    # Python concept: Iterate through snake segments to detect collision with itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False # Python concept: End the game if a tail collision occurs.
            scoreboard.reset() # Python concept: Reset the scoreboard and update high score.
            snake.reset_snake() # Python concept: Reset the snake to its starting state.

# Python concept: Exit the Turtle graphics window when the game loop finishes.
screen.exitonclick()






