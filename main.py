import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    api_key = '98add7df2ad65be49a201606748427f8'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    country = weather['sys']['country']

    icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
    return (icon_url, temperature, description, city, country)

def search():
    result = get_weather(city_entry.get())
    if result is None:
        return

    icon_url, temperature, description, city, country = result

    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

# GUI Setup
root = tk.Tk()
root.title('Weather App')
root.geometry('400x400')


frame = ttk.Frame(root)
frame.pack(expand=True, fill='both')

city_entry = ttk.Entry(frame, font=('Arial', 14))
city_entry.pack(pady=10, padx=10, fill='x')

search_button = ttk.Button(frame, text='Search', command=search)
search_button.pack(pady=5)

location_label = ttk.Label(frame, font=('Arial', 14))
location_label.pack(pady=5)

icon_label = ttk.Label(frame)
icon_label.pack(pady=5)

temperature_label = ttk.Label(frame, font=('Arial', 14))
temperature_label.pack(pady=5)

description_label = ttk.Label(frame, font=('Arial', 14))
description_label.pack(pady=5)

root.mainloop()
