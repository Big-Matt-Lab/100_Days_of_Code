"""Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
*** Quiz Project ***
The main entry point for the quiz application. It initializes the questions and runs the quiz loop.
- `Classes` and `Objects` for modeling quiz items and logic.
- `For Loops` for iterating through data to create object instances.
- `While Loops` for maintaining the game state until completion.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the raw data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the QuizBrain with the list of questions
quiz = QuizBrain(question_bank)

# Run the quiz until all questions are answered
while quiz.still_has_questions():
    quiz.next_question()

# Final output upon quiz completion
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
