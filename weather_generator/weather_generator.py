import os
import time
import random
import psycopg2
from datetime import datetime, timedelta

#Достаём данные из .env
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#Подключение к бд
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

# Диапазоны погодных параметров для каждого города зимой
cities = {
    "Москва": {
        "temperature": (-15, 0),
        "humidity": (30, 90),
        "pressure": (980, 1040),
        "wind_speed": (0, 10)
    },
    "Владивосток": {
        "temperature": (-20, 5),
        "humidity": (40, 95),
        "pressure": (990, 1030),
        "wind_speed": (6, 25)
    },
    "Санкт-Петербург": {
        "temperature": (-25, 4),
        "humidity": (50, 100),
        "pressure": (970, 1035),
        "wind_speed": (0, 12)
    },
    "Хабаровск": {
        "temperature": (-30, -2),
        "humidity": (25, 85),
        "pressure": (975, 1045),
        "wind_speed": (5, 14)
    }
}

# Начальная дата
start_date = datetime(2026, 1, 1, 12, 0)  # фиксированное время 12:00
current_date = start_date

def generate_weather_data_for_day():
    #Генерирует случайные данные
    global current_date

    city = random.choice(list(cities.keys()))
    ranges = cities[city]

    temperature = random.randint(*ranges["temperature"])
    humidity = round(random.uniform(*ranges["humidity"]), 1)
    pressure = round(random.uniform(*ranges["pressure"]), 1)
    wind_speed = round(random.uniform(*ranges["wind_speed"]), 1)

    timestamp = current_date
    current_date += timedelta(days=1)  # каждый день +1
    return timestamp, city, temperature, humidity, pressure, wind_speed

try:
    while True:
        timestamp, city, temperature, humidity, pressure, wind_speed = generate_weather_data_for_day()
        cursor.execute(
            """
            INSERT INTO weather (timestamp, city, temperature, humidity, pressure, wind_speed)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (timestamp, city, temperature, humidity, pressure, wind_speed)
        )
        conn.commit()
        time.sleep(1)

except Exception as e:
    pass
finally:
    cursor.close()
    conn.close()