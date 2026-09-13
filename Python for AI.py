import requests
def Weather_checker(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data["current"]["temperature_2m"]


latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")
edmonton_weather = Weather_checker(latitude, longitude)
print(edmonton_weather)