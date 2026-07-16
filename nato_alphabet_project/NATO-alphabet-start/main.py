
import pandas as pd

# Read csv to dataframe
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
code_dict = df.set_index('letter')['code'].to_dict()
print(code_dict)

# Create a list of the phonetic code words from a word that the user inputs.
def generate_message():
    message = input("What is the message?: ").strip().upper()
    try:
        #message_code_words = [code_dict[letter] for letter in message]
        message_code_words = [code_dict.get(letter, letter) for letter in message]
    except KeyError:
        print("Alphabetical characters only.")
        generate_message()
    else:
        #print(message_code_words)
        print(", ".join(message_code_words))

generate_message()
