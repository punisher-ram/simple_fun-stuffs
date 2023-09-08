#import the dependency's - pip install tkinter 
#pip install request
import tkinter as tk
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f'{base_url}q={city}&appid={api_key}&units=metric'
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]
        
        result_label.config(text=f'Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}')
    else:
        result_label.config(text='City not found')

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create labels and entry fields
city_label = tk.Label(root, text="Enter the City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

# Start the GUI main loop
root.mainloop()
