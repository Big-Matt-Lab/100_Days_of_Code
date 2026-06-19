"""Udemy - 100 Days of Code

*** Word List Loader and Filter ***
A utility script to load a list of words from a file and filter them
based on length.

Python concepts highlighted:
- File I/O with `with open()`
- List comprehensions for file reading
- `for` loops and `list.append()` for filtering
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
new_word_list = []
# Python concept: A standard `for` loop to iterate through a list.
for word in word_list:
    if len(word) > 3:
        # Python concept: `list.append()` to add items to a new list.
        new_word_list.append(word)
print(new_word_list)