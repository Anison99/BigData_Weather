import sqlite3
import matplotlib.pyplot as plt

# Łączenie z bazą danych
conn = sqlite3.connect('dane_pogodowe.db')
c = conn.cursor()

# Pobieranie danych z bazy danych
c.execute("SELECT data, temperatura, wilgotnosc FROM pogoda_tarnow")

dates = []
temperatures = []
humidities = []

# Przetwarzanie wyników zapytania
for row in c.fetchall():
    dates.append(row[0])
    temperatures.append(row[1])
    humidities.append(row[2])

# Zamykanie połączenia z bazą danych
conn.close()

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, 'o-', label='Temperatura (°C)')
plt.plot(dates, humidities, 'o-', label='Wilgotność (%)')
plt.xlabel('Data')
plt.ylabel('Wartość')
plt.title('Wykres pogodowy na najbliższe 5 dni - Tarnów')
plt.xticks(rotation=45)
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()
