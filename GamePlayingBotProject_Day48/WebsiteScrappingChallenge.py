from selenium import webdriver
from selenium.webdriver.common.by import By
event_dict = {}

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

#Getting data from python.org live site 
driver = webdriver.Chrome(options=web_options)
driver.get("https://www.python.org/")

#Getting the upcomin events time and name from the site
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

#Saving the time and date for each event in dictionary
for event in range(len(events)):
    temp_dict = {}
    temp_dict['time'] = events[event].text
    temp_dict['name'] = names[event].text
    event_dict[event] = temp_dict
    
print(event_dict)