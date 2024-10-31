import smtplib
import datetime as dt
import random
import pandas as pd

PLACEHOLDER = '[NAME]'

#Choosing the random letter from the available templates of letter
letters = ['letter_1','letter_2','letter_3']
current_letter = random.choice(letters)

#The email and the password generated for the python app
email = ""
password = ""

#Check if the date and month of today's match with someone in the csv file
#Replace the name of the person whose birthday is today in the chosen letter template
#Send the modified letter to the person 
now = dt.datetime.now()
birthday_df = pd.read_csv("./Birthdays.csv")
for i,row in birthday_df.iterrows():
    if(row['day'] == now.day):
        if(row['month'] == now.month):
            with open(f"./letter_templates/{current_letter}.txt",mode='r') as letterFile:
                content = letterFile.read() 
            message = content.replace(PLACEHOLDER,row['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=row['email'],
            msg=f"Subject:Happy Birthday!!!\n\n{message}"
        )
                    
        
