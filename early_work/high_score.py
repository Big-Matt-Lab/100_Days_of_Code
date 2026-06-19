"""Udemy - 100 Days of Code

*** Finding the High Score ***
This script demonstrates different ways to find the highest value in a list of scores.

Python concepts highlighted:
- Manual iteration with a `for` loop to find a maximum value
- Using the built-in `max()` function for a more Pythonic solution
- Using `sorted()` to find the maximum value
"""
scores = [100, 22, 300, 125, 331, 238, 234732, 34181, 123827, 126345, 12847124, 8471,21738]

# --- Method 1: Manual Iteration ---
# Python concept: A `for` loop to iterate through each item in a list.
high_score = 0
for score in scores:
    if score > high_score:
        high_score = score
print(f"Manual high score: {high_score}")

# --- Method 2: Using the `max()` function (most efficient) ---
# Python concept: The built-in `max()` function finds the largest item in an iterable.
print(f"High score with max(): {max(scores)}")
# --- Method 3: Sorting the list ---
# Python concept: `sorted()` returns a new sorted list. The last item (`[-1]`) is the highest.
print(f"High score with sorted(): {sorted(scores)[-1]}")