"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Coffee Machine ***
A command-line coffee machine simulator that manages resources, processes coin payments,
and dispenses espresso, latte, or cappuccino based on user input.

Python Concepts Highlighted:
- PEP 8 constants naming for defining read-only configuration (`MENU`)
- Nested dictionaries for accessing multi-level data structures (`MENU[drink]["ingredients"]`)
- Mutable vs. immutable global state for managing machine resources and earnings (`resources`, `profit`, `global profit`)
- Function definition for modularity and scope separation (`status_report`, `coins_tendered`, `make_coffee`, `main`)
- Nested functions for encapsulating local utility logic (`get_int_input` inside `coins_tendered`)
- Exception handling for user input sanitization and crash prevention (`try/except` around `int()`)
- Dictionary iteration with `.items()` for accessing keys and values simultaneously in loops (`supplies.items()`, `drink_ingredients.items()`)
- Idiomatic membership checking for verifying keys in a dictionary efficiently (`user_choice not in MENU`)
- String manipulation and formatting for clean input sanitization and readable output (`.strip()`, `.lower()`, `.title()`, f-strings)
- Control flow structures for managing loop execution and conditional logic (`if/elif/else`, `while not off`)
- Early return pattern for terminating function execution early when conditions are not met (`return`)
"""

# Python concept: Constant variables defined in uppercase like `MENU` to signal read-only status.
# This is structured as a nested dictionary mapping drink names to their ingredients and cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Python concept: Mutable dictionary representing the machine's ingredient resources.
# Dictionary values can be modified in local scopes without requiring the `global` keyword.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Python concept: Immutable float representing the total cash profit.
# Reassigning this variable within a local function scope requires the `global` keyword.
profit = 0.0


def status_report(supplies, cash):
    """
    Prints a formatted status report of current resources and profit.

    Displays water and milk in milliliters, coffee in grams, and money in dollars.

    Args:
        supplies (dict): Dictionary containing current resource amounts.
        cash (float): Current profit/money in the machine.

    Returns:
        None: This function only prints output.
    """
    # Python concept: `.items()` method returns key-value pairs for dictionary iteration.
    for ingredient, amount in supplies.items():
        # Python concept: `if` statement for conditional formatting based on ingredient type.
        if ingredient == 'coffee':
            # Python concept: `.title()` capitalizes the first letter of each word.
            print(f"{ingredient.title()}: {amount} g")
        else:
            # Python concept: `else` clause handles the default case for liquid ingredients.
            print(f"{ingredient.title()}: {amount} ml")
    # Python concept: `:.2f` format specifier inside an f-string to format the float to two decimal places.
    print(f"Money ${cash:.2f}")


def coins_tendered():
    """
    Calculates the total value of coins inserted by the user.

    Prompts user for quantities of each coin type and returns the monetary total.

    Returns:
        float: Total value of all coins inserted in dollars.
    """
    # Python concept: Nested functions to restrict helper function scope.
    # Defining `get_int_input` inside `coins_tendered` encapsulates the helper logic to prevent namespace clutter.
    def get_int_input(prompt):
        """
        Repeatedly prompts the user for input until a valid non-negative integer is entered.

        Args:
            prompt (str): The text prompt displayed to the user.

        Returns:
            int: The valid non-negative integer entered by the user.
        """
        # Python concept: `while True` loop for continuous input validation until a valid integer is returned.
        while True:
            # Python concept: `try/except` block for exception handling.
            # If the user enters a non-digit string, `int()` raises a `ValueError`.
            # The `except` block catches it to prevent program crash, prompting the user again.
            try:
                # Python concept: `input()` to receive string input and `int()` to type cast it to an integer.
                value = int(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    quarters = get_int_input("How many quarters?: ")
    dimes = get_int_input("How many dimes?: ")
    nickels = get_int_input("How many nickels?: ")
    pennies = get_int_input("How many pennies?: ")
    # Python concept: Arithmetic operators to compute the float sum of all coins.
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


def make_coffee(drink):
    """
    Processes a coffee order by checking resources, handling payment, and dispensing the drink.

    This function performs the complete transaction flow: resource validation,
    payment processing, change calculation, profit update, and resource depletion.

    Args:
        drink (str): The name of the drink to make (espresso, latte, or cappuccino).

    Returns:
        None: Function prints messages and modifies global state but returns nothing.
    """
    # Python concept: The `global` keyword is required to reassign immutable global variables.
    # Since `profit` is an immutable float, we must declare `global profit` to modify it.
    # Note that mutable objects like `resources` (dictionary) can be mutated without the `global` declaration.
    global profit

    # Python concept: Nested dictionary access to retrieve sub-dictionaries.
    # Accesses `MENU[drink]["ingredients"]` to retrieve the dictionary of required ingredients.
    drink_ingredients = MENU[drink]["ingredients"]

    # Python concept: Early return pattern to exit the function when resource requirements are not met.
    # Iterates through ingredients and checks if the quantity in `resources` is sufficient.
    for ingredient, amount in drink_ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return

    print("Please insert coins.")
    # Python concept: Function invocation to retrieve and calculate user's coin payment.
    payment = coins_tendered()
    drink_cost = MENU[drink]["cost"]

    # Python concept: `if` statement comparing user payment to drink cost.
    if payment < drink_cost:
        print("Sorry, that is not enough money. Money refunded.")
        # Python concept: `return` statement to exit the function early on insufficient payment.
        return

    # Python concept: Basic arithmetic subtraction to calculate the customer's change.
    change = payment - drink_cost
    # Python concept: Conditional `if` statement to check if change needs to be returned.
    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    # Python concept: `+=` augmented assignment operator to increment the `profit` variable.
    profit += drink_cost
    # Python concept: Dictionary iteration using `.items()` to update ingredients in stock.
    for ingredient, amount in drink_ingredients.items():
        # Python concept: `-=` augmented assignment operator to decrement value in `resources` dictionary.
        resources[ingredient] -= amount

    print(f"Here is your {drink} ☕. Enjoy!")


def main():
    """
    Runs the main program loop for the coffee machine.

    Continuously prompts user for drink choice until 'off' is entered or invalid input is given.
    Handles 'report' command to show current status and delegates drink orders to make_coffee.

    Returns:
        None: Function runs the program loop until termination.
    """
    # Python concept: Boolean flag variable to control execution state.
    off = False
    # Python concept: `while not` loop that continues running until the flag changes to `True`.
    while not off:
        # Python concept: Method chaining with `.strip()` and `.lower()` for input sanitization.
        user_choice = input("What would you like? (espresso $1.50, latte $2.50, cappuccino $3.00): ").strip().lower()
        # Python concept: Conditional branching using `if/elif/else` to execute commands.
        if user_choice == 'report':
            status_report(resources, profit)
        # Python concept: Idiomatic membership checking using the `in` and `not in` operators.
        # Checking `key in dict` is O(1) complexity because Python dictionaries use hash tables.
        # Checking `user_choice not in MENU` checks the keys directly and is preferred over `.keys()`.
        elif user_choice == 'off' or user_choice not in MENU:
            # Python concept: Reassigning sentinel flag to `True` to terminate the loop on next iteration.
            off = True
        else:
            make_coffee(user_choice)


# Python concept: The `if __name__ == '__main__'` idiom.
# Ensures that the main block of code runs only when the script is executed directly,
# rather than being imported as a module.
if __name__ == '__main__':
    main()
