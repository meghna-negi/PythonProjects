import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv

#Getting the environment variables
config = dotenv.dotenv_values("./.env")
username = config['LI_MAIL']
password = config['LI_PSWD']


#Creating web driver for chrome browser
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)


#Creating driver for chrome for the linkedin feed
driver = webdriver.Chrome(options=web_options)
driver.get("https://www.linkedin.com/feed/")
original_window = driver.current_window_handle

#Entering the login details and signing in
UserName = driver.find_element(By.ID, value='username')
UserName.send_keys(username)
Password = driver.find_element(By.ID, value='password' )
Password.send_keys(password)
SignIn_Button = driver.find_element(By.CSS_SELECTOR,value='.login__form_action_container button').click()

#Giving time for the load the feed and to manually bypass verification
time.sleep(15)

#Clicking on jobs icon and entering the title to be searched for
jobs_button = driver.find_element(By.XPATH,value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs_button.send_keys(Keys.ENTER)
time.sleep(5)
job_desc = driver.find_element(By.CLASS_NAME,value='jobs-search-global-typeahead__input')
job_desc.send_keys('Python Developer',Keys.ENTER)
time.sleep(5)

#Setting the easy apply filter
easy_apply = driver.find_element(By.CSS_SELECTOR,value='.search-reusables__filter-binary-toggle button').click()
time.sleep(2)

#Getting the list of job listings for the entered position with easy apply filter
jobs_div = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")
job_lists = driver.find_elements(By.CSS_SELECTOR,value='.job-card-container--clickable')

#Going through each listing and saving it
for job in job_lists:

    #Clicking on jobs one by one
    job.click()
    time.sleep(2)

    #If Job is not already saved then save
    save_button = driver.find_element(By.CSS_SELECTOR,value=".jobs-save-button")
    if "Saved" not in save_button.text:
        save_button.click()
    time.sleep(2)

    #Open the company page on separate tab
    company_page = driver.find_element(By.CSS_SELECTOR,value=".job-details-jobs-unified-top-card__company-name a")
    driver.execute_script(f"window.open('{company_page.get_attribute('href')}');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)

    #Follow the company page if not yet followed
    follow_button = driver.find_element(By.CSS_SELECTOR,value=".follow")
    if follow_button.text != "Following":
        follow_button.click()

    #Closing the current window and going back to the original window
    driver.close()
    driver.switch_to.window(original_window)
    time.sleep(5)
    driver.execute_script(f'arguments[0].scrollTop += {job.size["height"]}', jobs_div)

driver.quit()
