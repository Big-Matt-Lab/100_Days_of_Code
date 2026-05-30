# By Matt Lab
"""Udemy 100 Days of Code: BMI Calculator
Calculates a user's Body Mass Index (BMI) based on weight and height, 
and provides a health condition classification.

Python concepts highlighted:
- Type conversion (`int()`)
- Mathematical operators (`/`, `**` for exponentiation)
- Built-in functions (`round()`)
- Conditional logic (`if/elif/else`)
- F-strings for formatted output
"""
# Python concepts highlighted (additional):
# - Type conversion (`int()`)

# Prompt user for input and convert strings to integers
# Python concept: `int()` function for type conversion from string to integer.
user_weight = int(input("What is your weight? \n"))
user_height = int(input("What is your height(in inches)? \n"))

# Convert weight and height to metric system equivalents (approximate)
# Python concept: `/` operator for division.
weight = user_weight / 2.2 # Convert pounds to kilograms (approx. 1 kg = 2.2 lbs)
height = user_height / 39.2 # Convert inches to meters (approx. 1 meter = 39.37 inches, using 39.2 for simplicity)

# Calculate BMI: weight (kg) divided by height (m) squared, rounded to nearest whole number
# Python concept: `**` operator for exponentiation (power of).
# Python concept: `round()` built-in function to round a number.
bmi = round(weight / height ** 2)
# Python concept: F-string for embedding variables in a string.
print(f"Your BMI is: {bmi}")

# Determine the weight classification based on standard BMI thresholds
# Python concept: `if/elif/else` chain for conditional logic.
if bmi < 18.5:
    condition = "underweight"
elif bmi <= 25:
    condition = "at a normal weight"
else:
    condition = "overweight"

print(f"You are {condition}.")