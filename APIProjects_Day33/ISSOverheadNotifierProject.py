import requests
import datetime as dt
import smtplib
import time

MY_LAT = 48.775845 #Current location's latitude
MY_LONG = 9.182932 #Current location's longitude

#Setting email and secured  password for sending the mail
email = "" #Sender's email
password = "" #Sender's password

#The parameters to get the sunrise and sunset time of current location(24 hours format)
parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

#Checking if the ISS is near my location (+5 or -5 of my latitude and longitude of my location)
def is_iss_near(current_lat,current_long) -> bool:

    min_lat = min(MY_LAT-5.0,MY_LAT+5.0)
    max_lat = max(MY_LAT-5.0,MY_LAT+5.0)
    min_long = min(MY_LONG-5.0,MY_LONG+5.0)
    max_long = max(MY_LONG-5.0,MY_LONG+5.0)

    if(min_lat < current_lat < max_lat):
        if(min_long < current_long < max_long):
            return(True)
    return(False)

#Checking if the hour is between sunset and midnight or between midnight and sunrise
def is_night(time_now) -> bool:
    if(sunset < time_now < 24 or 0 < time_now < sunrise):
        return(True)
    return(False)

#Getting the sunrise and sunset "hour" for our location
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()
sunrise = int((data['results']['sunrise'].split("T"))[1].split(":")[0])
sunset = int((data['results']['sunset'].split("T"))[1].split(":")[0])

#Getting the current hour at our location
time_now = dt.datetime.now().hour

#Getting the current latitude and longitude coordinates for the ISS
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_loc = iss_response.json()
current_lat = float(iss_loc['iss_position']['latitude'])
current_long = float(iss_loc['iss_position']['longitude'])

#If ISS is nearby and it's nighttime send the mail and keep checking it each minute
while(True):
    time.sleep(60)
    if(is_iss_near(current_lat,current_long)):
        if(is_night(time_now)):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email,password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs="",
                    msg="Subject:Look Outside \n\n Go outside and look up, ISS is just above you" 
                ) 