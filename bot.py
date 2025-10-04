import os
import asyncio
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from weather import get_forecast, aggregate_daily_forecast, get_forecast_by_coords

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хранилище данных пользователя (язык)
user_data = {}

# Переводы интерфейса
translations_ui = {
    "ru": {
        "welcome": "Привет! Я бот прогноза погоды. Выбери язык:",
        "lang_selected": "Выбран язык: {lang_name}\nОтправь название города или поделись геолокацией, чтобы получить прогноз.",
        "share_location": "Поделись геолокацией или напиши город:",
        "fetching_city": "Получаю прогноз погоды для города: {city}...",
        "fetching_coords": "Получаю прогноз по координатам (lat: {lat}, lon: {lon})...",
        "forecast_city": "Прогноз погоды для <b>{city}</b>:\n\n",
        "error": "Ошибка при получении прогноза: {error}",
        "share_location_button": "Поделиться геолокацией",
        "temperature": "температура",
        "forecast_line": "{date}: {description} {emoji}, {temperature}: {temp}°C"
    },
    "en": {
        "welcome": "Hello! I'm a weather forecast bot. Choose a language:",
        "lang_selected": "Selected language: {lang_name}\nSend a city name or share your location to get the forecast.",
        "share_location": "Share your location or type a city name:",
        "fetching_city": "Fetching weather forecast for city: {city}...",
        "fetching_coords": "Fetching forecast for coordinates (lat: {lat}, lon: {lon})...",
        "forecast_city": "Weather forecast for <b>{city}</b>:\n\n",
        "error": "Error fetching forecast: {error}",
        "share_location_button": "Share location",
        "temperature": "temperature",
        "forecast_line": "{date}: {description} {emoji}, {temperature}: {temp}°C"
    },
    "uz": {
        "welcome": "Salom! Men ob-havo prognozi botiman. Tilni tanlang:",
        "lang_selected": "Tanlangan til: {lang_name}\nShahar nomini yuboring yoki geolokatsiyani ulashing.",
        "share_location": "Geolokatsiyani ulashing yoki shahar nomini yozing:",
        "fetching_city": "Shahar uchun ob-havo prognozini olmoqda: {city}...",
        "fetching_coords": "Koordinatalar uchun prognoz olmoqda (lat: {lat}, lon: {lon})...",
        "forecast_city": "<b>{city}</b> uchun ob-havo prognozi:\n\n",
        "error": "Prognozni olishda xatolik: {error}",
        "share_location_button": "Geolokatsiyani ulashish",
        "temperature": "harorat",
        "forecast_line": "{date}: {description} {emoji}, {temperature}: {temp}°C"
    }
}

# Переводы погодных описаний для узбекского
translations_weather = {
    "uz": {
        "clear sky": "Ochiq osmon",
        "few clouds": "Ozroq bulutli",
        "scattered clouds": "Tarqalgan bulutlar",
        "broken clouds": "Parcali bulutlar",
        "overcast clouds": "Bulutli",
        "light rain": "Yengil yomg‘ir",
        "moderate rain": "O‘rtacha yomg‘ir",
        "heavy intensity rain": "Kuchli yomg‘ir",
        "light snow": "Yengil qor",
        "snow": "Qor",
        "mist": "Tuman",
        "fog": "Tuman",
        "thunderstorm": "Momaqaldiroq"
    }
}

# Эмодзи для погодных состояний
weather_emojis = {
    "clear sky": "☀️",
    "few clouds": "⛅",
    "scattered clouds": "⛅",
    "broken clouds": "☁️",
    "overcast clouds": "☁️",
    "light rain": "🌧️",
    "moderate rain": "🌧️",
    "heavy intensity rain": "🌧️",
    "light snow": "❄️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "thunderstorm": "⛈️",
    "ochiq osmon": "☀️",
    "ozroq bulutli": "⛅",
    "tarqalgan bulutlar": "⛅",
    "parcali bulutlar": "☁️",
    "bulutli": "☁️",
    "yengil yomg‘ir": "🌧️",
    "o‘rtacha yomg‘ir": "🌧️",
    "kuchli yomg‘ir": "🌧️",
    "yengil qor": "❄️",
    "qor": "❄️",
    "tuman": "🌫️",
    "momaqaldiroq": "⛈️"
}

# Инлайн-кнопки для выбора языка
def get_language_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz"),
        ]
    ])
    return keyboard

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {"lang": "ru"}  # Русский по умолчанию
    lang = user_data[user_id]["lang"]
    await message.answer(
        translations_ui[lang]["welcome"],
        reply_markup=get_language_keyboard()
    )

@dp.callback_query(lambda c: c.data.startswith("lang_"))
async def process_language_selection(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang = callback.data.split("_")[1]  # ru, en, uz
    user_data[user_id]["lang"] = lang
    lang_names = {"ru": "Русский", "en": "English", "uz": "O‘zbek"}
    await callback.message.edit_text(
        translations_ui[lang]["lang_selected"].format(lang_name=lang_names[lang]),
        reply_markup=None
    )
    # Запрос геолокации
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=translations_ui[lang]["share_location_button"], request_location=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await callback.message.answer(translations_ui[lang]["share_location"], reply_markup=keyboard)

@dp.message(lambda message: message.location)
async def handle_location(message: Message):
    user_id = message.from_user.id
    lat = message.location.latitude
    lon = message.location.longitude
    lang = user_data.get(user_id, {"lang": "ru"})["lang"]
    # Получение названия города
    geolocator = Nominatim(user_agent="weather_bot")
    try:
        location = geolocator.reverse((lat, lon))
        city = location.address.split(",")[1].strip() if location else "Неизвестный город"
    except:
        city = "Неизвестный город"
    await message.answer(translations_ui[lang]["fetching_coords"].format(lat=lat, lon=lon))
    try:
        forecasts = get_forecast_by_coords(lat, lon, lang)
        daily_forecasts = aggregate_daily_forecast(forecasts)
        forecast_message = translations_ui[lang]["forecast_city"].format(city=city)
        for forecast in daily_forecasts:
            date = datetime.datetime.fromtimestamp(forecast["dt"]).strftime("%d.%m.%Y")
            temp_day = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"].capitalize()
            # Перевод на узбекский
            if lang == "uz" and description.lower() in translations_weather["uz"]:
                description = translations_weather["uz"][description.lower()]
            emoji = weather_emojis.get(description.lower(), "🌦️")
            forecast_message += translations_ui[lang]["forecast_line"].format(
                date=date, description=description, emoji=emoji, temperature=translations_ui[lang]["temperature"], temp=temp_day
            ) + "\n"
        await message.answer(forecast_message, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        await message.answer(translations_ui[lang]["error"].format(error=e), reply_markup=types.ReplyKeyboardRemove())

@dp.message()
async def handle_city(message: Message):
    city = message.text.strip()
    user_id = message.from_user.id
    lang = user_data.get(user_id, {"lang": "ru"})["lang"]
    await message.answer(translations_ui[lang]["fetching_city"].format(city=city))
    try:
        forecasts = get_forecast(city, lang)
        daily_forecasts = aggregate_daily_forecast(forecasts)
        forecast_message = translations_ui[lang]["forecast_city"].format(city=city)
        for forecast in daily_forecasts:
            date = datetime.datetime.fromtimestamp(forecast["dt"]).strftime("%d.%m.%Y")
            temp_day = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"].capitalize()
            # Перевод на узбекский
            if lang == "uz" and description.lower() in translations_weather["uz"]:
                description = translations_weather["uz"][description.lower()]
            emoji = weather_emojis.get(description.lower(), "🌦️")
            forecast_message += translations_ui[lang]["forecast_line"].format(
                date=date, description=description, emoji=emoji, temperature=translations_ui[lang]["temperature"], temp=temp_day
            ) + "\n"
        await message.answer(forecast_message, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        await message.answer(translations_ui[lang]["error"].format(error=e), reply_markup=types.ReplyKeyboardRemove())

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")