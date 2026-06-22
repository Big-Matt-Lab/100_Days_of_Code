
mail = """Dear [name],
\nYou are invited to my birthday this Saturday.
\nHope you can make it!
\nAngela"""
out = []

def get_names():
    try: # Python concept: Use a `try-except` block to handle potential file errors.
            # Python concept: Open `data.txt` in read mode.
        with open("Input/Names/invited_names.txt", mode="r") as file:
            names = (file.read()) # Python concept: Read the content of the file.
            return names.splitlines()
    except FileNotFoundError:
        return [] # Return an empty list if file not found
    

def save_letters(prepped_letters):
    for letter in prepped_letters:
        try:
            with open(f"Output/ReadyToSend/example.txt", "w") as merged_letter:
                merged_letter.write(letter)
        except FileNotFoundError:
            print(f"Error: Could not save letter for {name}")


name_list = get_names()
for name in name_list:
    out.append(mail.replace("[name]", name))

save_letters(zip(name_list, out))



