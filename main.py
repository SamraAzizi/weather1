from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezonrFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


#search box

search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)


textField = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040",border=0,  fg="white")
textField.place(x=50, y= 40)
textField.focus()


Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image)

root.mainloop()