import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)


#Creating driver for chrome for the linkedin feed
driver = webdriver.Chrome(options=web_options)
driver.get("https://www.linkedin.com/feed/")

#Entering the login details and signing in
UserName = driver.find_element(By.ID, value='username')
UserName.send_keys("")
Password = driver.find_element(By.ID, value='password' )
Password.send_keys("")
SignIn_Button = driver.find_element(By.CSS_SELECTOR,value='.login__form_action_container button').click()

#Giving time for the load the feed
time.sleep(15)

#Clicking on jobs icon and entering the title to be searched for
jobs_button = driver.find_element(By.XPATH,value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
print(jobs_button)
jobs_button.send_keys(Keys.ENTER)
time.sleep(5)
job_desc = driver.find_element(By.CLASS_NAME,value='jobs-search-global-typeahead__input')
job_desc.send_keys('Python Developer',Keys.ENTER)
time.sleep(5)

#Setting the easy apply filter
easy_apply = driver.find_element(By.CSS_SELECTOR,value='.search-reusables__filter-binary-toggle button').click()
time.sleep(2)

#Getting the list of job listings for the entered position with easy apply filter
job_lists = driver.find_elements(By.CSS_SELECTOR,value='.job-card-container--clickable')
print(len(job_lists))

#Going through each listing and saving it
for job in job_lists:
    job.click()
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR,value=".jobs-save-button")
    save_button.click()
    time.sleep(30)


