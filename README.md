ObHavo+ - Telegram Weather Bot




Описание
ObHavo+ — это мультиязычный Telegram-бот для получения прогноза погоды на 5 дней. Бот поддерживает русский, английский и узбекский языки, отображение эмодзи для погодных условий и определение города по геолокации (используя Nominatim).
Прогноз берётся из OpenWeatherMap API. Бот использует aiogram для асинхронной обработки сообщений и geopy для обратного геокодирования координат.
Основные фичи

Выбор языка: 🇷🇺 Русский, 🇬🇧 English, 🇺🇿 O‘zbek.
Прогноз по городу: Введите название (например, "Tashkent").
Геолокация: Поделитесь местоположением — бот определит город автоматически.
Переводы: Полный интерфейс на выбранном языке (включая "температура" → "harorat" / "temperature").
Эмодзи: ☀️ Ясно, ☁️ Пасмурно, 🌧️ Дождь и т.д.
Обработка ошибок: Дружественные сообщения при неверном городе или проблемах с API.

Демо

Отправьте /start боту.
Выберите язык (🇺🇿 O‘zbek).
Поделитесь геолокацией или введите "Tashkent".
Получите прогноз:
textOb-havo prognozi uchun <b>Toshkent</b>:
05.10.2025: Bulutli ☁️, harorat: 21.64°C
06.10.2025: Ochiq osmon ☀️, harorat: 21.46°C
...


Требования

Python 3.8+.
Telegram Bot Token (от @BotFather).
API Key от OpenWeatherMap (бесплатно до 1000 запросов/день).

Установка

Клонируйте репозиторий:
textgit clone https://github.com/твой_логин/WeatherBOT.git
cd WeatherBOT

Создайте виртуальное окружение:
textpython -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

Установите зависимости:
textpip install -r requirements.txt

Настройте .env:
Создайте файл .env в корне:
textBOT_TOKEN=your_telegram_bot_token_here
WEATHER_API_KEY=your_openweather_api_key_here

Запустите бота:
textpython bot.py


Структура проекта
textWeatherBOT/
├── bot.py              # Основной код бота (aiogram, обработчики)
├── weather.py          # Функции для API погоды и агрегации прогноза
├── requirements.txt    # Зависимости
├── Procfile           # Для деплоя (Render/Railway)
├── .gitignore         # Игнор файлов
└── .env               # Переменные (не коммитьте!)
Деплой
Render.com (рекомендуется, бесплатно до 750 ч/мес)

Запушьте на GitHub (см. ниже).
На render.com: "New +" → "Background Worker" → Подключите GitHub-репозиторий.
Build: pip install -r requirements.txt.
Start: python bot.py.
Environment Variables: Добавьте BOT_TOKEN и WEATHER_API_KEY.
Deploy!

GitHub

Создайте репозиторий на github.com.
В папке проекта:
textgit init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/твой_логин/WeatherBOT.git
git push -u origin main


API и ключи

Telegram Bot Token: Получите у @BotFather командой /newbot.
OpenWeatherMap API: Зарегистрируйтесь на openweathermap.org, скопируйте ключ из профиля (активация ~2 часа).

Возможные проблемы

401 Invalid API key: Проверьте ключ OpenWeatherMap (подтвердите email, подождите активацию).
Геолокация не работает: Убедитесь, что geopy установлен; тестируйте на мобильном Telegram.
Переводы не применяются: Проверьте lang в URL запроса к API (&lang=uz для узбекского).
Лимиты: OpenWeatherMap — 1000 запросов/день (бесплатно). Render — 750 ч/мес.

Контрибьютинг

Форкните репозиторий.
Создайте ветку: git checkout -b feature/awesome-feature.
Коммитьте изменения: git commit -m 'Add awesome feature'.
Пушьте: git push origin feature/awesome-feature.
Создайте Pull Request.

Лицензия
MIT License. См. LICENSE.
Авторы

Твой ник — основной разработчик.

Благодарности

aiogram — для Telegram API.
OpenWeatherMap — для погоды.
geopy — для геокодирования.


⭐ Если бот понравился, поставьте звёздочку на GitHub!
Вопросы? Откройте Issue или напишите в Telegram: @sadullaevich_f.
Обновлено: 05.10.2025
