from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

#Lists of digits and symbols that can be used in password
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['@', ')', '$', '_', '&', '(', '!', '#']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Function to generate strong password with combination of letters,digits and symbols
#Enable copying of password from the password field to paste it on the signup page for website
def generate_pswd() -> None:
    pswd_text.delete(0,'end')
    pswd = ''

    num_letters = random.randint(8,10)
    num_digits = random.randint(2,4)
    num_symbols = random.randint(2,4)

    pswd_letters = [random.choice(string.ascii_letters) for letter in range(num_letters)]
    pswd_digits = [random.choice(DIGITS) for digit in range(num_digits)]
    pswd_symbols = [random.choice(SYMBOLS) for symbol in range(num_symbols)]
    pswd_list = pswd_letters + pswd_digits + pswd_symbols

    random.shuffle(pswd_list)
    pswd = ''.join(pswd_list)   
    pswd_text.insert(0,pswd)

    pyperclip.copy(pswd_text.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
#Function to save the credentials in the txt doc
#If the website or password are empty pop up warning box
#Else write the details into the txt doc and display pop up to confirm details with user before writing
def add_pswd() -> None:
    if(len(website_text.get()) == 0 or len(pswd_text.get()) == 0):
        messagebox.showwarning(title='Oops',message="Please don't leave any fields empty")
    else:    
        response = messagebox.askokcancel(title=website_text.get(),message= f"These are the credentials entered\nEmail: {email_text.get()}\n"
                                                                        f"Password: {pswd_text.get()}\nDo you want to save?")
        if(response):
            with open('passwordList.txt',mode='a') as file:
                file.write(f"{website_text.get()} | {email_text.get()} | {pswd_text.get()}\n")
                website_text.delete(0,'end')
                pswd_text.delete(0,'end')



# ---------------------------- UI SETUP ------------------------------- #
#Creating window and adjusting the properties
window = Tk()
window.config(padx=40,pady=40,background='white')
window.title("Password Manager")

#Creating the canvas to put the logo in the window
canvas = Canvas(height=200,width=200,background='white',highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

#Creating label and the entry box for the website detail
website_label = Label(text="Website:",background='white')
website_label.grid(column=0,row=1,sticky='we')
website_text = Entry(width=35)
website_text.grid(column=1,row=1,columnspan=2,sticky='we')

#Creating label and the entry box for the email detail, assigning the email name by default
email_label = Label(text="Email/Username:",background='white')
email_label.grid(column=0,row=2,sticky='we')
email_text = Entry(width=35)
email_text.insert(0,'meghna2345@gmail.com')
email_text.grid(column=1,row=2,columnspan=2,sticky='we')

#Creating label and the entry box for the password detail
pswd_label = Label(text="Password:",background='white')
pswd_label.grid(column=0,row=3,sticky='we')
pswd_text = Entry(width=21)
pswd_text.grid(column=1,row=3,sticky='we')

#Creating buttons to generate the password and to add the password in the txt doc
gen_pswd = Button(text='Generate Password',width=14,background='white',command=generate_pswd)
gen_pswd.grid(column=2,row=3,sticky='we')
add_pswd = Button(text='Add',width=35,background='white',command=add_pswd)
add_pswd.grid(column=1,row=4,columnspan=2,sticky='we')


window.mainloop()




