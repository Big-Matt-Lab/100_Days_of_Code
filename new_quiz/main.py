"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Quiz Game Main Entry Point ***
This script serves as the main driver of the trivia application. It coordinates
fetching raw questions from the API, converting them into standard OOP models,
initializing the game engine, and launching the Tkinter user interface.

Python Concepts Highlighted:
- `import` statements for module modularity and code reuse.
- Class instantiation and Object-Oriented Programming (OOP) by creating custom objects.
- `random.sample()` for unique non-repetitive subset selection from lists.
- `list` comprehension/iteration to dynamically transform data schemas.
"""

import random

from question_fetch import QuestionFetcher
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

# Python concept: Instantiating the `QuestionFetcher` helper class to pull from API.
# The category parameter configures which specific genre of trivia to fetch.
fetcher = QuestionFetcher(category=0)

# Python concept: Calling an instance method `fetch_and_clean_data` to perform a network request.
raw_question_data = fetcher.fetch_and_clean_data()

# Global constant setting the total number of trivia questions in the active quiz.
# This variable is an integer, immutable by nature, and controls list slicing/sampling constraints.
number_of_questions = 5

# Python concept: Using `random.sample` to select a completely unique subset of dictionary items.
random_sample = random.sample(raw_question_data, number_of_questions)

# List container used to store the instanced `Question` objects.
question_bank = []

# Python concept: Iterating through standard dictionaries to build custom strongly-typed objects.
for question in random_sample:
    # Python concept: Initializing class instances with positional arguments.
    new_question = Question(question["text"], question["answer"])
    # Python concept: Dynamically appending objects to a `list` data structures.
    question_bank.append(new_question)

# Python concept: Instantiating the core logic controller `QuizBrain` with our collection of questions.
quiz = QuizBrain(question_bank)

# Python concept: Creating the Tkinter GUI interface `QuizInterface` and starting the event loop.
quiz_ui = QuizInterface(quiz)
