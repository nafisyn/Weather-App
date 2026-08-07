from Weather_Getter import get_weather
from tkinter import *
import customtkinter


#set theme
customtkinter.set_appearance_mode("dark") # dark mode
customtkinter.set_default_color_theme("blue") # blue theme


#root window
root_window = customtkinter.CTk()

root_window.title("🌻Weather")
root_window.geometry("700x600")


def submit():

    if value.get() == "TEMPERATURE":
        stat = get_weather(city_entry.get(), "temperature_2m")
        
        if stat != None:
            stat_label.configure(text=f"It is ~{(stat)}°C or ~{int(stat * 1.8 + 32)}°F")

    elif value.get() == "WIND SPEED":
            stat = get_weather(city_entry.get(), "wind_speed_10m")

            if stat != None:
                stat_label.configure(text=f"Wind Speed is {stat} km/h")

    elif value.get() == "HUMIDITY":
            stat = get_weather(city_entry.get(), "relative_humidity_2m")

            if stat != None:
                stat_label.configure(text=f"Relative Humidity is {stat}%")

    if stat == None:
         stat_label.configure(text="No city/value named as so.")  


#stats
stat_label = customtkinter.CTkLabel(root_window,
                                     text="",
                                     font=("Sans", 24),
                                     fg_color="#48494b",
                                     width=500,
                                     height=50,
                                     corner_radius=50
                                     )
stat_label.pack(pady=55)

#entry box
city_entry = customtkinter.CTkEntry(root_window,
                                    placeholder_text="Enter the city name.",
                                    height=50,
                                    width=400,
                                    font=("Sans", 18),
                                    corner_radius=25
                                    )
city_entry.pack()

value = StringVar(value="TEMPERATURE")

temperature_picker = customtkinter.CTkRadioButton(root_window,
                                                  text="Temperature",
                                                  variable=value,
                                                  value="TEMPERATURE")
temperature_picker.pack(pady=20)

wind_speed_picker = customtkinter.CTkRadioButton(root_window,
                                                  text="Wind Speed",
                                                  variable=value,
                                                  value="WIND SPEED")
wind_speed_picker.pack(pady=20)

humidity_picker = customtkinter.CTkRadioButton(root_window,
                                                  text="Humidity",
                                                  variable=value,
                                                  value="HUMIDITY")
humidity_picker.pack(pady=20)



#submit button
submit_button = customtkinter.CTkButton(root_window,
                                        text="Submit",
                                        command=submit,
                                        height=40,
                                        width=300,
                                        font=("Sans", 15),
                                        corner_radius=25)
submit_button.pack(pady=30)


root_window.mainloop()
