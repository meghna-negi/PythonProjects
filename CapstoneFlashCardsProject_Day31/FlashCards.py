from tkinter import *
import pandas as pd
import random
from pathlib import Path

#Checking if the words to learn file exists
#If yes, load the words from there, if not then from the main csv file
#This is to save the progress, and to only see the words that a person doesn't know
file_name = Path("./data/Words_to_learn.csv")
if file_name.is_file():
    words_df = pd.read_csv("./data/Words_to_learn.csv")
else:
    words_df = pd.read_csv("./data/GermanWordsList.csv")
words_list = words_df.to_dict(orient='records')

BACKGROUND_COLOR = "#B1DDC6"
new_word = {}

#Function to move to the next word and turn the flash card after 3sec
def change_card() -> None:
    global new_word
    new_word = random.choice(words_list)
    canvas_front.itemconfig(canvas_image,image=front_image)
    canvas_front.itemconfig(language_name,text='German',fill='black')
    canvas_front.itemconfig(word,text=new_word['German'],fill='black')
    window.after(3000,flip_card,new_word)

#Function to flip the card and display english meaning of the given word
def flip_card(new_word) -> None:
    canvas_front.itemconfig(canvas_image,image=back_image)
    canvas_front.itemconfig(language_name,text='English',fill='white')
    canvas_front.itemconfig(word,text=new_word['English'],fill='white')

#Function to add the not known German words to the csv file
def is_known() -> None:
    words_list.remove(new_word)
    words_to_learn_df = pd.DataFrame(words_list)
    words_to_learn_df.to_csv("./data/Words_to_learn.csv",index=False)
    change_card()

#Creating window and adjusting the properties
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Creating canvas and setting its properties, creating the image for front and back of the card
canvas_front = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas_front.create_image(400,265,image=front_image)
language_name = canvas_front.create_text(400,150,text="",fill="black",font=('Ariel',40,'italic'))
word = canvas_front.create_text(400,263,text="",fill="black",font=('Ariel',60,'bold'))
canvas_front.grid(column=0,row=0,columnspan=2)

#Creating button for the don't know the word
cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(text='cross',image=cross_image,command=change_card,highlightthickness=0,borderwidth=0)
wrong_button.grid(column=0,row=1)

#Creating the button for the know the word
tick_image = PhotoImage(file='./images/right.png')
right_button = Button(text='tick',image=tick_image,command=is_known,highlightthickness=0,borderwidth=0)
right_button.grid(column=1,row=1)

#Calling the function to change the flash cards
change_card()

window.mainloop()