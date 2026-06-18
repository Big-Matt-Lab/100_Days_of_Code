

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    
    
    def __init__(self, screen, name: str = "Player"):
        self.screen = screen
        self.left_name = name
        self.score = 0


        # screen dimensions 600 x 600
        half_w = self.screen.window_width() / 2
        top_y = self.screen.window_height() / 2 - 40
        