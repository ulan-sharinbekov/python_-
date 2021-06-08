import requests, json
from tkinter import *

def getWeather():
    KEY = '186a2ae6b4e4a7465105495e3430df15'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    city = inp1.get()
    params = {
        'q': city,
        'appid': KEY,
        'units': 'metric',
    }
    data = requests.get(URL, params=params)
    lbl_temp_value.config(text = data.json()["main"]["temp"])
    lbl_city_value.config(text = city)
    print(data.json())

window = Tk()
window.geometry("400x400")

inp1 = Entry(window)
inp1.grid(row=0, column=0)

lbl_city = Label(window, text="city")
lbl_city.grid(row=1, column=0)

lbl_city_value = Label(window, text="City name")
lbl_city_value.grid(row=1, column=1)


lbl_temp = Label(window, text="temp")
lbl_temp.grid(row=2, column=0)

lbl_temp_value = Label(window, text="temp value")
lbl_temp_value.grid(row=2, column=1)

btn = Button(window, text="click", command=getWeather)
btn.grid(row=0, column=2)

window.mainloop()
