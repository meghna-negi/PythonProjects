from tkinter import *
import requests

#Function to retrieve quotes from the api 
def retrieve_quotes() -> None:
    response = requests.get(url='https://api.kanye.rest')
    quote = response.json()
    canvas.itemconfig(canvas_quote,text=quote['quote'])

#Creating a window and assigning a title
window = Tk()
window.title("Kanye Says...")

#Creating a canvas with a background to write the quote 
canvas = Canvas(width=400,height=450)
quote_image = PhotoImage(file="background.png")
canvas.create_image(200,230,image=quote_image)
canvas_quote = canvas.create_text(200,210,text="Brace yourself!!!!!",font=("Ariel",15,"bold"),width=200,fill='white')
canvas.grid(column=0,row=0)

#Creating a button with kanye image on it
#When pressed retrieves the quote from the api and displays it on the screen in the canvas 
button_image = PhotoImage(file="kanye.png")
button = Button(image=button_image,borderwidth=0,command=retrieve_quotes)
button.grid(column=0,row=2)

window.mainloop()