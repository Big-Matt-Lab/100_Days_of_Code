"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Pomodoro Timer Application ***
A graphical countdown timer built with Tkinter that implements the classic Pomodoro 
technique. It alternates between 25-minute work blocks, 5-minute short breaks, and 
a 20-minute long break after every fourth work session to maximize productivity.

Python Concepts Highlighted:
- `tkinter` GUI development for creating desktop windows, labels, and input fields (`tk.Tk()`)
- `Canvas` widget drawing for stacking image backgrounds and digital text layers (`create_image()`)
- Event loop scheduling for asynchronous execution and building recurring timers (`window.after()`)
- Global state management for tracking application iterations across separate scopes (`global` keyword)
- Floor division and modulo arithmetic for formatting integer seconds into MM:SS string layouts (`//`, `%`)
"""

import math
import tkinter as tk

# ---------------------------- CONSTANTS & GLOBAL STATE ------------------------------- #
# Color Palette (Hex Codes) used to stylize the visual states of the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# UI Typography configuration
FONT_NAME = "Courier"

# Unicode character representing a successfully completed work interval
CHECK_MARK = "✓" 

# Pomodoro Interval Durations (expressed in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Python concept: Tracks the current session sequence index. 
# This integer determines whether the user should be working, short-breaking, or long-breaking.
reps = 0

# Python concept: Keeps a reference to the active 'after' macro event loop schedule. 
# Explicitly declared as None so it can be cleared or overridden safely.
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Resets the Pomodoro timer loop, zeroes the iteration counter, and restores the UI layout.
    
    This function leverages `window.after_cancel()` to cleanly tear down the background 
    recursive looping without crashing the Tkinter engine.
    """
    global reps, timer
    
    # Python concept: Safely cancels an active background thread scheduled via the event loop
    if timer is not None:
        window.after_cancel(timer)
        timer = None
        
    # Revert all canvas and text components back to their baseline states
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    
    # Zero out the global cycle monitor
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Increments the iteration tracking counter and triggers the appropriate session interval.
    
    Determines whether to launch a Work block (25 min), a Short Break (5 min), 
    or a Long Break (20 min) by running modulo checks on the current replication count.
    """
    global reps
    reps += 1

    # Python concept: Scale time parameters from minutes down into seconds for the countdown parser
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 

    # Python concept: Using the modulo operator `%` to alternate states based on structural indexes
    # Cycle 8: Long break triggered every 4th completed work session
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # Cycles 2, 4, 6: Alternate short break periods following standard work sessions
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # Cycles 1, 3, 5, 7: Standard productivity focus sprint
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Executes a recursive 1-second countdown loop that renders the remaining time to the UI.

    Args:
        count (int): The current remaining time tracking slice calculated in seconds.
    """
    global timer
    
    # Python concept: Floor division `//` isolates total remaining whole minutes
    counter_min = count // 60
    if counter_min == 0:
        counter_min = "00"
        
    # Python concept: Modulo operator `%` extracts structural remaining fractional seconds
    counter_sec = count % 60
    
    # Python concept: F-string formatting with zero padding to enforce strict two-digit display layouts
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"
        
    # Inject the fresh timestamps directly into the Tkinter Canvas text coordinate slot
    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    
    # Python concept: Recursive base-case pattern using `window.after()` to mimic a non-blocking clock
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Cascade into the next sequence immediately when the counter hits zero
        start_timer()
        
        # Parse out completed work blocks and string-multiply a tally checkmark badge setup
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Instantiate the root frame instance window and supply layout margins
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Python concept: Instantiating a `Canvas` widget to precisely position overlay elements over art assets
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image=tomato_img)
timer_text = canvas.create_text(103, 110, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

# Python concept: Implementing the Grid geometry manager to organize layouts systematically
canvas.grid(column=1, row=1)

# Application state indicator label
title_label = tk.Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0, padx=20)

# Tracker label that updates dynamically with completed checkmark loops
check_marks = tk.Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3, padx=20)

# Interactive macro buttons utilizing callback patterns to hit functional triggers
start_button = tk.Button(text="Start", command=start_timer, font=(FONT_NAME, 14, "bold"))
start_button.grid(column=0, row=3, pady=5)

reset_button = tk.Button(text="Reset", command=reset_timer, font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=3, pady=5)

# Python concept: Infinite main event rendering loop that watches for active component clicks
window.mainloop(