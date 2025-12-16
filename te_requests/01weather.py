import requests

city = input("Enter the city name:")
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    temp = data['current_condition'][0]['temp_C']
    desc = data['current_condition'][0]['weatherDesc'][0]['value']
    print(f"tempreture {city}: {temp}°C - {desc}")
 