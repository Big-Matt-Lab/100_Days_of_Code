"""
This program implements a simple number guessing game. It prompts the
user for an upper bound to set the difficulty level, generates a random
number, and then gives hints until the user guesses correctly.

Python concepts highlighted:
- Random number generation (random.randint)
- Exception handling (ValueError)
- Infinite loops with breaking conditions
- Input validation and type casting
"""

import random

EASY_GAME = 10
HARD_GAME = 5


def configure_game():
    """Uses random to create the number to be guessed.
    return: int: secret number
    """
    number = random.randint(1, 101)
    return number


def turns_limit():
    """Prompts the user to determine a limit of number of
    turns and validates that it is a positive integer.
    return: int: The maximum number of turns
    """
    while True:
        try:
            difficulty = int(input("Select difficulty (Easy - 1, Hard - 2): "))
            if difficulty not in (1, 2):
                print("Please enter a either a 1 or 2.")
                continue
            else:
                if difficulty == 1:
                    return EASY_GAME
                else:
                    return HARD_GAME
        except ValueError:
            print("Please enter a valid number.")
            continue


def get_user_guess():
    """Prompts the user for a guess and validates that it is a positive integer.
    return: int: The validated user guess.
    """

    while True:
        guess = ""
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            else:
                break
        except ValueError:
            continue
    return guess


def main():
    """
    Main game loop. Orchestrates the game flow, and win/loss conditions.
    """
    # Clear screen
    print("\n" * 20)
    # Allow replay of game
    play = True
    while play:
        number = configure_game()
        turns = turns_limit()

        print("I am thinking of a number between 1 and 100.")
        # Get user guess
        while turns > 0:
            print(f"You have {turns} turns remaining.")
            turns -= 1
            guess = get_user_guess()
            if guess == number:
                print("Correct!")
                break
            elif guess < number:
                print("Too low!")
                print("Guess again.")
            else:
                print("Too high!")
                print("Guess again.")
        else:
            print("Out of turns")
        play_again = input("Game over. Play again? (y or n): ")
        if play_again != 'y':
            play = False


if __name__ == "__main__":
    main()
