"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Password Manager ***
An interactive, desktop-based graphical password manager built with Tkinter. This application
enables users to generate highly secure, randomized passwords, automatically copy them to the 
system clipboard, and save login credentials (website, email/username, password) directly 
to a local text file.

Python Concepts Highlighted:
- `tkinter` for crafting graphical user interfaces and handling visual layouts (`tk.Tk()`, `tk.Canvas`, `tk.Entry`).
- List comprehensions for creating collections of randomly selected characters concisely (`[random.chsoice(...), k = (...)]`).
- File I/O for appending data to a file safely using context managers (`with open()`).
- External Libraries for integrating system clipboard interaction (`pyperclip.copy()`).
- In-place mutation with standard library functions to randomize element order (`random.shuffle()`).
- String manipulation using join operations to stitch a character list into a single string (`"".join()`).
"""
import json
import random
import tkinter as tk
from tkinter import messagebox as mbox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a secure, randomized password and copies it to the system clipboard.
    
    This function compiles a password consisting of letters, numbers, and symbols.
    It clears any existing password in the entry box, populates it with the new password,
    and copies it to the user's clipboard for easy access.

    Returns:
        None: Inserts password into `password_entry` and copies to clipboard.
    """
    # Character pools used as local constants. Although Python lists are technically mutable,
    # these lists act as read-only static reference sets for assembling passwords.
    LETTERS = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    SYMBOLS = ('!', '#', '$', '%', '&', '*', '+')

    # Python concept: Using a list comprehension to efficiently generate sub-lists of random characters.
    password_list = random.choices(LETTERS, k = random.randint(8, 10))
    password_list += random.choices(SYMBOLS, k = random.randint(2, 4))
    password_list += random.choices(NUMBERS, k = random.randint(2, 4))

    # Randomize the sequence of items in-place within the mutable list structure.
    random.shuffle(password_list)

    # Python concept: Calling the `join()` string method to merge all list items into a single string.
    password = "".join(password_list)

    # Delete any existing text inside the entry box before inserting the new password.
    password_entry.delete(0, tk.END)
    # Populate the entry field in the user interface.
    password_entry.insert(tk.END, password)
    # Python concept: Utilizing the external `pyperclip` module to copy text straight to clipboard.
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Saves the user's login credentials to a local text file.

    Retrieves the entered website, username, and password from the UI entry widgets.
    Appends the formatted credentials into 'data.txt' and clears the fields 
    for subsequent entries. Displays a popup messagebox upon successful completion.

    Returns:
        None: Appends data to 'data.txt' and clears inputs.
    """
    website = website_entry.get().strip().lower()
    email = username_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        mbox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    else:
        try:
            with open("data.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w", encoding="utf-8") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()


# ---------------------------- SEARCH ------------------------------- #
def search_password():
    website = website_entry.get().strip().lower()
    if len(website) == 0:
        mbox.showwarning(title="Oops", message="Please don't leave Website field empty!")
        return

    try:
        with open("data.json", mode="r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        mbox.showwarning(title="Oops", message="Log in data file doesn't exist yet.")
        return

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            message_text = f"Username: {email}\nPassword: {password}"
            mbox.showinfo(title=website, message=message_text)
            return

        else:
            mbox.showwarning(title="Oops", message=f"No info for {website} saved.")
            return


# ---------------------------- UI SETUP ------------------------------- #


# Initialize the main window acting as the foundational container for our UI widgets.
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Define a widget canvas container to draw external graphics like the PNG logo.
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Instantiate the static text labels instructing users on required input fields.
website_label = tk.Label(text="Website:", font=("Arial", 12, "bold"), bg="white")
website_label.grid(column=0, row=1)

username_label = tk.Label(text="Email/Username:", font=("Arial", 12, "bold"), bg="white")
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", font=("Arial", 12, "bold"), bg="white")
password_label.grid(column=0, row=3)

# Establish entry boxes that capture text inputs, setting their layouts and defaults.
website_entry = tk.Entry(width=23)
website_entry.insert(tk.END, string="")
website_entry.grid(column=1, row=1)
# Focus the text insertion cursor automatically on the first input field.
website_entry.focus()

search_button = tk.Button(text="Search", command=search_password, font=("Arial", 11, "bold"),
                        bg="white", width=16)
search_button.grid(column=2, row=1)

username_entry = tk.Entry(width=44)
username_entry.insert(tk.END, string="")
username_entry.grid(column=1, row=2, columnspan=2)
# Set a default commonly-used email placeholder.
username_entry.insert(0, "test@gmail.com")

password_entry = tk.Entry(width=23)
password_entry.insert(tk.END, string="")
password_entry.grid(column=1, row=3, columnspan=1)

# Instantiate action buttons that bind visual triggers to executable callback functions.
generate_button = tk.Button(text="Generate Password", command=generate_password,
                            font=("Arial", 11, "bold"), bg="white")
generate_button.grid(column=2, row=3)

save_button = tk.Button(text="Add", command=save_password, font=("Arial", 11, "bold"),
                        bg="white", width=38)
save_button.grid(column=1, row=4, columnspan=2)



# Python concept: Launching the main event listener to keep the graphical window alive and active.
window.mainloop()
