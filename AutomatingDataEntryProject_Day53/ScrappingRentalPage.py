import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

#Getting the page from the clone website of Zillow
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
rental_page = response.text
Data = BeautifulSoup(rental_page,'html.parser')

#Getting the address and the location links for the listings on the page
#Removing extra spaces and symbol from the address
listings_add = Data.find_all(name='a',class_='StyledPropertyCardDataArea-anchor')
address = [(place('address')[0].get_text()).replace("|","").strip() for place in listings_add]
address_link = [place['href'] for place in listings_add]

#Getting the price for the listings in the page
#Removing the extra symbols from the price value
listings_price = Data.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine')
price = [(place.get_text()).replace("/mo","").split('+')[0] for place in listings_price]

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

#Creating driver for chrome for google form
driver = webdriver.Chrome(options=web_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdM5IjCNSTh-XEE6hUZXVA0fyIgEo5jMebepa7tz7j7hKnBrQ/viewform?usp=sf_link")

#Iterating through all the listings and filling the google form
#Adding the address, address link and the price to the questions and sending the response
for index in range(len(address)):
    Address = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Address.send_keys(address[index])

    Price = driver.find_element(By.XPATH,value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Price.send_keys(price[index])

    Address_Link = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Address_Link.send_keys(address_link[index])

    Send_Button = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(2)
    
    Next_response = driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(2)