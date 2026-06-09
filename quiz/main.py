"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Quiz Game Main Execution ***
This is the main entry point for the quiz application. It initializes 
the question bank, creates the quiz brain instance, and runs the main 
game loop.

Python concepts highlighted:
- `from ... import` for importing custom modules and classes.
- `input()` for user interaction.
- `int()` for type conversion.
- `random.sample()` for selecting a random subset of items from a list.
- List iteration (`for` loop) and object creation.
- `list.append()` for adding items to a list.
- `while` loops for game state management.
- Calling instance methods (e.g., `quiz.next_question()`).
- F-strings for formatted output.
"""

# Python concept: Importing custom modules and classes.
from question_fetch import QuestionFetcher
from question_model import Question
from quiz_brain import QuizBrain
# Python concept: Importing the `random` module for random selections.
import random


# 10 books, 11 film, 12 music, 13 theater, tv, 15 video games, 16 board games
# 17 nature, computers, math, 20 mythology, sports geography, history
# 24 politics, art, celebrities, 27 animals, vehciles, comics
# 30 gadgets, anime, animation

# Python concept: Global variable `selected_category` to store the user's category choice.
# Its value is `None` if the user chooses "Any", otherwise it's an integer ID.
selected_category = None

# Present a numbered menu for the user where `1` is the default (Any/all).
print("Choose a category:")
print(" 1: Any (default)")
print(" 2: General Knowledge")
print(" 3: Books")
print(" 4: Film")
print(" 5: Music")
print(" 6: Musicals & Theatres")
print(" 7: Television")
print(" 8: Video Games")
print(" 9: Board Games")
print("10: Science & Nature")
print("11: Computers")
print("12: Mathematics")
print("13: Mythology")
print("14: Sports")
print("15: Geography")
print("16: History")
print("17: Politics")
print("18: Art")
print("19: Celebrities")
print("20: Animals")
print("21: Vehicles")
print("22: Comics")
print("23: Gadgets")
print("24: Anime & Manga")
print("25: Cartoon & Animations")

# Map the user's numbered choice to the API category ID values.
# API: 0 = Any, 9 = General Knowledge, 10 = Books, 11 = Film, ...
user_to_api = {
    "1": 0,
    "2": 9,
    "3": 10,
    "4": 11,
    "5": 12,
    "6": 13,
    "7": 14,
    "8": 15,
    "9": 16,
    "10": 17,
    "11": 18,
    "12": 19,
    "13": 20,
    "14": 21,
    "15": 22,
    "16": 23,
    "17": 24,
    "18": 25,
    "19": 26,
    "20": 27,
    "21": 28,
    "22": 29,
    "23": 30,
    "24": 31,
    "25": 32,
}

# Python concept: `input()` to get user input. Default to "1" if empty.
choice = input("Choice (1-25): ") or "1"

# Resolve the selected API category id. If an unexpected value is entered,
# attempt to convert it to an integer and use that directly.
if choice in user_to_api:
    selected_category = user_to_api[choice]
else:
    try:
        selected_category = int(choice)
    except ValueError:
        # Fallback to default (Any)
        selected_category = 0

# Python concept: Object-Oriented Programming (OOP) - creating an instance of `QuestionFetcher`.
# The `fetcher` object is responsible for retrieving and cleaning question data.
fetcher = QuestionFetcher(category_id=selected_category)
# Python concept: Calling an instance method `fetch_and_clean_data()` to get data.
raw_question_data = fetcher.fetch_and_clean_data()

# Python concept: Global variable `number_of_questions` defines the size of the quiz.
# This constant determines how many questions will be selected for the quiz.
number_of_questions = 5
# Python concept: `random.sample()` to select a unique random sample of questions.
# This ensures that the quiz uses a subset of the fetched data without repetition.
random_sample = random.sample(raw_question_data, number_of_questions)

# Python concept: Global variable `question_bank` to store `Question` objects.
# This list will hold the prepared questions for the quiz.
question_bank = []
# Python concept: `for` loop to iterate through the `random_sample` and create `Question` objects.
# Each dictionary from the API response is converted into a `Question` instance.
for question in random_sample:
    # Python concept: Instantiating the `Question` class.
    new_question = Question(question["text"], question["answer"])
    # Python concept: `list.append()` to add the new `Question` object to the `question_bank`.
    question_bank.append(new_question)

# Python concept: Instantiating the `QuizBrain` class to manage the quiz logic.
# The `quiz` object will handle question progression, scoring, and answer checking.
quiz = QuizBrain(question_bank)
# Python concept: `while` loop for game state management.
# The loop continues as long as `quiz.still_has_questions()` returns `True`.
while quiz.still_has_questions():
    # Python concept: Calling an instance method `next_question()` to advance the quiz.
    quiz.next_question()

# Python concept: F-strings for displaying the final score.
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
