from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city= textField.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat=location.latitude)
    print(result)

    home= pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %P")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # weather

    api = "https://api.openweathermap.org/data/2.5/weather?lat="+city+""


    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
#search box

search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)


textField = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040",border=0,  fg="white")
textField.place(x=50, y= 40)
textField.focus()


Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)


#logo

Logo_image = PhotoImage(file="logo.png")
Logo = Label(image= Logo_image)
Logo.place(x=150, y=100)


# bottom box

frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image = frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)


#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y= 130)
 
#label

label = Label(root, text="WIND", font=("helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label.place(x=120, y=400)

labe2 = Label(root, text="HUMIDITY", font=("helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
labe2.place(x=250, y=400)


labe3 = Label(root, text="DESCRIPITION", font=("helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
labe3.place(x=430, y=400)



labe4 = Label(root, text="PRESSURE", font=("helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
labe4.place(x=650, y=400)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c= Label(font=("arial", 15,"bold"))
c.place(x=400, y= 250)

w=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y= 430)

h=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y= 430)


d=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y= 430)


p=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y= 430)

root.mainloop()