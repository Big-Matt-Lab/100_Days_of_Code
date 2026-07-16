
new_lines = [
    "text",
    "another line of text",
    "one more text line",
    "yet another line of text"
    ]
try:
    with open("text_file.txt", 'r') as file:
        lines =file.readlines()
except FileNotFoundError:
    print("file not found, creating file")
    with open("text_file.txt", 'a', encoding="UTF-8") as new_file:
        for line in new_lines:
            new_file.write(line + "\n")
else:
    print(lines)
finally:
    print("End this exercise")