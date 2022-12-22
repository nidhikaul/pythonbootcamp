import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
APP_ID = os.environ.get('APP_ID')
FROM_PH = os.environ.get('FROM_PH')
TO_PH = os.environ.get('TO_PH')

parameters = {
    "appid" : APP_ID,
    "lat" : 39.738449,
    "lon" : -104.984848,
    "exclude" : "current,minutely,daily"
    }

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
# response.raise_for_status()
print(response.status_code)
weather_data = response.json()
print(weather_data)
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(  
                              from_=FROM_PH, 
                              body="Bring an umbrella",      
                              to=TO_PH
                          ) 
 
    print(message.status)


# trial = weather_data["hourly"][0]["weather"][0]["id"]

