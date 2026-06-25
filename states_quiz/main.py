
"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** US States Game ***
This program implements a game where the user has to guess the names of US states.
The game displays a map of the US and prompts the user to enter state names.
If the guess is correct, the state name is written on the map.
The game keeps track of correct guesses and, upon exiting, saves the un-guessed states to a CSV file.

Python Concepts Highlighted:
- `turtle` module for graphical user interface and drawing (`turtle.Screen`, `turtle.Turtle`, `screen.textinput`)
- `pandas` library for data manipulation and CSV file handling (`pd.read_csv`, `DataFrame`, `Series`, `to_list`, `to_csv`)
- List manipulation for tracking guessed and missing states (`append`, `len`)
- Conditional statements for game logic (`if/else`)
- Loops for continuous gameplay (`while` loop)
- String manipulation for input processing (`title()`)
- F-strings for dynamic title updates
"""

import turtle
import pandas as pd
import time

# Define the image file for the game map.
IMAGE = "blank_states_img.gif"

# Set up the turtle screen.
screen = turtle.Screen()
screen.title("US States Game")
# Add the state map image as a shape to the turtle screen.
screen.addshape(IMAGE)
# Set the turtle\'s shape to the added image.
turtle.shape(IMAGE)

# Read the 50_states.csv file into a pandas DataFrame.
data = pd.read_csv("50_states.csv")
# Extract all state names from the DataFrame and convert them to a list.
all_states = data.state.to_list()
# Initialize an empty list to store states guessed correctly by the user.
guessed_states = []
# Define the filename for saving missing states.
file_to_save = "states_to_learn.csv"

# Main game loop: continues until all 50 states are guessed.
while len(guessed_states) < 50:
    # Prompt the user for a state name. The title shows current progress.
    # The input is converted to title case for consistent comparison.
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="What\'s another state\'s name?").title()
    
    # Check if the user wants to exit the game.
    if answer_state == "Exit":
        break

    # Check if the guessed state is in the list of all US states.
    if answer_state in all_states:
        # Add the correctly guessed state to the `guessed_states` list.
        guessed_states.append(answer_state)
        # Create a new Turtle object to write the state name on the map.
        t = turtle.Turtle()
        # Hide the turtle icon.
        t.hideturtle()
        # Lift the pen to prevent drawing lines when moving.
        t.penup()
        # Get the row of data corresponding to the guessed state.
        state_data = data[data.state == answer_state]
        # Move the turtle to the state\'s coordinates on the map.
        # `item()` is used to extract the scalar value from the pandas Series.
        t.goto(state_data.x.item(), state_data.y.item())
        # Write the state name on the map.
        t.write(answer_state)
        # Pause for 1 second to allow the user to see the written state.
        time.sleep(1)

# Convert the list of all states into a pandas Series for easier set operations.
missing_states = pd.DataFrame([state for state in all_states if state not in guessed_states])

# Save the identified missing states to a new CSV file named `states_to_learn.csv`.
# `index=False` prevents writing the DataFrame index as a column.
# `header=["missing_states"]` sets the column header for the output CSV.
missing_states.to_csv(file_to_save, index=False, header=["missing_states"])

# Inform the user that the game is over and where the missing states are saved.
print(f"Game over! Missing states saved to: {file_to_save}")
