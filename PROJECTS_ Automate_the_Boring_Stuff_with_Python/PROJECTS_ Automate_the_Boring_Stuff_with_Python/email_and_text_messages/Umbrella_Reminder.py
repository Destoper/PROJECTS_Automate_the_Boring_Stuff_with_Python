# Sends a message to your cell phone if there is a chance of rain in your city

import json, requests, sys
from twilio.rest import TwilioRestClient

APPID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Your API key from openweathermap.org
lat = '-12.9711' # lat from your city
lon = '-38.5108' # lon from your city

def get_weather(APPID, lat, lon):    
    # Download the JSON data from openweathermap.org's API
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APPID}'
    response = requests.get(url)
    response.raise_for_status()
    # Load JSON data into Python variable.
    weatherData = json.loads(response.text)
    # Make a list with the main weather and its description
    data = [weatherData['weather'][0]['main'], weatherData['weather'][0]['description']]
    return data   
   
def send_message(message):
    account_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'      # Your twilio acount sid
    auth_Token  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'        # Your twilio auth token
    my_number = '+-------------'                            # Your cell phone number
    twilio_mumber = '+----------'                           # the twilio number

    client = TwilioRestClient(account_SID, auth_Token)
    client.messages.create(body=message, from_=twilio_mumber, to=my_number)


weather = get_weather(APPID, lat, lon)
possible_rain = ['Clouds', 'Snow', 'overcast clouds']

if weather[0] in possible_rain and weather[1] in possible_rain:
    message =  "The weather is cloudy and there's overcast clouds, high chance of rain today! Take an umbrella."
    send_message(message)
elif weather[0] in possible_rain:
    message =  'The weather is cloudy, there is a remote possibility of rain.'
    send_message(message)
else:
    print('No message send today.')