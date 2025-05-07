import streamlit as st
import requests
import os
from dotenv import load_dotenv  # ✅ Correct import

# Load API key
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# UI
st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌤️ Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city:
        data = get_weather(city)
        if data:
            st.success(f"Weather in {data['name']}, {data['sys']['country']}")
            st.write(f"**Condition**: {data['weather'][0]['description'].title()}")
            st.write(f"**Temperature**: {data['main']['temp']} °C")
            st.write(f"**Humidity**: {data['main']['humidity']}%")
            st.write(f"**Wind Speed**: {data['wind']['speed']} m/s")
        else:
            st.error("City not found or API limit reached.")
    else:
        st.warning("Please enter a city name.")
