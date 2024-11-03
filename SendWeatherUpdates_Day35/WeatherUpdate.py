import requests
import smtplib

MY_LAT = 48.775845 #Current location's latitude
MY_LONG = 9.182932 #Current location's longitude

email = "" #Enter the email
password = "" #Enter the password

api_key = "" #Enter the generated api key of open weather api

#Parameters for the api call
parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid':api_key,
    'cnt':4
}

#Calling the api with the paramteres to get the data for a location in json file
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data['list']

#Set the flag to True if it there are chances of rain
will_rain = False

#To retrieve the weather id and if it is less than 700 then setting the flag to True
for weather in weather_list:
    predicted_weather = weather['weather'][0]['id']
    if(predicted_weather < 700):
        will_rain = True

#If there is a prediction of bad weather send the mail to send a reminder to carry umbrella
if(will_rain):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs='',
            msg="Subject:Weather Update\n\n It's going to rain. Bring your umbrella."
        )

