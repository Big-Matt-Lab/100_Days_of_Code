"""Docstring Here"""

import tkinter as tk

window = tk.Tk()
window.title("My irst GUI program")
window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="New Text", font=("Arial", 24, "bold"))
my_label.pack()


# my_label.config(text="New Text")

# Button

def button_clicked():
    """Docstring Here"""
    new_text = entry.get()
    my_label["text"] = new_text

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
entry = tk.Entry(width=10)
entry.pack()





window.mainloop()
