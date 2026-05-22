"""Udemy 100 Days of Code: BMI Calculator

Calculates a user's Body Mass Index (BMI) based on weight and height, 
and provides a health condition classification.

Python concepts highlighted:
- Type conversion ('int()')
- Mathematical operators ('/', '**' for exponentiation)
- Built-in functions ('round()')
- Conditional logic ('if/elif/else')
"""

# Prompt user for input and implicitly convert strings to integers
user_weight = int(input("What is your weight? \n"))
user_height = int(input("What is your height(in inches)? \n"))

# Convert weight and height to metric system equivalents (approximate)
weight = user_weight / 2.2
height = user_height / 39.2

# Calculate BMI: weight (kg) divided by height (m) squared, rounded to nearest whole number
bmi = round(weight / height ** 2)
print(f"Your BMI is: {bmi}")

# Determine the weight classification based on standard BMI thresholds
if bmi < 18.5:
    condition = "underweight"
elif bmi <= 25:
    condition = "at a normal weight"
else:
    condition = "overweight"

print(f"You are {condition}.")