import smtplib
import datetime as dt
import random

#The email and the password generated for the python app
email = ""
password = ""

#Reading the quotes from the txt file
with open("quotes.txt",encoding='utf8') as quote:
    quotes = quote.read()

#Storing the quotes in the list of quotes
list_quotes = quotes.split("\n")

#Getting the weekday of today and send the mail with randomly selected quote if it's monday
now = dt.datetime.now()
if(now.weekday() == 0):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="",
            msg=f"Subject:Monday Motivation \n\n {list_quotes[random.randint(0,101)]}".encode('utf8')
        )



