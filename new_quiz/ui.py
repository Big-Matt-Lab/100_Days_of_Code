"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Quiz Interface UI Module ***
This module contains the `QuizInterface` class, which handles rendering the graphical
user interface (GUI) using Tkinter. It listens for user events and provides immediate
visual feedback based on whether their answers are correct.

Python Concepts Highlighted:
- `import tkinter as tk` for generating native OS window components.
- Window event-driven architecture using Tkinter main loop (`mainloop()`).
- GUI element layouts and positioning using grid managers (`grid()`).
- Interactive callbacks triggered by UI event handlers (`command` attribute bindings).
- Dynamic timer-based actions using the Tkinter window main loop (`after()`).
"""

import tkinter as tk
from quiz_brain import QuizBrain

# Global immutable constant specifying the default background theme color of the window.
THEME_COLOR = "#375362"


class QuizInterface:
    """Manages the instantiation of Tkinter UI components and controls the graphical quiz display.

    Attributes:
        quiz (QuizBrain): The core quiz logic engine managing question state and scores.
        window (tk.Tk): The root Tkinter GUI window container.
        canvas (tk.Canvas): Canvas widget used to display the active question text clearly.
        question_text (int): Reference ID pointing to the text element loaded inside the Canvas.
        score_label (tk.Label): Label rendering the player's active high score.
        true_button (tk.Button): Interactive selection button registering a 'True' user choice.
        false_button (tk.Button): Interactive selection button registering a 'False' user choice.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """Initializes the Tkinter main window, configurations, and instantiates UI elements.

        Args:
            quiz_brain (QuizBrain): The active quiz engine managing data and answers.
        """
        # Python concept: Binding and referencing the central quiz controller object.
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question?",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)

        self.score_label = tk.Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=10, pady=10)

        # Python concept: Using `PhotoImage` to load assets from file system directories.
        true_button_image = tk.PhotoImage(file="images/true.png")
        false_button_image = tk.PhotoImage(file="images/false.png")

        # Python concept: Configuring button callbacks using command references to bind methods.
        self.true_button = tk.Button(image=true_button_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=10, pady=10)

        self.false_button = tk.Button(image=false_button_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, padx=10, pady=10)

        # Python concept: Fetching and loading the first question into the view during initialization.
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetches the next available question from the quiz, handles UI updates and checks bounds."""
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        
        # Python concept: Using a conditional check to verify index boundaries safely before reading.
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz.\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Callback handler executed when the user presses the 'True' button."""
        # Python concept: Initiating validation routines and passing evaluation results.
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Callback handler executed when the user presses the 'False' button."""
        # Python concept: Initiating validation routines and passing evaluation results.
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Applies dynamic colored background visual feedback, then sets a delay timer to proceed.

        Args:
            is_right (bool): True if the answer provided was correct, False otherwise.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        # Python concept: Scheduling non-blocking future function calls using `window.after()`.
        self.window.after(1000, self.get_next_question)
