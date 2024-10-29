from tkinter import *
import pandas as pd
import random

words_df = pd.read_csv("./data/GermanWordsList.csv")
words_dict = words_df.to_dict()

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas_front = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
canvas_front.create_image(400,265,image=front_image)
language_name = canvas_front.create_text(400,150,text="German",fill="black",font=('Ariel',40,'italic'))
word = canvas_front.create_text(400,263,text="Ich",fill="black",font=('Ariel',60,'bold'))
canvas_front.grid(column=0,row=0,columnspan=2)

#canvas_back = Canvas(height=300,width=300,bg=BACKGROUND_COLOR,highlightthickness=0)
#back_image = PhotoImage(file="./images/card_back.png")
#canvas_back.create_image(300,300,image=back_image)
#canvas_back.grid(column=1,row=1,columnspan=3)

canvas_cross = Canvas(bg=BACKGROUND_COLOR,highlightthickness=0)
cross_image = PhotoImage(file="./images/wrong.png")
canvas_cross.create_image(200,50,image=cross_image)
canvas_cross.grid(column=0,row=1)

canvas_tick = Canvas(bg=BACKGROUND_COLOR,highlightthickness=0)
tick_image = PhotoImage(file="./images/right.png")
canvas_tick.create_image(180,50,image=tick_image)
canvas_tick.grid(column=1,row=1)

window.mainloop()