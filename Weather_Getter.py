import requests


running = True


def get_weather(city, value):
    
    try:
        location_data = requests.get(

            f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
            
            ).json()


        results = location_data["results"]
        longitude = results[0]["longitude"]
        latitude = results[0]["latitude"]

        weather_data = requests.get(

            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly={value}&timezone=auto",
            timeout=10

            ).json()


        return weather_data["hourly"][f"{value}"][0]

    except KeyError:
        return None


if __name__ == "__main__":
    while running:
        temperature = get_weather(input("Input City: ").strip(), "temperature")

        if temperature != None:
            print(temperature)

        else:
            print("No city/value named as so.")

        if input("Another city?(y/n):    ").upper() == "N":
            break