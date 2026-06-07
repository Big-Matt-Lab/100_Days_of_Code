"""Udemy 100 Days of Code: Quiz Game Main Execution
This is the main entry point for the quiz application. It initializes 
the question bank, creates the quiz brain instance, and runs the main 
game loop.

Python concepts highlighted:
- Importing custom modules and classes
- List comprehension and object creation
- While loops for game state management
- Calling instance methods
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Python concepts highlighted: List comprehension and object creation
# Creating a list of Question objects from the raw dictionary data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Python concepts highlighted: Object instantiation
# Initializing the QuizBrain with the prepared list of questions
quiz = QuizBrain(question_bank)

# Python concepts highlighted: While loops for game flow
# Run the quiz loop as long as there are questions left
while quiz.still_has_questions():
    quiz.next_question()

# Final output upon quiz completion
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
