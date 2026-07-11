import requests
city = input("enter a city")

url = f"https://wttr.in/{city}?format=j1"
response =requests.get(url)
data = response.json()
temp=data["current_condition"][0]["temp_C"]
humidity = data["current_condition"][0]["humidity"]
pre = data["current_condition"][0]["pressure"]
hour = data["weather"][0]["hourly"]

for hour in hour:
    print(
        f"Time:{hour['time']} | "
        f"temp:{hour['tempC']}C | "
        f"Humidity:{hour['humidity']}% | "
        f"Weather :{hour['weatherDesc'][0]['value']}"
    )


print("Presuure",pre)
print("Humidity",humidity)
print("Temperature:",temp,"C")