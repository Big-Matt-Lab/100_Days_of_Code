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


# Python concept: Global variable `selected_category` to store the user's category choice.
# Its value is `None` if the user chooses "Any", otherwise it's an integer ID.
selected_category = None

print("Choose a category:\n0: Any\n9: General Knowledge\n21: Sports")
# Python concept: `input()` to get user input.
choice = input("Choice: ")
# Python concept: Conditional expression to set `selected_category` based on user input.
# `int()` is used for type conversion if a specific category is chosen.
if choice != "0":
    selected_category = int(choice)

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
