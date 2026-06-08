"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Quiz Brain Module ***
This module defines the `QuizBrain` class, which manages the core logic
of the quiz game. It handles question progression, user input, scoring,
and checking answers.

Python Concepts Highlighted:
- Class definition and `__init__` constructor for object initialization.
- Instance attributes (`self.question_number`, `self.question_list`, `self.score`).
- `len()` for determining the length of a list.
- List indexing (`self.question_list[index]`) for accessing elements.
- `input()` for user interaction.
- F-strings for formatted output.
- `str.lower()` for case-insensitive string comparison.
- Conditional logic (`if/else`) for checking answers and providing feedback.
- `+=` augmented assignment operator for incrementing score and question number.
- Boolean return values for controlling game flow.
"""

class QuizBrain:
    """
    Manages the flow and logic of a quiz game.

    Attributes:
        question_number (int): The current question number (0-indexed).
        question_list (list): A list of `Question` objects for the quiz.
        score (int): The player's current score.
    """

    def __init__(self, question_list):
        """
        Initializes the QuizBrain with a list of questions.

        Args:
            question_list (list): A list of `Question` objects.
        """
        # Python concept: Instance attribute `self.question_number` to track current question index.
        self.question_number = 0
        # Python concept: Instance attribute `self.question_list` to store all quiz questions.
        self.question_list = question_list
        # Python concept: Instance attribute `self.score` to track the player's correct answers.
        self.score = 0

    def next_question(self):
        """
        Advances to the next question, prompts the user for an answer,
        and checks if the answer is correct.
        """
        # Python concept: List indexing to retrieve the current `Question` object.
        current_question = self.question_list[self.question_number]
        # Python concept: Augmented assignment `+=` to increment the question number.
        self.question_number += 1
        # Python concept: F-string for dynamic question prompt.
        # Python concept: `input()` to get the user's answer.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        # Python concept: Calling another instance method `check_answer()` to validate the input.
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Checks if there are more questions remaining in the quiz.

        Returns:
            bool: `True` if there are more questions, `False` otherwise.
        """
        # Python concept: `len()` to get the total number of questions.
        # Python concept: Comparison operator `<` to check if the current question number
        # is less than the total number of questions.
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Compares the user's answer with the correct answer and updates the score.
        Provides feedback to the user.

        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer to the question.
        """
        # Python concept: `str.lower()` for case-insensitive comparison.
        # Python concept: `if/else` for conditional logic based on answer correctness.
        if user_answer.lower() == correct_answer.lower():
            # Python concept: Augmented assignment `+=` to increment the score.
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        # Python concept: F-strings for displaying feedback and current score.
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        # Python concept: Printing a newline character for better readability between questions.
        print("\n") 