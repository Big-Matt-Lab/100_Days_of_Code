""" Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Password Generator ***
Creating a password generator that uses random to generate a password to
spec (letters, number, special characters) than after the random selection
of the characters, randomizes the string again. Purposely not using 'secrets'
as it has not been introduced to the curriculum.
"""

import random

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SPECIALS = ['!', '@', '#', '$', '%', '&']

def letter_generator(length, case):
    letter_share = []
    for i in range(length):
        chosen_letter = random.choice(LETTERS)
        if case == 'u':
            # All letters should be uppercase
            letter_share.append(chosen_letter.upper())
        elif case == 'l':
            # All letters should be lowercase
            letter_share.append(chosen_letter.lower())
        elif case == 'm':
            # For mixed case, alternate between upper and lower based on index
            if i % 2 == 0: # Even index (0, 2, 4...), make it lowercase
                letter_share.append(chosen_letter.lower())
            else: # Odd index (1, 3, 5...), make it uppercase
                letter_share.append(chosen_letter.upper())
        else:
            # Fallback for invalid 'case' input, default to lowercase
            letter_share.append(chosen_letter.lower())
    return letter_share

def number_generator(how_many, alphas):
    for _ in range(how_many):
        alphas.append(random.choice(NUMBERS))
    return alphas


def special_generator(how_many, char_list):
    for _ in range(how_many):
        char_list.append(random.choice(SPECIALS))
    return char_list


def main():
    print("This is a configurable password generator.")
    length = int(input("How many letters?: "))
    case = input("Upper case, lower case, or mixed(u, l, or m): ")
    if case not in ['u', 'l', 'm']:
        case = 'm'
    nums = int(input("How many numbers?:"))
    specials = int(input("How many special characters?: "))

    alphas = letter_generator(length, case)

    if nums > 0:
        alpha_numerics = number_generator(nums, alphas)
    else:
        alpha_numerics = alphas

    if specials > 0:
        chars = special_generator(specials, alpha_numerics)
    else:
        chars = alpha_numerics

    
    for _ in range(5):
        random.shuffle(chars)
        print(chars)
    
    password = "".join(str(char) for char in chars)
    
    print(f"\n{password}")




if __name__ == "__main__":
    main()
