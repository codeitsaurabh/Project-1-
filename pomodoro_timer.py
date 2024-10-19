import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="purple")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg="orange")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="white")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="#0e1525")

title_label = tk.Label(text="Timer", fg="white", bg="#0e1525", font=("Times new roman", 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="#0e1525", highlightthickness=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Times new roman", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=1, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="#0e1525", font=("Courier", 24, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
