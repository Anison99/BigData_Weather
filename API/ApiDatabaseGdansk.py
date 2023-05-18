import sqlite3
import requests
from datetime import datetime, timedelta

# Tworzenie lub łączenie z bazą danych
conn = sqlite3.connect('dane_pogodowe.db')
c = conn.cursor()

# Tworzenie tabeli w bazie danych, jeśli nie istnieje
c.execute('''CREATE TABLE IF NOT EXISTS pogoda_gdansk
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              data TEXT,
              temperatura REAL,
              wilgotnosc INTEGER,
              opis TEXT)''')

# Pobieranie danych pogodowych dla kolejnych 5 dni
api_key = 'a17a960f9fcd4f071a2bf3bd5bd570b0'
city = 'Gdańsk'

# Pobieranie prognozy pogody dla kolejnych 5 dni
url = f'http://api.openweathermap.org/data/2.5/forecast?q=Gdansk,pl&exclude=current,minutely,hourly,alerts&units=metric&appid={api_key}'
response = requests.get(url)
data_api = response.json()

daily_forecast = data_api['list']

# Obecna data
current_date = datetime.now().date()

for i in range(5):
    # Obliczanie daty dla danego dnia
    date = (current_date + timedelta(days=i)).strftime('%Y-%m-%d')

    # Pobieranie danych pogodowych dla danego dnia
    temperatura = daily_forecast[i]['main']['temp']
    wilgotnosc = daily_forecast[i]['main']['humidity']
    opis = daily_forecast[i]['weather'][0]['description']

    # Wstawianie danych do bazy danych
    c.execute("INSERT INTO pogoda_gdansk (data, temperatura, wilgotnosc, opis) VALUES (?, ?, ?, ?)",
              (date, temperatura, wilgotnosc, opis))

# Zapisywanie zmian i zamykanie bazy danych
conn.commit()
conn.close()
