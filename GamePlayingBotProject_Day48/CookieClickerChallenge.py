import time
from selenium import webdriver
from selenium.webdriver.common.by import By


game_on = True

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

#Getting form from the cookie game site 
driver = webdriver.Chrome(options=web_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button=driver.find_element(By.CSS_SELECTOR,value="#cookie")

while(game_on):
    timeout = time.time() + 10
    cookie_button.click()