from tkinter import *

from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox,Entry
from numpy import obj2sctype
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests 
import pytz
########################



root = Tk()
root.title("WeatherCast")
root.geometry("1000x700+300+200")
root.resizable(False,False)
root.configure(bg="White")


def getWeather():
  try:
    city=textfield.get()
    geolocator = Nominatim(user_agent="Komal-Bhau-GeoApp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude









    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)  
    home=pytz.timezone(result)
    loacal_time=datetime.now(home)
    current_time=loacal_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT TIME")
  
    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6b5b7c5709273e8c42917bb326a1814e"

    json_data=requests.get(api).json()
    condition= json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
  
    t.config(text=(temp,"°C"))
    
  
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
  
  except Exception as e:
    messagebox.showerror("Invalid Entry")







#search box

Search_field = PhotoImage(file="C:/Users/bansa/OneDrive/Desktop/search field.png")
search_image = Label(image=Search_field,border=0)
search_image.place(x=100,y=36)



textfield=Entry(root,justify="center",width=40,font=("italic",16,"bold"),bg="#218D6A",fg="#FFFDD0",border=0)
textfield.place(x=180,y=55)
textfield.focus()

Search_icon = PhotoImage(file="C:/Users/bansa/OneDrive/Desktop/search icon.png",height=33,width=33)
my_image = Button(image=Search_icon,border=0,cursor="cross",borderwidth=0,bg="#218D6A",command=getWeather)
my_image.place(x=630,y=48)

#logo
Logo_image=PhotoImage(file="C:/Users/bansa/OneDrive/Desktop/My first design.png",height=400,width=400)
logo = Label(border=0,image=Logo_image)
logo.place(bordermode='ignore',x=180,y=100)

#bottom
frame_image=PhotoImage(file="C:/Users/bansa/OneDrive/Desktop/bottom.png")
frame=Label(image=frame_image,border=0)
frame.pack(padx=30,pady=30,side="bottom")

#time
name=Label(root,font=("Georgia",15,"bold"),fg="black",bg="white")
name.place(x=50,y=130)
clock=Label(root,font=("Comfortaa",15),fg="black",bg="white")
clock.place(x=50,y=170)


#labels
label1=Label(root,text="WIND",font=("italic",14,"bold"),fg="white",bg="#022F6D")
label1.place(x=100,y=572)

label2=Label(root,text="HUMIDITY",font=("italic",14,"bold"),fg="white",bg="#022F6D")
label2.place(x=270,y=572)

label3=Label(root,text="DESCRIPTION",font=("italic",14,"bold"),fg="white",bg="#022F6D")
label3.place(x=500,y=572)

label4=Label(root,text="PRESSURE",font=("italic",14,"bold"),fg="white",bg="#022F6D")
label4.place(x=730,y=572)

#temperature

t=Label(font=("Lexend",50,"bold"),fg="#151B8D",bg="white")
t.place(x=600,y=150)
c=Label(text="~Let your smile be the sunshine that brightens even the stormiest days~",wraplength=310,font=("Impact",25,"bold"),fg="#5CB3FF",bg="white")
c.place(x=600,y=220)

w=Label(text=".....",font=("arial",15,"bold"),bg="#022F6D",fg="white")
w.place(x=100,y=615)

h=Label(text=".....",font=("arial",15,"bold"),bg="#022F6D",fg="white")
h.place(x=270,y=615)

d=Label(text=".....",font=("arial",15,"bold"),bg="#022F6D",fg="white")
d.place(x=500,y=615)

p=Label(text=".....",font=("arial",15,"bold"),bg="#022F6D",fg="white")
p.place(x=730,y=615)


root.mainloop()
