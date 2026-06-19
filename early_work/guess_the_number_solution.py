"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Number Guessing Game ***
A command-line game where the user guesses a randomly generated number between 1 and 100.
The user chooses a difficulty level (easy or hard) which determines their number of attempts.

Python Concepts Highlighted:
- Random module imports for generating the target number (`from random import randint`)
- PEP 8 constants naming for defining difficulty turn counts (`EASY_LEVEL_TURNS`, `HARD_LEVEL_TURNS`)
- Function definition with parameters and return values for game modularity (`check_answer`, `set_difficulty`, `game`)
- Control flow structures for determining outcomes and game flow (`if/elif/else`, `while`)
- Type casting for converting string inputs into numeric comparison types (`int()`)
- Local variables and tracking state within running functions (`turns`, `guess`, `answer`)
"""

# Python concept: Importing specific functions and assets from modules using `from ... import`.
from random import randint
from art import logo

# Python concept: PEP 8 constants naming.
# Global variables defined in all-caps represent constants that should not be modified.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """
    Checks the user's guess against the target answer and prints feedback.

    Decrements the turns remaining if the guess is incorrect.

    Args:
        user_guess (int): The number guessed by the user.
        actual_answer (int): The correct target number.
        turns (int): The current number of remaining attempts.

    Returns:
        int: The updated number of turns remaining (decremented by 1 if incorrect).
    """
    # Python concept: `if/elif/else` conditional chain to determine feedback and update turns.
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        # Python concept: F-string for embedding target variable in output.
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    """
    Prompts the user to choose a game difficulty level.

    Sets the starting number of attempts based on the user's input.

    Returns:
        int: The number of turns assigned for the chosen difficulty.
    """
    # Python concept: `input()` to retrieve choice of difficulty level from the user.
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Python concept: `if/else` control flow to return the appropriate turn constant.
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    Executes the number guessing game.

    Handles the initialization of the secret number, sets difficulty,
    and manages the main loop prompting the user until they win or lose.

    Returns:
        None: This function executes the game flow and returns nothing.
    """
    print(logo)
    # Python concept: `randint()` from the `random` module to generate a pseudo-random integer.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    # Python concept: `while` loop that continues running until `guess` equals `answer`.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Python concept: `input()` to receive input and `int()` to type cast the input string.
        guess = int(input("Make a guess: "))
        
        # Python concept: Calling user-defined function `check_answer` and reassigning the return value.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            # Python concept: Early return using `return` to terminate the function.
            return
        elif guess != answer:
            print("Guess again.")


game()
