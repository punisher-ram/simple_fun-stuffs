#import the dependency's - pip install tkinter and pip install geocoder.
#this program displays your current location using geocoder.
import tkinter as tk
import geocoder

# Function to fetch and display your current location
def show_my_location():
    location = geocoder.ip('me')
    
    if location:
        latitude = location.latlng[0]
        longitude = location.latlng[1]
        address = location.address

        result_label.config(text=f"Your Current Location:\nLatitude: {latitude}\nLongitude: {longitude}\nAddress: {address}")
    else:
        result_label.config(text="Unable to fetch your location.")

# Create the main window
root = tk.Tk()
root.title("My Location App")

# Create labels, buttons, and result display
title_label = tk.Label(root, text="Click 'My Location' to Fetch Your Current Location", font=("Arial", 14))
title_label.pack()

location_button = tk.Button(root, text="My Location", command=show_my_location, font=("Arial", 12))
location_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
result_label.pack()

# Start the GUI main loop
root.mainloop()
