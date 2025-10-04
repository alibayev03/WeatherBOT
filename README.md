# ObHavo+ - Telegram Weather Bot

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/твой_бот_юзернейм)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![AIogram](https://img.shields.io/badge/AIogram-3.18.0-red.svg)](https://github.com/aiogram/aiogram)

## Описание
**ObHavo+** — это мультиязычный Telegram-бот для получения прогноза погоды на 5 дней. Бот поддерживает русский, английский и узбекский языки, отображение эмодзи для погодных условий и определение города по геолокации (с помощью Nominatim).  

Прогноз предоставляется через OpenWeatherMap API. Бот использует **aiogram** для асинхронной обработки сообщений и **geopy** для обратного геокодирования координат.  

### Основные фичи
- **Выбор языка**: 🇷🇺 Русский, 🇬🇧 English, 🇺🇿 O‘zbek.
- **Прогноз по городу**: Введите название (например, "Tashkent").
- **Геолокация**: Поделитесь местоположением — бот определит город автоматически.
- **Переводы**: Полный интерфейс на выбранном языке (например, "температура" → "harorat" / "temperature").
- **Эмодзи**: ☀️ Ясно, ☁️ Пасмурно, 🌧️ Дождь и т.д.
- **Обработка ошибок**: Дружественные сообщения при неверном городе или проблемах с API.

### Демо
1. Отправьте `/start` боту.
2. Выберите язык (🇺🇿 O‘zbek).
3. Поделитесь геолокацией или введите "Tashkent".
4. Получите прогноз (на 05.10.2025, 03:29 AM +05):

Ob-havo prognozi uchun Toshkent:
05.10.2025: Bulutli ☁️, harorat: 21.64°C
06.10.2025: Ochiq osmon ☀️, harorat: 21.46°C
...
text## Требования
- Python 3.8+.
- Telegram Bot Token (от [@BotFather](https://t.me/BotFather)).
- API Key от [OpenWeatherMap](https://openweathermap.org/api) (бесплатно до 1000 запросов/день).

## Установка
1. **Клонируйте репозиторий**:
git clone https://github.com/твой_логин/WeatherBOT.git
cd WeatherBOT
text2. **Создайте виртуальное окружение**:
python -m venv venv
source venv/bin/activate  # Linux/Mac
или
venv\Scripts\activate  # Windows
text3. **Установите зависимости**:
pip install -r requirements.txt
text4. **Настройте .env**:
Создайте файл `.env` в корне:
BOT_TOKEN=your_telegram_bot_token_here
WEATHER_API_KEY=your_openweather_api_key_here
text5. **Запустите бота**:
python bot.py
text## Структура проекта
WeatherBOT/
├── bot.py              # Основной код бота (aiogram, обработчики)
├── weather.py          # Функции для API погоды и агрегации прогноза
├── requirements.txt    # Зависимости
├── Procfile           # Для деплоя (Render/Railway)
├── .gitignore         # Игнор файлов
└── .env               # Переменные (не коммитьте!)
text## Деплой
### Render.com (рекомендуется, бесплатно до 750 ч/мес)
1. Запушьте на GitHub (см. ниже).
2. На render.com: "New +" → "Background Worker" → Подключите GitHub-репозиторий.
3. Build: `pip install -r requirements.txt`.
4. Start: `python bot.py`.
5. Environment Variables: Добавьте `BOT_TOKEN` и `WEATHER_API_KEY`.
6. Deploy!

### PythonAnywhere (альтернатива, бесплатно 24/7)
1. Зарегистрируйтесь на [pythonanywhere.com](https://www.pythonanywhere.com/).
2. Загрузите файлы в `/home/твой_логин/`.
3. Установите зависимости: `pip3.10 install --user -r requirements.txt`.
4. Добавьте переменные окружения (`BOT_TOKEN`, `WEATHER_API_KEY`).
5. Настройте scheduled task: `python3.10 /home/твой_логин/bot.py` (continuously).

### GitHub
- Создайте репозиторий на github.com.
- В папке проекта:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/твой_логин/WeatherBOT.git
git push -u origin main
text## API и ключи
- **Telegram Bot Token**: Получите у [@BotFather](https://t.me/BotFather) командой `/newbot`.
- **OpenWeatherMap API**: Зарегистрируйтесь на [openweathermap.org](https://openweathermap.org/api), скопируйте ключ (активация ~2 часа).

## Возможные проблемы
- **401 Invalid API key**: Проверьте ключ OpenWeatherMap (подтвердите email, подождите активацию).
- **Геолокация не работает**: Убедитесь, что `geopy` установлен; тестируйте на мобильном Telegram.
- **Переводы не применяются**: Проверьте `lang` в URL запроса к API (`&lang=uz` для узбекского).
- **Лимиты**: OpenWeatherMap — 1000 запросов/день (бесплатно). Render — 750 ч/мес.

## Контрибьютинг
1. Форкните репозиторий.
2. Создайте ветку: `git checkout -b feature/awesome-feature`.
3. Коммитьте изменения: `git commit -m 'Add awesome feature'`.
4. Пушьте: `git push origin feature/awesome-feature`.
5. Создайте Pull Request.

## Лицензия
MIT License. См. [LICENSE](LICENSE).

## Авторы
- **Твой ник** — основной разработчик.

## Благодарности
- [aiogram](https://github.com/aiogram/aiogram) — для Telegram API.
- [OpenWeatherMap](https://openweathermap.org/) — для погоды.
- [geopy](https://geopy.readthedocs.io/) — для геокодирования.

---

⭐ Если бот понравился, поставьте звёздочку на GitHub!  
Вопросы? Откройте Issue или напишите в Telegram: https://t.me/sadullaevich_f.  

**Обновлено: 05.10.2025**
