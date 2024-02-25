import tkinter
import customtkinter
from customtkinter import *


app =CTk()
app.geometry("600x500")
app.title("CTk example")


def button_click():
    print("button click")
    label = customtkinter.CTkLabel(app, text="CTkLabel",text_color='red')
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(app, command=button_click)
button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app

app.mainloop()



