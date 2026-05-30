# By Matt Lab
"""Udemy 100 Days of Code: Pay the Tab Roulette
This module provides a function to randomly select a person from a list,
simulating a "tab roulette" game to decide who pays the bill.

Python concepts highlighted:
- Importing the `random` module for random selections
- Function definition with optional arguments
- List data structure and `random.choice()`
- `if __name__ == '__main__':` idiom for demonstrating module usage
"""


import random

def who_pays(friends_list=None):
    """
    Randomly selects a person from a list to pay the bill.
    If no list is provided, it uses a default list of friends.

    Args:
        friends_list (list, optional): A list of names (strings) to choose from.
                                       Defaults to None, in which case a predefined list is used.

    Returns:
        str: The name of the randomly selected person.
    """
    # If no list is provided, use a default set of names.
    # Python concept: Checking for `None` to handle optional arguments.
    if friends_list is None:
        friends_list = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
    # Randomly pick one name from the list.
    # Python concept: `random.choice()` to select a single item from a list.
    payer = random.choice(friends_list)
    
    return payer # Optionally return the payer's name

# Python concept: The `if __name__ == "__main__"` block ensures this code
# only runs when the script is executed directly.
if __name__ == '__main__':
    # It demonstrates how to use the who_pays function.
    # Python concepts highlighted:
    # - Calling a function with its default argument
    print(f"The default payer is: {who_pays()}")
