"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Miles to Kilometers Converter ***
This program creates a simple GUI application using Python's `tkinter` library
to convert a value entered in miles to its equivalent in kilometers.

Python Concepts Highlighted:
- `tkinter` for GUI development (`tk.Tk`, `tk.Label`, `tk.Entry`, `tk.Button`)
- Event handling for button clicks (`command` attribute)
- Data type conversion (`float()`)
- String formatting for output (`f-strings`)
- Error handling with `try-except` blocks for `ValueError`
- Widget positioning using `grid()` layout manager
- Global variable usage for GUI components (`entry`, `result_label`)
"""

import tkinter as tk

def calculate_km():
    """Calculates the equivalent kilometers from the miles value entered by the user.

    This function retrieves the current value from the `entry` widget, converts it to a float,
    performs the conversion to kilometers, and updates the `result_label` with the calculated value.
    It includes error handling for invalid input.

    Args:
        None (reads directly from the global `entry` widget).

    Returns:
        None (updates the global `result_label` widget directly).
    """ 
    try:
        # 1. Get the string from entry right now and convert to float
        miles_value = float(entry.get())
        # 2. Convert miles to kilometers
        km_value = miles_value * 1.60934
        # 3. Update the label text with the result
        result_label.config(text=f"Result: {km_value:.2f} km")
    except ValueError:
        # Handles cases where the user typed text instead of numbers
        result_label.config(text="Please enter a valid number")


# --- GUI Setup --- #
# Initializes the main window and configures its properties.
window = tk.Tk()
# Sets the minimum size of the window to 500 pixels wide and 200 pixels high.
window.minsize(width=500, height=200)
# Configures the first column (index 1) of the grid to have a minimum width of 100 pixels.
window.grid_columnconfigure(1, minsize=100)


# --- Widgets --- #
# Labels are used to display static text or results in the GUI.

# `title_label`: Displays the main title of the application.
title_label = tk.Label(text="Miles to Kilometers Calculator", font=("Arial", 20, "bold"))
title_label.grid(column=1, row=0, padx=20)

enter_miles_label = tk.Label(text="Enter miles:", font=("Arial", 16, "bold"), padx=50)
# Positions the `enter_miles_label` in the grid at column 0, row 1.
enter_miles_label.grid(column=0, row=1)

# `result_label`: Displays the conversion result. Initially set to "Result: 0 km".
result_label = tk.Label(text="Result: 0 km", font=("Arial", 16, "bold"))
result_label.grid(column=1, row=3)


# Entries allow users to input text.
# `entry`: An input field for the user to type in the miles value.
entry = tk.Entry(width=10)
# Inserts an empty string as initial text, clearing any default placeholder.
entry.insert(tk.END, string="")
# Positions the `entry` widget in the grid at column 1, row 1.
entry.grid(column=1, row=1)


# Buttons are interactive widgets that trigger functions when clicked.

# `button`: Triggers the `calculate_km` function when clicked. `command` links the button to the function.
# Note: No parentheses after `calculate_km` because we are passing the function reference, not calling it immediately.
button = tk.Button(text="Calculate", command=calculate_km, font=("Arial", 14, "bold"))
button.grid(column=1, row=2, pady=5)



window.mainloop()