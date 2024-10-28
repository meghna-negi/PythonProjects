from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

#Lists of digits and symbols that can be used in password
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['@', ')', '$', '_', '&', '(', '!', '#']

# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
#Function to search the credentials for the website
#If credentials are found for website, display it
#Else display result not found
def search_pswd() -> None:
    try:
        with open("passwordList.json", mode='r') as file:
            password = json.load(file)

    except FileNotFoundError:
            messagebox.showerror(title="Error",message="No Data File Found.")
    else:        
        if website_text.get() in password:
            email = password[website_text.get()]['email']
            pswd = password[website_text.get()]['password']
            messagebox.showinfo(title=website_text.get(),message=f"The credentials for {website_text.get()} are:\n"
                                                        f"Email: {email}\n"
                                                        f"Password: {pswd}")
        else:
            messagebox.showinfo(title=website_text.get(),message=f"The credentials for {website_text.get()} are not found.\n")


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
    new_pswd = {
        website_text.get():{
                "email":email_text.get(),
                "password":pswd_text.get(),
            }
        }
    if(len(website_text.get()) == 0 or len(pswd_text.get()) == 0):
        messagebox.showwarning(title='Oops',message="Please don't leave any fields empty")
    else:    
        response = messagebox.askokcancel(title=website_text.get(),message= f"These are the credentials entered\nEmail: {email_text.get()}\n"
                                                                        f"Password: {pswd_text.get()}\nDo you want to save?")
        if(response):
            try:
                with open('passwordList.json',mode='r') as file:
                    pswd = json.load(file)              
            except FileNotFoundError:
                with open('passwordList.json',mode='w') as file:    
                    json.dump(new_pswd, file,indent=4)
            else:
                pswd.update(new_pswd)
                with open('passwordList.json',mode='w') as file:    
                    json.dump(pswd, file,indent=4)
            finally:
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
website_text = Entry(width=21)
website_text.grid(column=1,row=1,sticky='we')

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

#Creating buttons to generate the password and to add and search the password in the txt doc
gen_pswd = Button(text='Generate Password',width=14,background='white',command=generate_pswd)
gen_pswd.grid(column=2,row=3,sticky='we')
add_password = Button(text='Add',width=35,background='white',command=add_pswd)
add_password.grid(column=1,row=4,columnspan=2,sticky='we')
search_pswd = Button(text='Search',width=14,background='white',command=search_pswd)
search_pswd.grid(column=2,row=1,sticky='we')

window.mainloop()




