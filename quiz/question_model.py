"""Udemy 100 Days of Code: Quiz Question Model
This module defines the Question class, which serves as the blueprint for 
each question in the quiz game.

Python concepts highlighted:
- Class definitions and object-oriented programming
- Constructor method (__init__)
- Attribute initialization
"""

class Question:
    """
    A class to represent a quiz question.

    Attributes:
        text (str): The text of the question.
        answer (str): The correct answer to the question.
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes the question with text and answer.

        Args:
            q_text (str): The text of the question.
            q_answer (str): The correct answer.
        """
        # Python concepts highlighted: Attribute initialization
        # Assigning the passed arguments to the instance attributes
        self.text = q_text
        self.answer = q_answer
