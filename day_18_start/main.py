#
import random
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(1, 1, 2)
t.pensize(1)
t.speed(20)
SCREEN = turtle.Screen()
SCREEN.colormode(255)


def color_generator():
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


for _ in range(72):
    t.setheading(t.heading() + 5)
    t.circle(100)
    t.pencolor(color_generator())






SCREEN.exitonclick()
