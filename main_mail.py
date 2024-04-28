#Wheather.com 
import requests
def get_weather_data(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data:", response.status_code)
        return None

#gemini ai
import google.generativeai as genai
def generate_email(weather_data,GEMINI_API_KEY):
    try:
        if not GEMINI_API_KEY:
            print("no api key")
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        convo = model.start_chat(history=[])
        weather_data_str = str(weather_data)
        convo.send_message(f"Generate an email body that describes the following weather conditions in a human-readable format: {weather_data_str}. The email should start with a greeting and end with a polite closing and write regards with a sample name Shyam")
        return convo.last.text.replace("[Name]", "User")
    except Exception as e:
        print("An error occurred while generating the email.")
#email
import smtplib
import os
!pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
email=os.getenv('Your_mail')
re_email=input("Enter reciever mail : ")
api_key = os.getenv('WEATHER_API_KEY')
location = input("Enter your location : ")
try:
  weather_data = get_weather_data(api_key, location)
except Exception as e:
   print("Api error ")
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
try:
  text=get_weather_data(api_key, location)
except Exception as e:
  print(e)
try:
  sample="Location"+text['location']['name']
  sample+="\n Wheather condition"+text['current']['condition']['text']
  sample+="\n Temperature C"+str(text['current']['temp_c'])
  sample+="\n Humidity"+str(text['current']['humidity'])
  sample+="\n precipitation"+str(weather_data['current']['precip_mm'])
except Exception as e:
  print('Error getting location try correcting your api')
try:
  email_text=generate_email(sample,GEMINI_API_KEY)
except Exception as e:
  print('error generating email text')
try:
  server=smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(email,"etjkthvoscdqjoej")
  server.sendmail(email,re_email,str(email_text))
  print(f"Mail sent successfully to {re_email}")
except Exception as e:
  print('error sending mail')