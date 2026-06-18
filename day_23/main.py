
"""
placeholder for docstring
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.title("Frogger Game")
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player()
car = CarManager()

SCREEN.listen()

SCREEN.onkey(player.go_up, "Up")
# SCREEN.onkey(car.left, "Left")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    SCREEN.update()
    car.left()

