import tkinter
import customtkinter

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")


def button_click():
    print("button click")
    label = customtkinter.CTkLabel(app, text="CTkLabel",text_color='red')
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(app, text="Click Me",command=button_click, corner_radius=64,
                                 fg_color="#8158D0", hover_color="#4158D0")
button.grid(row=5, column=5, padx=20, pady=10)

    # add methods to app

app.mainloop()



