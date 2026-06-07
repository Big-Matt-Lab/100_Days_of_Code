"""Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
*** Quiz Project ***
Defines the `Question` class to represent a single quiz question.
- `Classes` for blueprinting the structure of quiz items.
- `Object Attributes` for storing `text` and `answer` data.
"""

class Question:
    """Models a single quiz question with text and answer."""

    def __init__(self, q_text, q_answer):
        """Initializes a `Question` object.
        Arguments:
        q_text: The text content of the question.
        q_answer: The correct answer for the question.
        """
        self.text = q_text
        self.answer = q_answer
