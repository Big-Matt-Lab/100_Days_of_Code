""" Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Password Generator ***
Creating a password generator that uses random to generate a password to
spec (letters, number, special characters) than after the random selection
of the characters, randomizes the string again. Purposely not using 'secrets'
as it has not been introduced to the curriculum.
"""
# Python concepts highlighted:
# - List data structures
# - Function definitions and modularity
# - `random` module usage (`choice`, `shuffle`)
# - Control flow (`if/elif/else`, `for` loops)
# - String and list manipulation

import random

# Python concept: Lists used to store character sets.
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SPECIALS = ['!', '@', '#', '$', '%', '&']

def letter_generator(length, case):
    """
    Generates a list of random letters based on specified length and casing.

    Args:
        length (int): The desired number of letters.
        case (str): Casing option ('u' for uppercase, 'l' for lowercase, 'm' for mixed).

    Returns:
        list: A list of generated letter characters.
    """
    letter_share = []
    # Python concept: `enumerate` provides an index `i` along with the item.
    # Here, `range` is used, so `i` is just the loop counter.
    for i in range(length):
        # Python concept: `random.choice` selects one item from a list.
        chosen_letter = random.choice(LETTERS)
        if case == 'u':
            # All letters should be uppercase
            # Python concept: `str.upper()` converts a string to uppercase.
            letter_share.append(chosen_letter.upper())
        elif case == 'l':
            # All letters should be lowercase
            # Python concept: `str.lower()` converts a string to lowercase.
            letter_share.append(chosen_letter.lower())
        elif case == 'm':
            # For mixed case, alternate between upper and lower based on index
            # Python concept: Modulo operator `%` to check for even/odd index.
            if i % 2 == 0: # Even index (0, 2, 4...), make it lowercase
                letter_share.append(chosen_letter.lower())
            else: # Odd index (1, 3, 5...), make it uppercase
                letter_share.append(chosen_letter.upper())
        else:
            # Fallback for invalid 'case' input, default to lowercase
            # Python concept: `list.append()` adds an item to the end of a list.
            letter_share.append(chosen_letter.lower())
    return letter_share

def number_generator(how_many, alphas):
    """
    Appends a specified number of random digits to an existing list.

    Note: This function modifies the list passed to it (a side effect).

    Args:
        how_many (int): The number of random digits to generate and append.
        alphas (list): The list to which numbers will be appended.

    Returns:
        list: The modified list with numbers appended.
    """
    # Python concept: `_` used as a throwaway variable when the loop counter is not needed.
    for _ in range(how_many):
        alphas.append(random.choice(NUMBERS))
    return alphas


def special_generator(how_many, char_list):
    """
    Appends a specified number of random special characters to an existing list.

    Note: This function modifies the list passed to it (a side effect).

    Args:
        how_many (int): The number of special chars to generate and append.
        char_list (list): The list to which special chars will be appended.

    Returns:
        list: The modified list with special chars appended.
    """
    for _ in range(how_many):
        char_list.append(random.choice(SPECIALS))
    return char_list


def main():
    """Main function to drive the password generation process."""
    print("This is a configurable password generator.")
    # Python concept: `int()` to convert string input to an integer.
    length = int(input("How many letters?: "))
    case = input("Upper case, lower case, or mixed(u, l, or m): ")
    # Python concept: `in` operator to check for membership in a list.
    if case not in ['u', 'l', 'm']:
        case = 'm'
    nums = int(input("How many numbers?:"))
    specials = int(input("How many special characters?: "))

    # Generate the initial list of letters.
    alphas = letter_generator(length, case)

    # Conditionally add numbers and special characters.
    if nums > 0:
        alpha_numerics = number_generator(nums, alphas)
    else:
        alpha_numerics = alphas

    if specials > 0:
        # The list `alpha_numerics` (which is the same object as `alphas`) is modified in place.
        chars = special_generator(specials, alpha_numerics)
    else:
        chars = alpha_numerics

    # This loop is redundant; one shuffle is sufficient.
    for _ in range(5):
        # Python concept: `random.shuffle` shuffles a list in-place.
        random.shuffle(chars)
        print(chars)
    
    # Python concept: A generator expression inside `join` to convert all items
    # (including integers) to strings before joining.
    password = "".join(str(char) for char in chars)
    
    # Python concept: F-string for formatted output.
    print(f"\n{password}")



# Python concept: The `if __name__ == "__main__"` block ensures this code
# only runs when the script is executed directly.
if __name__ == "__main__":
    main()
