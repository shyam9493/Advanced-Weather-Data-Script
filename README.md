#  Advanced Weather Data Script

## Description
This project is a simple python script built using python3. It allows users to send email which contains the wheather report of a particular location.

## Table of Contents
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Output](#Output)
- [Approach](#approach)
- [Api](#api)
  

## Prerequisites
Before getting started, ensure you have the following prerequisites installed on your system:

- Git: [Download & Install](https://git-scm.com/downloads)
- Any IDE
- Python:[Download & Install](https://www.python.org/downloads/)
## Installation
To run this project locally, follow these steps:
- Clone the repository:
```bash
git clone https://github.com/shyam9493/Advanced-Weather-Data-Script.git
```
- locate to the folder where you have installed and create a file named '.env' and the content is 
```bash
WEATHER_API_KEY="Your_api_key"
GEMINI_API_KEY="Your_api_key"
Your_mail="Your_mail"
auth_password="your mail authentication password"
```
To get API key 
Sign up for a Weather.com API key at
(https://www.weatherapi.com/signup.aspx)

TO get gemini api
signup and create new api
[Signup](https://www.bing.com/ck/a?!&&p=58053060397588beJmltdHM9MTcxNDE3NjAwMCZpZ3VpZD0wMWNiMWQ1Ni00NzZlLTZkYjctMmY2ZS0wOTFkNDZjODZjNDUmaW5zaWQ9NTIxNA&ptn=3&ver=2&hsh=3&fclid=01cb1d56-476e-6db7-2f6e-091d46c86c45&psq=gemini+ai+api&u=a1aHR0cHM6Ly9haS5nb29nbGUuZGV2Lw&ntb=1)
- To get auth password it is mandatory that you should turn on two step authentication and search for app passwords and create a new password and that password is your auth_password
- To install requirements just run
```bash
pip install -r requirements.txt
```
- after successful installation to run the application go to terminal and enter
```bash
python main_mail.py
```

## Output
It will ask you to enter the email of the reciever and the location 
if you enter those your email will be sent successfully

## Approach

I first started creating a api for the weather.com and made a sample responses and then tried to send sample mails through smtp and then started to integrate gemini ai to generate emails and then I merged those 3 fields into a main_mail.py .


## API 
- Wheather.com api sample response
  ```bash
  {
    "location": {
        "name": "New Delhi",
        "region": "Delhi",
        "country": "India",
        "lat": 28.6,
        "lon": 77.2,
        "tz_id": "Asia/Kolkata",
        "localtime_epoch": 1714286003,
        "localtime": "2024-04-28 12:03"
    },
    "current": {
        "last_updated_epoch": 1714285800,
        "last_updated": "2024-04-28 12:00",
        "temp_c": 34,
        "temp_f": 93.2,
        "is_day": 1,
        "condition": {
            "text": "Mist",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/143.png",
            "code": 1030
        },
        "wind_mph": 2.2,
        "wind_kph": 3.6,
        "wind_degree": 287,
        "wind_dir": "WNW",
        "pressure_mb": 1009,
        "pressure_in": 29.8,
        "precip_mm": 0,
        "precip_in": 0,
        "humidity": 23,
        "cloud": 50,
        "feelslike_c": 32,
        "feelslike_f": 89.6,
        "vis_km": 3.5,
        "vis_miles": 2,
        "uv": 9,
        "gust_mph": 9,
        "gust_kph": 14.5
      }
    }
- Gemini ani sample response
```bash
Subject: Weather Update: Mist 

Hi [Recipient Name],

Just wanted to let you know that there's a bit of mist outside at the moment. Visibility might be a little reduced, so do take care if you're heading out and about. 

Regards,

Shyam
```

