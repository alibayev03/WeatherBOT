import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_forecast(city: str, lang: str = "ru") -> list:
    if not WEATHER_API_KEY:
        raise ValueError("WEATHER_API_KEY не найден в .env")
    
    forecast_url = (
        f"http://api.openweathermap.org/data/2.5/forecast?"
        f"q={city}&units=metric&appid={WEATHER_API_KEY}&lang={lang}"
    )
    try:
        response = requests.get(forecast_url)
        response.raise_for_status()
        data = response.json()
        if "list" in data:
            return data["list"]
        else:
            raise Exception(f"Ошибка получения прогноза погоды. Ответ API: {data}")
    except requests.RequestException as e:
        raise Exception(f"Ошибка запроса к API: {str(e)}")

def get_forecast_by_coords(lat: float, lon: float, lang: str = "ru") -> list:
    if not WEATHER_API_KEY:
        raise ValueError("WEATHER_API_KEY не найден в .env")
    
    forecast_url = (
        f"http://api.openweathermap.org/data/2.5/forecast?"
        f"lat={lat}&lon={lon}&units=metric&appid={WEATHER_API_KEY}&lang={lang}"
    )
    try:
        response = requests.get(forecast_url)
        response.raise_for_status()
        data = response.json()
        if "list" in data:
            return data["list"]
        else:
            raise Exception(f"Ошибка получения прогноза погоды. Ответ API: {data}")
    except requests.RequestException as e:
        raise Exception(f"Ошибка запроса к API: {str(e)}")

def aggregate_daily_forecast(forecasts: list) -> list:
    daily = {}
    for forecast in forecasts:
        dt_txt = forecast.get("dt_txt")
        if not dt_txt:
            continue
        date_str, time_str = dt_txt.split(" ")
        if date_str not in daily:
            daily[date_str] = forecast
        if time_str == "12:00:00":
            daily[date_str] = forecast
    daily_forecasts = [daily[date] for date in sorted(daily.keys())]
    return daily_forecasts