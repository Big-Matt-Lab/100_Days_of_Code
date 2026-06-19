# By Matt Lab
"""Udemy 100 Days of Code: Pizza Order Program
Calculates the total cost of a pizza based on user's choice of size and toppings.

Python concepts highlighted:
- String manipulation methods (`strip`, `lower`) for input sanitization
- Control flow with `if/elif/else` statements
- Augmented assignment operators (`+=`)
- F-string formatting to display floats as currency
# Python concepts highlighted (additional):
# - Basic arithmetic operations
"""

print("Welcome to the Python Pizza Delivery Company")

# Get user input and sanitize using strip() and lower() to handle accidental spaces or caps
# Python concept: Chaining string methods for input sanitization.
size = input("What size pizza would you like? S, M , or L: ").strip().lower()
pepperoni  = input("Would you like pepperoni on your pizza? Y or N: ").strip().lower()
extra_cheese  = input("Would you like extra cheese on your pizza? Y or N: ").strip().lower()

# Determine base price based on pizza size
cost = 0
# Python concept: `if/elif/else` block to handle mutually exclusive conditions.
if size == 's':
    cost += 15 # Python concept: Augmented assignment operator `+=`.
    # Small pizza base price
elif size == 'm':
    cost += 20
    # Medium pizza base price
else:
    cost += 25 # Assumes 'L' or any other input defaults to Large.
    # Large pizza base price

# Add additional costs for pepperoni depending on pizza size
if pepperoni == 'y':
    if size == 's':
        cost += 2
        # Small pizza pepperoni cost
    else:
        cost += 3
        # Medium/Large pizza pepperoni cost

# Add additional cost for extra cheese (flat rate regardless of size)
if extra_cheese == 'y':
    cost += 1

# Output the final cost formatted to 2 decimal places for currency.
# Python concept: F-string with format specifier `:.2f` for floating point numbers.
print(f"The cost for your pizza today is ${cost:.2f}")
