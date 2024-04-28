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