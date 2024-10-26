from tkinter import *
import math

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
#Function to reset the clock, the timer label and the ticks
def reset_clock():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer",fg=GREEN)
    tick_label['text'] = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
#Function to start the times based on work or break sessions
def start_clock():
    global reps
    reps += 1

    #For odd reps value start countdown for work sessions
    #For even reps value start countdown for short break sessions
    #After every 8th rep start countdown for long break session
    if(reps%2 == 1):
        count_down(WORK_MIN*60)
        title_label.config(text="Work",fg=GREEN)
    elif(reps%2 == 0):
        count_down(SHORT_BREAK_MIN*60)
        title_label.config(text="Break",fg=PINK)
    elif(reps%8 == 0):
        count_down(LONG_BREAK_MIN*60)
        title_label.config(text="Break",fg=RED)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#Function to start the countdown for a session
def count_down(count):
    global timer

    #Calculating the minutes and seconds in the count
    count_min = math.floor(count/60)
    count_sec = count%60

    #Condition to change single digit seconds as 09 instead of 9
    if(count_sec < 10):
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #Condition to avoid timer to become negative
    if(count > 0):
        timer = window.after(1000,count_down,count-1)
    #When the work session is completed, tick appears below tomato    
    else:
        start_clock()
        tick = ""
        for _ in range(math.floor(reps/2)):
            tick +=  "✔"
            tick_label['text'] = tick


# ---------------------------- UI SETUP ------------------------------- #
#Creating the window 
window = Tk()
window.title('Pomodoro Technique')
window.config(padx=100, pady=50, bg=YELLOW)

#Creating the canvas to place the image of tomato in the screen
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,128,text="00:00",fill="white",font=(FONT_NAME,34,'bold'))
canvas.grid(column=1,row=1)

#Creating the title label which shows "Timer", "Work" and "Break"
title_label = Label(text="Timer",font=(FONT_NAME,30,'normal'),bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)

#Creating button to reset the timer clock
reset_button = Button(text="Reset",command=reset_clock,highlightthickness=0)
reset_button.grid(column=2,row=3)

#Creating button to start the timer clock
start_button = Button(text="Start",command=start_clock,highlightthickness=0)
start_button.grid(column=0,row=3)

#Creating the label for setting the tick marks after completing work sessions
tick_label = Label(text="",bg=YELLOW,fg=GREEN,highlightthickness=0)
tick_label.grid(column=1,row=3)

window.mainloop()