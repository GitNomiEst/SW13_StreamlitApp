import streamlit as st
import requests
import pandas as pd
import datetime

API_KEY = 'bfd59cda378f3132f08aebf94451e03b'

# Funktion zum Laden der Wetterdaten
@st.cache_data
def load_weather_data(city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt={days*8}&appid={API_KEY}"
    response = requests.get(url)
    
    # Überprüfung auf Fehler in der API-Antwort
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    # Extrahieren der relevanten Daten
    dates = [datetime.datetime.fromtimestamp(entry['dt']) for entry in data['list']]
    temperatures = [entry['main']['temp'] for entry in data['list']]
    humidity = [entry['main']['humidity'] for entry in data['list']]
    wind_speed = [entry['wind']['speed'] for entry in data['list']]
    
    # Erstellen eines DataFrame
    weather_data = pd.DataFrame({
        'Date': dates,
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidity,
        'Wind Speed (m/s)': wind_speed
    })
    return weather_data

# Titel der App
st.title("Wettervisualisierungs-App")

# Stadt- und Zeitraum-Auswahl
city = st.text_input("Geben Sie eine Stadt ein", "Berlin")
days = st.slider("Wählen Sie die Anzahl der Tage", 1, 5, 3)

# Laden der Daten
if st.button("Daten laden"):
    weather_data = load_weather_data(city, days)
    
    # Überprüfung, ob die Daten erfolgreich geladen wurden
    if weather_data is not None:
        # Datenanzeige
        st.write(f"Wettervorhersage für {city} für die nächsten {days} Tage")

        # Tabellenanzeige
        st.write(weather_data)

        # Temperatur-Diagramm
        st.subheader("Temperature")
        st.line_chart(weather_data.set_index('Date')[['Temperature (°C)']])

        # Luftfeuchtigkeit-Diagramm
        st.subheader("Humidity")
        st.line_chart(weather_data.set_index('Date')[['Humidity (%)']])

        # Windgeschwindigkeit-Diagramm
        st.subheader("Wind Speed")
        st.line_chart(weather_data.set_index('Date')[['Wind Speed (m/s)']])
    else:
        st.error(f"Fehler beim Laden der Daten für {city}. Bitte überprüfen Sie die Stadtname und versuchen Sie es erneut.")