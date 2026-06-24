"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Analyzing Squirrel Census Data with Pandas ***
This script demonstrates how to use the `pandas` library to analyze squirrel census data.
It reads a CSV file containing information about squirrels, calculates the counts of squirrels
for different primary fur colors, and then saves these counts into a new CSV file.

Python Concepts Highlighted:
- `pandas` library for data manipulation (`pd.read_csv`, `DataFrame`, `Series`, filtering, `to_csv`)
- Reading and writing CSV files.
- Data filtering and aggregation (`==`, `.sum()`)
- Dictionary creation and conversion to `DataFrame`.
- Basic data analysis to count occurrences of categorical data.
"""

import pandas as pd

# Read the squirrel data from the `squirrel_data.csv` file into a pandas DataFrame.
data = pd.read_csv("squirrel_data.csv")

# Calculate the number of squirrels for each primary fur color.
# This is done by filtering the 'Primary Fur Color' column for each color
# and then using `.sum()` on the resulting boolean Series to count `True` values.
gray_count = (data["Primary Fur Color"] == "Gray").sum()
black_count = (data["Primary Fur Color"] == "Black").sum()
cinnamon_count = (data["Primary Fur Color"] == "Cinnamon").sum()

# Create a dictionary to hold the fur colors and their corresponding counts.
# This dictionary will be used to create a new DataFrame.
fur_color_dict = {
    'fur colors': ['gray', 'black', 'cinnamon'],
    'counts': [gray_count, black_count, cinnamon_count]
}

# Create a new pandas DataFrame from the `fur_color_dict`.
color_count = pd.DataFrame(fur_color_dict)
# Save the `color_count` DataFrame to a new CSV file named `squirrel_colors.csv`.
# `index=False` prevents `pandas` from writing the DataFrame index as a column in the CSV.
color_count.to_csv("squirrel_colors.csv", index=False)
