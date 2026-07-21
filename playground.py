"""Docstring"""
START_WORD = "I think the original idea is that because join() returns a string"
reversed_word = []
for letter in START_WORD:
    reversed_word.insert(0, letter)
print("".join(reversed_word))
