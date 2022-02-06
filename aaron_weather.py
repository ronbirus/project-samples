#Import everything I need
import tkinter as tk
from tkinter import ttk
import requests
import json
api_key = "dc7feb2f03a75529fbe7331f22c3db37"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
#city = "toronto"
#url = f'{base_url}q={city}&appid={api_key}'

#Weather Function
def calculate_weather():
    city = citytext.get() # changed
    api_key = "dc7feb2f03a75529fbe7331f22c3db37"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = f'{base_url}q={city}&appid={api_key}'
    weather_data = requests.get(url)
    if weather_data.status_code == 200:
        #get temp
        data = weather_data.json()
        tempk = data.get('main')['temp']
        tempc = tempk - 273.15
        #get feels like
        feelikelv = data.get('main')['feels_like']
        feel = feelikelv - 273.15
        #get summary
        summary = data.get('weather')[0]['description']
        #get wind speed
        windspeed = data.get('wind')['speed']
        #get wind gusts
        windgusts = data.get('wind')['gust']

        currenttempdisp.set(f'{tempc}')
        feelslikedisp.set(f'{feel}')
        summarydisp.set(f'{summary}')
        windspeeddisp.set(f'{windspeed}')
        windgustsdisp.set(f'{windgusts}')


#GUI Design
#Create the root window
root = tk.Tk()
root.title('Weather App')
root.geometry('300x200')

#Create the main frame
#Frame is a child of root
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

#Title
ttk.Label(frame_home, text = "              ").grid(column=0, row=0)
ttk.Label(frame_home, text = "              ").grid(column=2, row=0)
ttk.Label(frame_home, text = "Weather App").grid(column=1, row=0)

#Menu WIP template
#Entry field
ttk.Label(frame_home, text = "Enter city:").grid(column=0, row=1)
citytext = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=citytext).grid(column=1,row=1)
ttk.Button(frame_home, width=30, text='Submit', command = calculate_weather).grid(column=1,row=2,)
#Current Temp
ttk.Label(frame_home, text = "Current Temp:").grid(column=0, row=3)
currenttempdisp= tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=currenttempdisp).grid(column=1,row=3)
#Feels Like
ttk.Label(frame_home, text = "Feels Like:").grid(column=0, row=4)
feelslikedisp= tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=feelslikedisp).grid(column=1,row=4)
#Summary
ttk.Label(frame_home, text = "Summary:").grid(column=0, row=5)
summarydisp= tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=summarydisp).grid(column=1,row=5)
#Wind Speed
ttk.Label(frame_home, text = "Wind Speed:").grid(column=0, row=6)
windspeeddisp= tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=windspeeddisp).grid(column=1,row=6)
#Wind Gusts
ttk.Label(frame_home, text = "Wind Gusts:").grid(column=0, row=7)
windgustsdisp= tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=windgustsdisp).grid(column=1,row=7)






#Put this in to make it work
root.mainloop()
