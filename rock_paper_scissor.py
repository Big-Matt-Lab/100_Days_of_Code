"""
Udemy 100 Days of Code
 
Rock Paper Scissors Game

A simple game of Rock, Paper, Scissors against the computer.

Python concepts highlighted:
- The 'random' module for generating random choices
- Dictionary usage for mapping choices to names
- Input sanitization ('strip', 'lower')
- Input validation using a loop
- Concise game logic using modular arithmetic (alternative to extensive if/else)
"""

import random

# Map choices to numbers: 0: Paper, 1: Scissors, 2: Rock.
# This specific numerical assignment (Paper=0, Scissors=1, Rock=2)
# is crucial for the modular arithmetic logic to work correctly.
PLAYS = {0: 'paper', 1: 'scissors', 2: 'rock'}

def play_rock_paper_scissors():
    """
    Plays a single round of Rock, Paper, Scissors.
    """
    print("Let's play Rock, Paper, Scissors!")

    # Get computer's random choice (0, 1, or 2)
    computer_choice_num = random.randint(0, 2)

    # Get user input and validate it, mapping 'r', 'p', 's' to 2, 0, 1 respectively.
    # Using a dictionary for mapping input characters to numbers is more concise.
    input_to_num = {'p': 0, 's': 1, 'r': 2}
    player_choice_num = None # Initialize with an invalid value
    while player_choice_num is None:
        player_input = input("Enter R for rock, P for paper or S for scissors: ").strip().lower()
        player_choice_num = input_to_num.get(player_input)
        if player_choice_num is None: # If input_to_num.get() returned None, it was an invalid input
            print("Invalid entry. Please enter R, P, or S.")

    player_call = PLAYS[player_choice_num]
    computer_call = PLAYS[computer_choice_num]

    # Display choices
    print(f"Player chose: {player_call}")
    print(f"Computer chose: {computer_call}")

    # Game logic using modular arithmetic.
    # The formula (player_choice_num - computer_choice_num + 3) % 3
    # calculates the outcome:
    # - If the result is 0, it's a tie.
    # - If the result is 1, the player wins.
    # - If the result is 2, the computer wins.
    # The '+ 3' ensures that the result of the subtraction is always non-negative
    # before the modulo operation, which is important for consistent results
    # when dealing with negative differences (e.g., 0 - 2 = -2, but -2 % 3 = 1 in Python).
    outcome = (player_choice_num - computer_choice_num + 3) % 3

    if outcome == 0:
        print("It's a tie!")
    elif outcome == 1:
        print("Player wins!")
    else: # outcome == 2
        print("Computer wins!")

if __name__ == "__main__":
    play_rock_paper_scissors()
