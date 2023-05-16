import requests

def get_weather_data():
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=a17a960f9fcd4f071a2bf3bd5bd570b0'

    # Tworzenie żądania HTTP GET do API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Pobranie odpowiedzi w formacie JSON
        return data
    else:
        print('Błąd podczas pobierania danych:', response.status_code)
        return None

# Wywołanie funkcji i pobranie danych
weather_data = get_weather_data()

if weather_data is not None:
    # Przetwarzanie i zapis danych
    # Tutaj możesz zapisać dane do bazy danych lub przekształcić je do innej struktury danych
    # Na przykład, jeśli API zwraca dane w postaci listy, możesz iterować po nich i zapisywać do bazy danych

    # Przykład wyświetlenia pobranych danych
    print(weather_data)
