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

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time
from turtle import Screen

# Python concept: initialize the Turtle graphics window for the game.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Python concept: disable automatic screen updates for manual control.
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Python concept: module-level flag to keep the game loop running.
game_is_on = True


def end_game():
    """Stop the game loop when the quit key is pressed.

    Args:
        None

    Returns:
        None: Updates `game_is_on` to terminate the loop.
    """
    # Python concept: modify a module variable from inside a function.
    global game_is_on
    game_is_on = False

screen.listen()

# Python concept: bind arrow keys to snake movement methods.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Python concept: bind `q` to end the game gracefully.
screen.onkey(end_game, 'q')

while game_is_on:
    # Python concept: update the screen and pause briefly for animation.
    screen.update()
    time.sleep(.1)

    snake.move()
    snake.border_crossing()

    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.reset()
        snake.reset_snake()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
