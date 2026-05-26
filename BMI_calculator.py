# By Matt Lab
"""Udemy 100 Days of Code: BMI Calculator

Calculates a user's Body Mass Index (BMI) based on weight and height, 
and provides a health condition classification.

Python concepts highlighted:
- Type conversion ('int()')
- Mathematical operators ('/', '**' for exponentiation)
- Built-in functions ('round()')
- Conditional logic ('if/elif/else')
# Python concepts highlighted (additional):
# - Type conversion (`int()`)
"""

# Prompt user for input and implicitly convert strings to integers
user_weight = int(input("What is your weight? \n"))
user_height = int(input("What is your height(in inches)? \n"))
# Assuming weight in pounds and height in inches for input
user_weight_lbs = int(input("What is your weight (in pounds)? \n"))
user_height_inches = int(input("What is your height (in inches)? \n"))

# Convert weight and height to metric system equivalents (approximate)
weight = user_weight / 2.2 # Convert pounds to kilograms (approx. 1 kg = 2.2 lbs)
height = user_height / 39.2 # Convert inches to meters (approx. 1 meter = 39.37 inches, using 39.2 for simplicity)
# More precise conversion factors: 1 kg = 2.20462 lbs, 1 meter = 39.3701 inches
weight_kg = user_weight_lbs / 2.20462
height_m = user_height_inches / 39.3701

# Calculate BMI: weight (kg) divided by height (m) squared, rounded to nearest whole number
bmi = round(weight / height ** 2)
print(f"Your BMI is: {bmi}")
# BMI is often reported with one decimal place for better precision
bmi = round(weight_kg / height_m ** 2, 1)
print(f"Your BMI is: {bmi:.1f}")

# Determine the weight classification based on standard BMI thresholds
if bmi < 18.5:
    condition = "underweight"
elif bmi <= 25:
    condition = "at a normal weight"
else:
    condition = "overweight"

print(f"You are {condition}.")