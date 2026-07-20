

"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Kanye Says Program ***
This program generates and displays quotes from Kanye West using the `kanye.rest` API.
Each time the user clicks on Kanye's image, a new quote is fetched and displayed.

Python Concepts Highlighted:
- `tkinter` for creating graphical user interfaces (GUI) (`tk.Tk`, `tk.Canvas`, `tk.Button`)
- `requests` for making HTTP GET requests to external APIs (`requests.get`, `response.json`)
- Exception handling for API calls (`response.raise_for_status`)
- Asynchronous programming concepts for GUI updates (fetching data without freezing the UI)
- Global variable usage for GUI elements (`canvas`, `quote_text`)
- Event handling for button clicks (`command` parameter in `tk.Button`)
"""

import tkinter as tk
import requests


def get_quote():
    """Fetches a random quote from the Kanye.rest API and updates the GUI.

    This function makes an HTTP GET request to the `https://api.kanye.rest` endpoint.
    It then parses the JSON response to extract Kanye's quote and updates the `quote_text`
    element on the Tkinter canvas.

    Args:
        None

    Returns:
        None: This function directly modifies the GUI and does not return any value.
    """
    target_url = "https://api.kanye.rest"

    response = requests.get(target_url)
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data['quote'])



# --- GUI SETUP ---

# Initialize the main window for the application.
window = tk.Tk()
window.title("Kanye Says...")  # Set the window title.
# Configure padding around the window content using `padx` and `pady`.
window.config(padx=50, pady=50)

# Create a `Canvas` widget to display images and text.
canvas = tk.Canvas(width=300, height=414) # Define canvas dimensions.
# Load the background image for the quote display.
background_img = tk.PhotoImage(file="background.png")
# Place the background image at specified coordinates on the canvas.
canvas.create_image(150, 207, image=background_img)
# Create a text element on the canvas to display quotes.
# `quote_text` is a global variable, allowing `get_quote()` to update it.
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE",
                                width=250, font=("Arial", 30, "bold"), fill="white")
# Position the canvas in the grid layout at row 0, column 0.
canvas.grid(row=0, column=0)

# Load Kanye's image for the button.
kanye_img = tk.PhotoImage(file="kanye.png")
# Create a `Button` widget with Kanye's image.
# `highlightthickness=0` removes the default button border.
# `command=get_quote` links the button click to the `get_quote` function.
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
# Position the button in the grid layout at row 1, column 0.
kanye_button.grid(row=1, column=0)

# Fetch an initial quote when the application starts.
get_quote()

# Start the Tkinter event loop.
# This function keeps the application running, listens for events (like button clicks),
# and updates the GUI until the window is closed.
window.mainloop()
