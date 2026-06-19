""" """
def calculate_love_score(name_1, name_2):
    """Calculates a 'love score' based on the number of times the letters
    in the words "true" and "love" appear in two names."""

    # 1. Combine and sanitize names into a single string for easier processing.
    combined_names = (name_1 + name_2).lower()

    # 2. Count occurrences of letters for "true" and "love".
    # Using sum() with a generator expression and str.count() is highly efficient
    # and much cleaner than nested loops.
    true_count = sum(combined_names.count(char) for char in "true")
    love_count = sum(combined_names.count(char) for char in "love")

    # 3. Combine the two counts to form the score.
    # Using an f-string and int() conversion is a clear way to concatenate the digits.
    score = int(f"{true_count}{love_count}")


    print(f"Love Score = {score}")

calculate_love_score("Kim Kardashian", "Kanye West")
