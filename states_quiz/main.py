
import pandas
import turtle

IMAGE = "blank_states_img.gif"



screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the state:", prompt="Guess another state's name:")
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())


print(answer_state)





screen.exitonclick()
