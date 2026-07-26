"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Quiz Brain Game Engine Module ***
This module contains the `QuizBrain` class, which serves as the controller and coordinator for managing
the active quiz session state. It handles progression tracking, scoring, and answering logic.

Python Concepts Highlighted:
- Object-Oriented Programming (OOP) class implementation representing system logic.
- Using integer instance variables to maintain persistent dynamic session state (`self.question_number`, `self.score`).
- `list` indexing to fetch stored collection items (`self.question_list[self.question_number]`).
- Custom method creation with boolean checks (`still_has_questions()`).
- Direct string and variable formatting using f-strings to display metadata.
"""

import html


class QuizBrain:
    """The central game controller that processes quiz state, scoring, and question sequencing.

    Attributes:
        question_number (int): The index counter tracking the active question position (0-indexed).
        score (int): The current tally of correctly answered questions in the session.
        question_list (list): The list containing the collection of loaded `Question` objects.
        current_question (Question): The current active question instance.
    """

    def __init__(self, q_list):
        """Initializes QuizBrain with a structured bank of question objects.

        Args:
            q_list (list): A list containing `Question` objects to be used for the quiz.
        """
        # Python concept: Initializing standard tracker integers to zero.
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Determines whether there are any remaining questions left in the active bank list.

        Returns:
            bool: True if there are more questions available to be served, False otherwise.
        """
        # Python concept: Comparing integers to return a standard boolean evaluation result.
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieves and prepares the next question text, incrementing the question index.

        Returns:
            str: A formatted string containing the question index number and unescaped HTML content.
        """
        # Python concept: Accessing list elements sequentially by their index.
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Validates the user's submitted choice against the true question solution, updating score.

        Args:
            user_answer (str): The option selected by the user (typically "True" or "False").

        Returns:
            bool: True if the user's choice matches the correct solution, False otherwise.
        """
        correct_answer = self.current_question.answer
        # Python concept: Using case-insensitive string comparison via `.lower()`.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
