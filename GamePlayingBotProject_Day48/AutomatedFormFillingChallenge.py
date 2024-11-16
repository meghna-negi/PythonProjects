from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

#Getting form from the site 
driver = webdriver.Chrome(options=web_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

#Getting the elements using name, filling it and submitting it
FName = driver.find_element(By.NAME, value='fName')
FName.send_keys("Meghna")
LName = driver.find_element(By.NAME, value='lName')
LName.send_keys("Negi")
Email = driver.find_element(By.NAME, value='email')
Email.send_keys("megneg@abc.com",Keys.ENTER)

