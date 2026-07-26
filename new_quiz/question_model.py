"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Question Data Model ***
This module defines the basic OOP model class `Question` used to encapsulate individual
trivia questions with explicit properties representing their text and solutions.

Python Concepts Highlighted:
- Object-Oriented Programming (OOP) class blueprint construction (`Question`).
- Initializer constructor `__init__()` for instance-level variable bindings.
"""


class Question:
    """Represents a single trivia question with a query and standard solution answer.

    Attributes:
        text (str): The actual wording/content of the trivia question.
        answer (str): The correct corresponding answer, usually "True" or "False".
    """

    def __init__(self, q_text, q_answer):
        """Initializes a Question instance with text and the correct answer.

        Args:
            q_text (str): The body content of the question.
            q_answer (str): The correct boolean string answer.
        """
        # Python concept: Setting object-level state properties using instance assignments.
        self.text = q_text
        self.answer = q_answer
