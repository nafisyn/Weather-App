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

            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

            ).json()


        return weather_data["current"][f"{value}"]

    except KeyError:
        pass


if __name__ == "__main__":
    while running:
        temperature = get_weather(input("Input City: "), "temperature")

        if temperature != None:
            print(temperature)

        else:
            print("No city/value named as so.")

        if input("Another city?(y/n):    ").upper() == "N":
            break