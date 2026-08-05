from Weather_Getter import get_weather
from tkinter import *
import customtkinter


#set theme
customtkinter.set_appearance_mode("dark") # dark mode
customtkinter.set_default_color_theme("blue") # blue theme


#root window
root_window = customtkinter.CTk()

root_window.title("🌻Weather")
root_window.geometry("700x500")


def submit():

    if value_entry.get().upper() == "TEMPERATURE" or value_entry.get().upper() == "TEMP":
        stat = get_weather(city_entry.get(), "temperature_2m")
        stat_label.configure(text=f"It is ~{(stat)}°C or ~{int(stat * 1.8 + 32)}°F",
                             fg_color="#FFFFFFA7")


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

value_entry = customtkinter.CTkEntry(root_window,
                                    placeholder_text="Enter the value you want (Temperature).",
                                    height=50,
                                    width=400,
                                    font=("Sans", 18),
                                    corner_radius=25
                                    )
value_entry.pack()

#submit button
submit_button = customtkinter.CTkButton(root_window,
                                        text="Submit",
                                        command=submit,
                                        height=40,
                                        width=300,
                                        font=("Sans", 15),
                                        corner_radius=25)
submit_button.pack(pady=50)


root_window.mainloop()