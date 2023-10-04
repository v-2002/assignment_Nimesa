import requests
import json

URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        return None

def main():
    weather_report = get_weather_data()
    if weather_report is None:
        return

    while True:
        print("\nMenu:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1" or choice == "2" or choice == "3":
            target_datetime = input("Enter the date and time in the 'YYYY-MM-DD HH:MM:SS' format: ")

            if choice == "1":
                for data in weather_report:
                    if data["dt_txt"] == target_datetime:
                        temperature = data["main"]["temp"]
                if temperature is not None:
                    print(f"Temperature is {temperature} K")
                else:
                    print("No data available")
            elif choice == "2":
                for data in weather_report:
                    if data["dt_txt"] == target_datetime:
                        wind_speed = data["wind"]["speed"]
                if wind_speed is not None:
                    print(f"Wind Speed is {wind_speed} m/s")
                else:
                    print("No data available ")
            elif choice == "3":
                for data in weather_report:
                    if data["dt_txt"] == target_datetime:
                        pressure = data["main"]["pressure"]
                if pressure is not None:
                    print(f"Pressure is {pressure} hPa")
                else:
                    print("No data available ")
        else:
            print("Try again.")

if __name__ == "__main__":
    main()
