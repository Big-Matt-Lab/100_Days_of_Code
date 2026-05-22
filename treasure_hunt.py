# By Matt Lab
"""Udemy 100 Days of Code: Treasure Island

A text-based adventure game where the user makes choices to find the hidden treasure.

Python concepts highlighted:
- The 'sys' module for exiting the program early ('sys.exit()')
- Multiline strings ('\"\"\"') for displaying long menus
- Input sanitization ('strip()', 'lower()')
- Sequential logic and guard clauses to keep code flat (avoiding deep nesting)
"""


import sys

print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure.")

# Game starts - linear game flow using guard clauses
print("You know the treasure is here, somewhere.")
print("Follow your instincts and maybe, just maybe, you will find the treasure!")
print("\n")

# First checkpoint: Beach or Jungle
print("You've landed on a beach and need to move - which way to go?")
print("""A - Stay on the beach and move around the island or
      B - Head into the jungle.""")
move_1 = input("A - Beach or B - Jungle: ").strip().lower()
if move_1 != 'a':
    print("You've made a poor decision. You've fallen into a hole.")
    print("Game over!")
    sys.exit()

print("Congratulations, you are heading the right way!")

# Second checkpoint: Boat or Inland
print("Uh oh, a stone jetty blocks your path. There is an old boat on the beach.")
print("A - Take the boat and row around the jetty or B - move inland?")
move_2 = input("A - Boat or B - Inland?: ").strip().lower()
if move_2 != 'b':
    print("You've made a poor decision. The boat is leaking and sinking quickly.")
    print("Game over!")
    sys.exit()

print("Whew, that was the correct choice!")

# Third checkpoint: Multiple doors
print("You've come to an ancient wall with three doors")
print("Choose which door to pass through.")
print("The doors are red, blue and green.")
print("Choose R for the Red door, B for the blue door and G for the green door.")
move_3 = input("R - Red or B - Blue or G - Green?: ").strip().lower()
if move_3 == 'b':
    print("Hooray, you've found the treasure!")
    print("You've won!")
    sys.exit()
if move_3 == 'r':
    print("A bad decision. There is a roaring fire and you've been burned.")
    print("Game over!")
    sys.exit()
elif move_3 == 'g':
    print("Ferocious beasts were just beyond the door. Ouch")
    print("Game over!")
    sys.exit()
else:
    print("Oops, that was incorrect")
    print("This isn't going to end well for you")
    print("Game over!")
