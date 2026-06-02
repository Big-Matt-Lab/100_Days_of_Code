"""
This program implements a simple number guessing game. It prompts the
user for a difficulty level, generates a random number between 1 and 100,
and then gives hints until the user guesses correctly or runs out of turns.

Python concepts highlighted:
- Random number generation (random.randint)
- Exception handling (try-except for ValueError)
- Constants for configuration
- Input validation and type casting
- Modular functions
"""

import random

# --- Game Configuration Constants ---
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
DIFFICULTY_EASY = 1
DIFFICULTY_HARD = 2
NUMBER_MIN = 1
NUMBER_MAX = 100
# ------------------------------------


def configure_game():
    """Generates the random number to be guessed.

    Returns:
        int: The secret number between NUMBER_MIN and NUMBER_MAX.
    """
    print(f"I am thinking of a number between {NUMBER_MIN} and {NUMBER_MAX}.")
    return random.randint(NUMBER_MIN, NUMBER_MAX)


def select_difficulty():
    """Prompts the user to select a difficulty and returns the turn limit.

    Returns:
        int: The maximum number of turns for the selected difficulty.
    """
    while True:
        try:
            difficulty = int(input(f"Select difficulty (Easy - {DIFFICULTY_EASY}, Hard - {DIFFICULTY_HARD}): "))
            if difficulty == DIFFICULTY_EASY:
                return EASY_LEVEL_TURNS
            elif difficulty == DIFFICULTY_HARD:
                return HARD_LEVEL_TURNS
            else:
                print(f"Invalid selection. Please enter either {DIFFICULTY_EASY} or {DIFFICULTY_HARD}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_user_guess():
    """Prompts the user for a guess and validates that it is an integer
    within the game's number range.

    Returns:
        int: The validated user guess.
    """
    while True:
        try:
            guess = int(input("Make a guess: "))
            if NUMBER_MIN <= guess <= NUMBER_MAX:
                return guess
            else:
                print(f"Your guess must be between {NUMBER_MIN} and {NUMBER_MAX}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """
    Main function to orchestrate the game flow, including the replay loop,
    turn management, and win/loss conditions.
    """
    while True:
        # Clear screen for a new game
        print("\n" * 20)
        print("--- Welcome to the Number Guessing Game! ---")

        number_to_guess = configure_game()
        turns = select_difficulty()

        # Game loop
        while turns > 0:
            print(f"\nYou have {turns} attempts remaining to guess the number.")
            guess = get_user_guess()
            turns -= 1

            if guess == number_to_guess:
                print(f"You got it! The answer was {number_to_guess}.")
                break
            elif guess < number_to_guess:
                print("Too low.")
            else:
                print("Too high.")

            if turns > 0:
                print("Guess again.")
            else:
                print("You've run out of guesses, you lose.")
                print(f"The correct number was {number_to_guess}.")

        if input("\nPlay again? (y/n): ").lower() != 'y':
            break


if __name__ == "__main__":
    main()
