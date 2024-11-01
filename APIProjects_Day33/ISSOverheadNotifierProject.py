import requests
import datetime as dt
import smtplib

#MY_LAT = 48.775845
#MY_LONG = 9.182932

MY_LAT = -45.3759 #Latitude for testing
MY_LONG = -139.1616 #Longitude for testing

#Setting email and secured  password for sending the mail
email = "meghnanegi510@gmail.com" #Sender's email
password = "uguc qaav zcfa yslg" #Sender's password

#The parameters to get the sunrise and sunset time of current location(24 hours format)
parameters = {
    "lat": 48.775845,
    "lng":9.182932,
    "formatted":0,
}

#Getting the sunrise and sunset "hour" for our location
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()
sunrise = int((data['results']['sunrise'].split("T"))[1].split(":")[0])
sunset = int((data['results']['sunset'].split("T"))[1].split(":")[0])

#Getting the current hour at our location
time_now = dt.datetime.now()
hour_now = int(str(time_now).split(" ")[1].split(":")[0])

#Getting the current latitude and longitude coordinates for the ISS
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_loc = iss_response.json()
current_lat = float(iss_loc['iss_position']['latitude'])
current_long = float(iss_loc['iss_position']['longitude'])

#Checking if the ISS is near my location (+5 or -5 of my latitude and longitude of my location)
#Checking if the hour is between sunset and midnight or between midnight and sunrise
#If above conditions are satisfied send the mail
if(min(MY_LAT-5.0,MY_LAT+5.0) < current_lat < max(MY_LAT-5.0,MY_LAT+5.0)):
    if(min(MY_LONG-5.0,MY_LONG+5.0) < current_long < max(MY_LONG-5.0,MY_LONG+5.0)):
        if(sunset < hour_now < 24 or 0 < hour_now < sunrise):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email,password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs="",
                    msg="Subject:Look Outside \n\n Go outside and look up, ISS is just above you" 
                ) 