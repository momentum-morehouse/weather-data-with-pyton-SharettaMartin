import requests
#In this project, you will use the Python requests library to obtain weather data for different locations.

# You will store that data as instances of a class and then use matplotlib to generate a bar chart of temperatures.
#Determine how to make a request,make a function that iterate over the locations

#Sample taken from class uses my personal key from my Climacell
#Makes a weather request in real time

locations = [("Grand Canyon Nat'l Park", 36.30785475, -112.292896),("Yosemite Nat'l Park",	37.84054795, -119.5165878),("Yellowstone Nat'l Park", 44.6200885, -110.5607575),("Rocky Mountain Nat'l Park", 40.35594255, -105.7176855),("Big Bend Nat\'l Park", 29.33341, -103.1940004),("Eifel Tower",	48.8587307,	2.2944894),("Empire State Building", 40.7484284, -73.98565462),("French Quarter", 29.9595056, -90.0655668),("Mount Rushmore", 43.88086685, -103.4538231),("Arrowhead Stadium", 39.04894045, -94.4830034)]

def get_weather_data (lat,lon):

    url = "https://api.climacell.co/v3/weather/realtime"

payload = {
  "apikey": "DRshkcC8L2AUGpntarjn5LeF9RtKv7DS", 
  "lat":18.476223, 
  "lon": -77.893890, 
  "unit_system":"us",
  "fields": ["temp", "precipitation", "wind_gust",]
  ,}
#Explain line below...
  response = requests.get(url, params=payload).json()
    print(response)
    # print(response["temp"] ["value"])


get_weather_data(lat, lon)

#Create a list of tuples for the LATsand LONGs


#Need a func that will get  
#def get_weatherdata(locations):
# pass

#Need a loop to get attributes of every item in the list
for location in locations:
  weather(location[1],location[2])

print(locations)