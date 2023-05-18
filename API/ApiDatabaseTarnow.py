import sqlite3
import requests
from datetime import datetime, timedelta

# Tworzenie lub łączenie z bazą danych
conn = sqlite3.connect('dane_pogodowe.db')
c = conn.cursor()

# Tworzenie tabeli w bazie danych, jeśli nie istnieje
c.execute('''CREATE TABLE IF NOT EXISTS pogoda_tarnow
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              data TEXT,
              temperatura REAL,
              wilgotnosc INTEGER,
              opis TEXT)''')

# Pobieranie danych pogodowych dla najbliższych 5 dni co 3 godziny
api_key = 'a17a960f9fcd4f071a2bf3bd5bd570b0'
city = 'Tarnów'

# Pobieranie prognozy pogody dla najbliższych 5 dni co 3 godziny
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}'
response = requests.get(url)
data_api = response.json()

hourly_forecast = data_api['list']

for i in range(5):
    # Obliczanie daty początkowej dla danego dnia
    start_date = (datetime.now() + timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)

    for j in range(8):
        # Obliczanie daty dla danego punktu czasowego
        date = (start_date + timedelta(hours=(j * 3))).strftime('%Y-%m-%d %H:%M:%S')

        # Pobieranie danych pogodowych dla danego punktu czasowego
        temperatura = hourly_forecast[(i * 8) + j]['main']['temp']
        wilgotnosc = hourly_forecast[(i * 8) + j]['main']['humidity']
        opis = hourly_forecast[(i * 8) + j]['weather'][0]['description']

        # Wstawianie danych do bazy danych
        c.execute("INSERT INTO pogoda_tarnow (data, temperatura, wilgotnosc, opis) VALUES (?, ?, ?, ?)",
                  (date, temperatura, wilgotnosc, opis))

# Zapisywanie zmian i zamykanie bazy danych
conn.commit()
conn.close()
