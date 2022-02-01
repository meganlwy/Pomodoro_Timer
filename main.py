from cgitb import text
from curses import BUTTON1_RELEASED
from distutils.command.config import config
from email.mime import image
from itertools import count
from tkinter import *
from turtle import width
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLACK = "#323232"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFE162"
BEIGE = "#FFEDDB"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
round = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    label1.config(text="TIMER")
    label2.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global round
    round = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global round
    round += 1
    if round % 8 == 0:
        label1.config(text="BREAK", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif round % 2 == 0:
        label1.config(text="BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        countdown(WORK_MIN * 60)
        label1.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minute = math.floor(count / 60)
    second = math.floor(count % 60)

    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_count()
        round_mark = ""
        for _ in range(math.floor(round / 2)):
            round_mark += "🍅"
        label2.config(text=round_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=BEIGE)


# creata canvas
canvas = Canvas(width=300, height=300, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(
    file="pomodoro-start/tomato-small.png"
)  # can read a file and hold the item
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(
    150, 220, text="00:00", fill="white", font=(FONT_NAME, 40, "bold")
)
canvas.grid(column=1, row=1)

# Label
label1 = Label(text="TIMER", fg=BLACK, font=("Calibri", 30, "bold"), bg=BEIGE)
label1.grid(column=1, row=0)


# checkmark
label2 = Label(text="", bg=BEIGE)
label2.grid(column=1, row=3)

# Button
button_s = Button(
    text="start", highlightbackground=BEIGE, fg=BLACK, command=start_count
)
button_r = Button(text="reset", highlightbackground=BEIGE, fg=BLACK, command=reset)
button_r.grid(column=2, row=2)
button_s.grid(column=0, row=2)


window.mainloop()
