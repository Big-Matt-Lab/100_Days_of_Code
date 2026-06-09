from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=500)

starting_color = screen.textinput(title="Etch a Sketch", prompt="Enter starting pen color:")

tim.teleport(-225, 0)

def move_forwards():
    tim.forward(2)

def move_backwards():
    tim.backward(2)

def turn_left():
    tim.left(1)

def turn_right():
    tim.right(1)

def clear_screen():
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
