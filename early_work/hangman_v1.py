""" Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Hangman Game ***
A classic word-guessing game where the player tries to guess a secret word
letter by letter.

Python concepts highlighted:
- `random` module for word selection
- File I/O with `with open()`
- List comprehensions for data filtering
- `str` and `list` manipulation
- `set` for tracking unique guesses
- `while` loops for game flow control
- Conditional logic (`if`/`elif`)
- F-strings for formatted output
"""

import random

def load_words(word_list):
    """Loads words from a text file into a list."""
    # Python concept: The `with` statement ensures the file is properly closed.
    with open(word_list, 'r') as file:
        # Read lines, strip whitespace, and convert to lowercase
        # Python concept: List comprehension for creating a new list concisely.
        words = [line.strip().lower() for line in file.readlines()]
    return words

word_list = load_words('word_list.txt')
# Python concept: List comprehension to filter the list for words of a certain length.
new_word_list = [word for word in word_list if len(word) > 3]

# Python concept: `random.choice()` selects a random item from a sequence.
chosen_word = random.choice(new_word_list)
word_length = len(chosen_word)

# In lieu of ASCII art, we will present a series of messages as lives are lost
# demonstrating string retrieval from a list base on index
lives_lost_messages = [
    'That was your last try', 'Be careful, only one life left',
    'The end is near', 'Not looking good, three lives left',
    'Another life gone', 'That will cost you one life']

# Python concept: List multiplication to create a list with repeated elements.
display = ['_'] * word_length
# Python concept: F-strings for easy embedding of variables in strings.
print(f"Welcome to Hangman! Your word has {word_length} letters.")
# Python concept: `str.join()` to convert a list of characters into a single string for display.
print(f"{' '.join(display)}")

game_over = False
lives = 6
# Python concept: A `set` is used to store guessed letters. Sets are highly efficient
# for checking if an item is present and automatically handle duplicates.
guessed_letters = set()

# Python concept: A `while` loop to continue the game as long as `game_over` is False.
while not game_over:
    # Python concept: `strip()` and `lower()` to sanitize user input.
    guess = input("Pick a single letter: ").strip().lower()

    # Input validation: ensure it's a single letter.
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        # Python concept: `continue` skips the rest of the loop and starts the next iteration.
        continue

    # Check if the letter has already been guessed.
    # Python concept: Fast membership testing with a `set`.
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    # Python concept: `set.add()` to add the new guess to the set of guessed letters.
    guessed_letters.add(guess)

    # Update the display list with the new guess.
    # Python concept: `range()` to loop through indices of the word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # A guess is incorrect if it's not in the chosen word.
    # Python concept: Augmented assignment operator `-=` to decrement lives.
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. {lives_lost_messages[lives]}")

    print(f"{' '.join(display)}")
    # Python concept: `sorted()` returns a new sorted list from an iterable.
    print(f"Your picks: {', '.join(sorted(guessed_letters))}")

    # Check if the player has won.
    if "_" not in display:
        game_over = True
        print("You won!")
    # Check if the player has lost.
    elif lives == 0:
        game_over = True
        print("You lost!")
        print(f"The word was '{chosen_word}'.")
