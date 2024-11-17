import time
from selenium import webdriver
from selenium.webdriver.common.by import By

game_on = True

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

#Creating driver for chromw for the cookie game site 
driver = webdriver.Chrome(options=web_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#Getting cooking clicking button
cookie_button=driver.find_element(By.CSS_SELECTOR,value="#cookie")

#Getting the upgrade list
upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
upgrades_id = [item.get_attribute("id") for item in upgrades]

#Setting timeout for checking upgrades and to display the cookie per sec
timeout = time.time() + 5
checktime = time.time() + 60*5

#Loop to run the code
while(game_on):

    #Automated clicking the cookie button 
    cookie_button.click()

    #Check the upgrades after the time interval set at beginning
    if(time.time() > timeout):

        #Getting the cost of each upgardes
        prices_text = driver.find_elements(By.CSS_SELECTOR,value='#store b')
        prices = []

        #Getting the value of cost of each upgardes
        for items in prices_text:
            if items.text != '':
                price_str = items.text.split("-")[-1].strip()
                price = "".join(price_str.split(','))
                prices.append(price)

        #Get the current cookie number
        money_text = (driver.find_element(By.CSS_SELECTOR,value="#money")).text
        money = "".join(money_text.split(','))

        #Creating the dictionary for the upgardes id and cost
        cookie_upgrades = {}
        for price in range(len(prices)):
            cookie_upgrades[prices[price]] = upgrades_id[price]

        #Reversing the dictionary to get the expensive upgardes at the starting
        cookie_upgrades = dict(reversed(cookie_upgrades.items()))

        #Checking if current money is more than the cost of upgrade item
        #If yes then click the upgarde button and wait for 5ms
        for price,id in cookie_upgrades.items():
            if(int(money)>int(price)):
                upgrade_button = (driver.find_element(By.ID,value=id)).click()
                time.sleep(0.05)

        #Increase the timeout by the decided seconds
        timeout = time.time() + 20

    #If 5 mins have passed display the cookie per second
    if(time.time()>checktime):
        cookie_per_sec = driver.find_element(By.CSS_SELECTOR,value="#cps").text
        print(cookie_per_sec)
        game_on = False

driver.quit()