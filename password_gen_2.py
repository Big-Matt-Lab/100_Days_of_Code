""" Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Password Generator ***
Creating a password generator that uses random to generate a password to
spec (letters, number, special characters) than after the random selection
of the characters, randomizes the string again. Purposely not using 'secrets'
as it has not been introduced to the curriculum.

Python concepts highlighted:
- List data structures
- Function definitions and modularity
- `random` module usage (`choice`, `shuffle`)
- Control flow (`if/elif/else`, `for` loops)
- List comprehensions and string manipulation
"""

import random

# Python concept: String constants used as immutable sequences for random selection.
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
# Python concept: String containing valid digits.
NUMBERS = '0123456789'
# Python concept: String containing valid special characters.
SPECIALS = '!@#$%&'

def letter_generator(length, case):
    """
    Generates a list of random letters based on specified length and casing.

    Args:
        length (int): The desired number of letters.
        case (str): Casing option ('u' for uppercase, 'l' for lowercase, 'm' for mixed).

    Returns:
        list: A list of generated letter characters.

    Python concepts highlighted:
    - Function parameters and return values
    - `random.choice()` for random selection from a sequence
    - List comprehensions for concise list creation
    - `enumerate()` for accessing the index during iteration
    """
    # Generate base characters
    # Python concept: List comprehension for concise iteration and list creation.
    chars = [random.choice(LETTERS) for _ in range(length)]
    
    if case == 'u':
        # Python concept: List comprehension applying string method `upper()`.
        return [char.upper() for char in chars]
    elif case == 'm':
        # Python concept: List comprehension with ternary operator and `enumerate()` for index tracking.
        return [char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(chars)]
    
    # Fallback/Default to lowercase for 'l' and invalid inputs
    return [char.lower() for char in chars]

def number_generator(how_many):
    """
    Generates a list of random digits.

    Args:
        how_many (int): The number of random digits to generate.

    Returns:
        list: A list of generated numbers.

    Python concepts highlighted:
    - List comprehensions for concise list creation
    - `_` as a throwaway variable in a `for` loop
    """
    # Python concept: `_` used as a throwaway variable since the loop index isn't needed.
    return [random.choice(NUMBERS) for _ in range(how_many)]


def special_generator(how_many):
    """
    Generates a list of random special characters.

    Args:
        how_many (int): The number of random special characters to generate.

    Returns:
        list: A list of generated special characters.

    Python concepts highlighted:
    - List comprehensions for concise list creation
    - `_` as a throwaway variable in a `for` loop
    """
    # Python concept: Returning the result of a list comprehension directly.
    return [random.choice(SPECIALS) for _ in range(how_many)]


def main():
    """
    Main function to orchestrate password generation based on user input.

    Python concepts highlighted:
    Args:
        None

    Returns:
        None

    - Input collection and type conversion (`int()`)
    - `list.extend()` to combine lists
    - `random.shuffle()` for in-place list randomization
    - `"".join()` for combining list elements into a string
    """
    print("This is a configurable password generator.")
    # Python concept: Nested functions `int()` and `input()` for typed user input.
    length = int(input("How many letters?: "))
    case = input("Upper case, lower case, or mixed(u, l, or m): ")
    
    # Python concept: `in` operator to check membership against a list of valid options.
    if case not in ['u', 'l', 'm']:
        case = 'm'
    nums = int(input("How many numbers?:"))
    specials = int(input("How many special characters?: "))

    # Combine all generated characters into a single list
    # Python concept: Assigning the returned list to a variable.
    chars = letter_generator(length, case)
    if nums > 0:
        # Python concept: `list.extend()` adds elements from an iterable to the end of the list.
        chars.extend(number_generator(nums))
    if specials > 0:
        chars.extend(special_generator(specials))

    # Shuffle once and join into a final string
    # Python concept: `random.shuffle()` modifies the list in-place (returns None).
    random.shuffle(chars)
    # Python concept: `str.join()` concatenates an iterable of strings into a single string.
    password = "".join(chars)
    
    # Python concept: F-string for embedding variables directly into string literals.
    print(f"\n{password}")




if __name__ == "__main__":
    # This block executes when the script is run directly.
    # Python concepts highlighted:
    # - `if __name__ == '__main__':` idiom for script execution
    main()
