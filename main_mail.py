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
