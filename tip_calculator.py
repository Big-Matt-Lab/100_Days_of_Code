# By Matt Lab
"""Udemy 100 Days of Code: Tip Calculator and Bill Splitter

This program calculates tip amounts, total bill, and can split the bill
among multiple diners. It also integrates with a 'tab roulette' module
to randomly select who pays.

Python concepts highlighted:
- Function definitions and modularity
- Input validation with `while` loops and `try-except` blocks
- String manipulation (`strip`, `lower`, `title`)
- F-strings for formatted output
- List manipulation (appending, checking length)
- Importing and using custom modules
"""

import pay_the_tab_roulette # Import the module

def tip_calc(tab, tip_percent):
    """
    Calculates the tip amount and total bill.

    Args:
        tab (float): The initial bill amount.
        tip_percent (float): The tip percentage (e.g., 15 for 15%).

    Returns:
        tuple: (tip_amount, total_bill_with_tip)

    Python concepts highlighted:
    - Function parameters and return values
    """
    # Calculate the tip amount based on the percentage.
    tip = tab * tip_percent / 100
    # Calculate the total bill by adding the tip to the original tab.
    total = tab + tip
    return tip, total


def bill_split(total, how_many=1):
    """
    Splits the total bill evenly among a number of people.

    Args:
        total (float): The total bill amount.
        how_many (int): The number of people to split the bill with.

    Returns:
        float: The amount each person pays.

    Python concepts highlighted:
    - Conditional logic (`if`) to handle edge cases
    """
    # Ensure 'how_many' is a positive number to prevent ZeroDivisionError
    # and handle illogical splits. If 0 or less, the total is returned,
    # implying no split or an error condition where the original total is relevant.
    if how_many <= 0:
        return total 
    # Perform the division to split the bill.
    split = total / how_many
    return split

def get_diners():
    """
    Collects names of diners from user input.
    Returns a list of diner names.
    Prompts the user to enter names one by one until 'q' is entered.
    Each entered name is capitalized for consistent formatting.

    Python concepts highlighted:
    - `while True` loop for indefinite input until a break condition
    """
    diners = [] # Initialize an empty list to store diner names.
    print("Who dined today?")
    while True: # Loop indefinitely until a break condition is met.
        # Get input, remove leading/trailing whitespace, and convert to lowercase for 'q' check.
        diner = input("Enter a name (or 'q' to quit): ").strip()
        if diner.lower() == 'q': # Check if the user wants to quit.
            break
        if diner: # Only add non-empty names to the list.
            diners.append(diner.title()) # Capitalize the first letter of each word in the name for consistent display.
    return diners

def get_float_input(prompt, min_val=0):
    """
    Gets a float input from the user with validation.

    Python concepts highlighted:
    - `try-except` block for robust error handling of user input
    """
    while True:
        try: # Attempt to convert user input to a float.
            value = float(input(prompt))
            # Validate against the minimum acceptable value.
            if value < min_val:
                print(f"Value must be {min_val} or greater.")
                continue # Continue the loop to ask for input again.
            return value
        except ValueError:
            # Handle cases where input is not a valid number.
            print("Invalid entry. Please enter a numeric value.")

def get_yes_no_input(prompt):
    """
    Gets a 'y' or 'n' input from the user with validation.

    Python concepts highlighted:
    - `in` operator for checking membership in a collection
    """
    while True:
        # Get input, remove leading/trailing whitespace, and convert to lowercase.
        response = input(prompt).strip().lower() 
        if response in ['y', 'n']: # Check if the response is 'y' or 'n'.
            return response
        else:
            # Inform the user about invalid input.
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == '__main__':
    # This block executes when the script is run directly.
    # Python concepts highlighted:
    # - `if __name__ == '__main__':` idiom for script execution
    # - Sequential program flow
    print("Time to pay the tab. Let's sort out tip, split and who pays!")

    # Get the total bill amount from the user, ensuring it's a valid float.
    tab = get_float_input("How much is the bill?: $") 

    diners = [] # Initialize an empty list for diner names.
    # Ask if there were other diners, using a validated yes/no input.
    solo_response = get_yes_no_input("Did others dine with you (y/n)? ") 
    if solo_response == 'y': # If yes, collect diner names.
        diners = get_diners() 
        # If the user said 'y' but then didn't enter any names, adjust the response.
        if not diners: # If the user indicated 'y' but then entered no names, treat it as dining alone.
            print("No diners entered. Assuming you dined alone.")
            solo_response = 'n'

    # Get the tip percentage from the user, ensuring it's a valid float and non-negative.
    percent = get_float_input("How much tip to leave? (e.g., 15, 18, 22): ", min_val=0) 
    if percent > 100: # Provide a warning for unusually high tip percentages, but allow it.
        print("Warning: Tip percentage is very high. Proceeding anyway.")

    # Calculate the tip amount and total bill using the tip_calc function.
    tip_amount, total_bill = tip_calc(tab, percent)

    # Display a summary of the bill.
    print(f"\n--- Bill Summary ---")
    print(f"Initial Bill: ${tab:.2f}")
    print(f"Tip ({percent:.0f}%): ${tip_amount:.2f}")
    print(f"Total with Tip: ${total_bill:.2f}")
    print(f"--------------------")

    # Determine further actions based on whether there were other diners.
    if solo_response == 'n' or not diners: 
        print("You dined alone.")
        # If dining alone, there's no need to split or play roulette.
    else:
        # Scenario for multiple diners.
        divide_response = get_yes_no_input("Will the bill be split (y/n)? ") # Ask if the bill should be split.
        if divide_response == 'y': 
            num_of_diners = len(diners) # Get the number of diners from the list.
            if num_of_diners > 0: # Ensure there are actual diners to split with.
                # Call the bill_split function to calculate individual amounts.
                divided_amount = bill_split(total_bill, num_of_diners) # Split the bill.
                print(f"The bill is split among {num_of_diners} diners.")
                print(f"Each person pays ${divided_amount:.2f}.")
            else:
                # This case should ideally not be reached if solo_response logic is robust
                # but acts as a safeguard.
                print("No diners were entered, so the bill cannot be split.")
        else:
            # If not splitting, offer to play 'Tab Roulette'.
            roulette_response = get_yes_no_input("Playing 'Tab Roulette' to decide who pays (y/n)? ") 
            if roulette_response == 'y': 
                # Call the who_pays function from the imported module.
                # .title() is applied to ensure consistent capitalization of the payer's name.
                payer = pay_the_tab_roulette.who_pays(diners) 
                print(f"Let's see who pays the tab!")
                print(f"{payer.title()} pays the tab today!")
            else:
                print("No one is playing tab roulette.")
