from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv

#Getting the environment variables
config = dotenv.dotenv_values("./.env")
email = config['EMAIL_ADD']
pswd = config['EMAIL_PSWD']
to_email = config['TO_EMAIL_ADD']

#Header for retreiving the amazon data
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,lb;q=0.7", 
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Chrome/130.0.0.0",
  }

#Getting the data from the amazon website
URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
response = requests.get(url=URL,headers=headers)
data = response.text

#Scrapping the amazon site for the product
Soup = BeautifulSoup(data,"html.parser")

#Getting the title and the price for product
title = Soup.find(name='span',class_='a-size-large product-title-word-break')
product_title = title.text
price = Soup.find(name='span',class_='a-offscreen')
listed_price = price.text.split("$")[1]
print(listed_price)
print("\n")
print(product_title)

#Setting the desired price for the product
target_price = 90.00

#If the listed price is less than desired price, send the mail
if(float(listed_price) < target_price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=pswd)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject:Price Decrease Alert!!!\n\nThe price for instant pot has dropped to {listed_price}."
            )
