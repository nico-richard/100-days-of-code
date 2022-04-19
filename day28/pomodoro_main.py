from tkinter import *
from tkinter.font import BOLD
from PIL import Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='TIMER', bg=YELLOW, fg='#454545', font=(FONT_NAME, 30, 'bold'))
    checkmark_label.config(text='')
    canvas.itemconfig(canvas_text, text='00:00')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text='Work time', fg=GREEN)
        count_down(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text='Short break', fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text='Long break', fg=RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = str(count // 60).zfill(2)
    seconds = str(count % 60).zfill(2)
    time = f'{minutes}:{seconds}'

    canvas.itemconfig(canvas_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        if reps % 2 != 0 and reps != 1:
            checkmark_label.config(text=checkmark_label['text'] + '✓')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50)
window.config(background=YELLOW)

image = PhotoImage(file='day28/tomato.png')
IMG_WIDTH = image.width()
IMG_HEIGHT = image.height()

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, background=YELLOW, highlightthickness=0)
canvas_image = canvas.create_image(IMG_WIDTH / 2, IMG_HEIGHT / 2, image=image)
canvas_text = canvas.create_text(IMG_WIDTH / 2, IMG_HEIGHT / 2 + 20, text='00:00', font=(FONT_NAME, 25, 'bold'), fill=YELLOW)
canvas.grid(row=1, column=1)

timer_label = Label(text='TIMER', bg=YELLOW, fg='#454545', font=(FONT_NAME, 30, 'bold'))
timer_label.grid(row=0, column=1)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkmark_label.grid(row=3, column=1)

start_button = Button(text='start', highlightthickness=0, font=(FONT_NAME, 15), command=start_count)
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', highlightthickness=0, font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()