import requests

def get_weather(city: str, api_key: str):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        print(f"Current temperature in {city}: {temp}°C")
        print(f"Weather condition: {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    API_KEY = "77c78eb3dddab8df680ad3553101c3e3"
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
