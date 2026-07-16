
import pandas as pd
import random
import tkinter as tk




BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    root.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=back_img)


#--------------- UI SETUP --------------#

root = tk.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# Define a widget canvas container to draw external graphics like the PNG logo.
canvas = tk.Canvas(width=800, height=526, bg="white")
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

unknown_img = tk.PhotoImage(file="images/wrong.png")
known_img = tk.PhotoImage(file="images/right.png")

unknown_button = tk.Button(command=next_card, image=unknown_img)
unknown_button.grid(column=0, row=1)

known_button = tk.Button(command=next_card, image=known_img)
known_button.grid(column=1, row=1)

next_card()
root.after(3000, func=flip_card)


root.mainloop()