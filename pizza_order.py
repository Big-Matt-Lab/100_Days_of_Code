"""Udemy 100 Days of Code: Pizza Order Program

Calculates the total cost of a pizza based on user's choice of size and toppings.

Python concepts highlighted:
- String manipulation methods ('strip', 'lower') for input sanitization
- Control flow with 'if/elif/else' statements
- Augmented assignment operators ('+=')
- F-string formatting to display floats as currency
"""

print("Welcome to the Python Pizza Delivery Company")

# Get user input and sanitize using strip() and lower() to handle accidental spaces or caps
size = input("What size pizza would you like? S, M , or L: ").strip().lower()
pepperoni  = input("Would you like pepperoni on your pizza? Y or N: ").strip().lower()
extra_cheese  = input("Would you like extra cheese on your pizza? Y or N: ").strip().lower()

# Determine base price based on pizza size
cost = 0
if size == 's':
    cost += 15
elif size == 'm':
    cost += 20
else:
    cost += 25

# Add additional costs for pepperoni depending on pizza size
if pepperoni == 'y':
    if size == 's':
        cost += 2
    else:
        cost += 3

# Add additional cost for extra cheese (flat rate regardless of size)
if extra_cheese == 'y':
    cost += 1

# Output the final cost formatted to 2 decimal places
print(f"The cost for your pizza today is ${cost:.2f}")
