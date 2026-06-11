
import random
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
        self.increase_score()
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))
        