import requests
import time

API_KEY = 'd6c98de467c64de5a1050158240301'

favorite_cities = []  # list for favorite cities

def get_weather(city):
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['current']['condition']['text']}, "
              f"Temperature: {data['current']['temp_c']}°C")
    else:
        print(f"Failed to fetch weather for {city}")

def add_favorite(city):
    favorite_cities.append(city)
    print(f"Added {city} to favorites.")
    for city in favorite_cities:
        print(city)


def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"Removed {city} from favorites.")
    else:
        print(f"{city} is not in favorites.")

def update_favorite(old_city, new_city):
    if old_city in favorite_cities:
        index = favorite_cities.index(old_city)
        favorite_cities[index] = new_city
        print(f"Updated {old_city} to {new_city} in favorites.")
    else:
        print(f"{old_city} is not in favorites.")

def list_favorites():
    if favorite_cities:
        print("Favorite Cities:")
        for city in favorite_cities:
            print(city)
    else:
        print("No favorite cities added yet.")

if __name__ == '__main__':
    while True:
        print("OPTIONS")
        print("1.Check weather by city name")
        print("2.Add a favourite city")
        print("3.Remove a favourite city")
        print("4.List favourite cities")
        print("5.Auto refresh weather")
        print("6.Exit")
        choice=int(input("Enter your choice:"))
        if choice== 1:
            city=input("Enter city name")
            get_weather(city)
        elif choice==2:
            city=input("Enter a city name to be added in favorites")
            add_favorite(city)
        elif choice==3:
            city=input("Enter a city name to be removed from favorites")
            remove_favorite(city)
        elif choice==4:
            list_favorites()
        elif choice==5:
            city=input("Enter a city name to check the auto refreshed weather")
            while True:
                get_weather(city)  #refresh
                time.sleep(15)  # Simulating 15 seconds delay
        elif choice==6:
            break
        else:
            print("Invalid input")
