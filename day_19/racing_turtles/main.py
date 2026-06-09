
import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
X_START = -350
Y_START = -200
Y_INCREMENT = 35
END_POSITION = 350
y_position = Y_START
all_turtles = []

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.teleport(X_START, y_position)
    y_position += Y_INCREMENT
    all_turtles.append(t)
racing =True
count = 0
while racing:
    for turtle in all_turtles:
        count += 1
        if turtle.xcor() > END_POSITION:
            racing = False
            print(f"The {turtle.color()[0]} turtle has won the race!")
            break
        turtle.forward(random.randint(1, 10))

screen = Screen()


screen.exitonclick()
print(f"Total number of moves: {count}")