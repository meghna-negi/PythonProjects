from tkinter import *

#Function to calculate the kms in the miles
def miles_to_kms():
    miles = float(input_box.get())
    km= miles * 1.609
    km_output_label.config(text=f'{km}')

#Creating a window
window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=20,pady=20)

#Creating a entry box
input_box = Entry()
input_box.grid(column=1, row=0)

#Creating a label for mile unit
miles_label = Label(text="miles")
miles_label.config(padx=10,pady=10)
miles_label.grid(column=2,row=0)

#Creating a label for is equal to text
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

#Creating a output lbbel
km_output_label = Label(text="0")
km_output_label.grid(column=1,row=1)

#Creating a label for kilometer unit
km_label = Label(text="kilometers")
km_label.grid(column=2,row=1)

#Creating a button to trigger the conversion of miles to kms
calculate_button = Button(text='Calculate',command=miles_to_kms)
calculate_button.grid(column=1,row=3)

window.mainloop()