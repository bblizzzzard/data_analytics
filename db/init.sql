-- Таблица погодных данных
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    city VARCHAR(50) NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    pressure REAL NOT NULL,
    wind_speed REAL NOT NULL
);

--Индексы для ускорения выборок
--Индексирует по дню
CREATE INDEX IF NOT EXISTS idx_weather_timestamp ON weather(timestamp);

--Индексирует по городу
CREATE INDEX IF NOT EXISTS idx_weather_city ON weather(city);

--Индексирует по температуре
CREATE INDEX IF NOT EXISTS idx_weather_temperature ON weather(temperature);

--Индексирует по влажности
CREATE INDEX IF NOT EXISTS idx_weather_humidity ON weather(humidity);

--Индексирует по давлению
CREATE INDEX IF NOT EXISTS idx_weather_pressure ON weather(pressure);
--Индексирует по скорости ветра
CREATE INDEX IF NOT EXISTS idx_weather_wind_speed ON weather(wind_speed);