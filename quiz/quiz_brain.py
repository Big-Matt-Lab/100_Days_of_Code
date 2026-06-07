"""Udemy 100 Days of Code: Quiz Brain Logic
This module manages the core logic and state of the quiz, including 
tracking the current question, user score, and validating answers.

Python concepts highlighted:
- Class definitions and encapsulation
- List indexing and slicing
- F-strings for dynamic question output
- Input handling and conditional logic
- Method definitions with self-referencing
"""

class QuizBrain:
    """
    Manages the logic and state of the quiz.

    Attributes:
        question_number (int): The current question number (0-indexed).
        score (int): The user's current score.
        question_list (list): A list of Question objects.
    """

    def __init__(self, q_list):
        """
        Initializes the QuizBrain with a list of questions.

        Args:
            q_list (list): A list of Question objects.
        """
        # Python concepts highlighted: Attribute initialization
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are more questions remaining in the quiz.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the current question and prompts the user for an answer.
        Increments the question number and calls answer verification.
        """
        # Python concepts highlighted: List indexing and F-strings
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Compares the user's answer with the correct answer and updates score.

        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer to the question.
        """
        # Python concepts highlighted: String comparison and conditional logic
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
