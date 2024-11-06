import requests
import datetime as dt

#The credentials and endpoint for Nutritionix API
APP_ID = ''
API_KEY = ''
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

#Header for the Nutritionix API
NUTRITIONIX_Headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

#Getting user's input for the parameters
parameters = {
    "query": input("Tell me which exercises you did?")
}

#Getting the calories,duration and exercise based on user's input
nutiritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT,json=parameters,headers=NUTRITIONIX_Headers)
nutiritionix_data = nutiritionix_response.json()['exercises']

#Credentials and endpoint for the SHEETY API
username = ''
project_name = 'workoutTracking'
sheet_name = 'workouts'
SHEETY_AUT_KEY = ''
SHEETY_ENDPOINT = f'https://api.sheety.co/{username}/{project_name}/{sheet_name}'

#Header for the SHEETY API
SHEETY_Headers = {
    "Authorization": SHEETY_AUT_KEY
}

#Getting current date and time in specific format to enter in the sheet
entry_date = dt.date.today().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

#Add all the exercise entered by the user in the sheet on separate rows
#Adding the duration and calories counted by the Nutritionix API
for index in range(len(nutiritionix_data)):
    column_data = {
        "workout": {
                "date": entry_date,
                "time": time,
                "exercise": nutiritionix_data[index]['user_input'].title(),
                "duration": nutiritionix_data[index]['duration_min'],
                "calories": nutiritionix_data[index]['nf_calories'],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT,json=column_data,headers=SHEETY_Headers)
    print(sheety_response.text)


