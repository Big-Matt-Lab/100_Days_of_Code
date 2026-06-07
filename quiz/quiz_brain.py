"""Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
*** Quiz Project ***
Manages the quiz logic, including tracking the current question and score.
- `Classes` for encapsulating quiz behavior.
- `Methods` for handling question flow and answer verification.
"""

class QuizBrain:
    """Manages the logic and state of the quiz."""

    def __init__(self, q_list):
        """Initializes the `QuizBrain` with a list of questions.
        Arguments:
        q_list: A list of `Question` objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """Checks if there are more questions remaining in the quiz.
        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieves the current question and prompts the user for an answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Compares the user's answer with the correct answer and updates the score.
        Arguments:
        user_answer: The answer provided by the user.
        correct_answer: The actual correct answer for the question.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
