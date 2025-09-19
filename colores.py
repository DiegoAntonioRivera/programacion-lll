# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x400")

style = ttk.Style(main)
style.theme_use("clam")

# Variable para controlar la selección del radiobutton
radio_button_var = tk.IntVar(value=-1)  # Ninguno seleccionado al inicio

style.configure("radio_button.TRadiobutton", background="#E4E2E2", foreground="#000000")
style.map("radio_button.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

# Radiobuttons
radio_button_0 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Rojo", value=0, style="radio_button.TRadiobutton")
radio_button_0.place(x=315, y=38)

radio_button_1 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Azul", value=1, style="radio_button.TRadiobutton")
radio_button_1.place(x=315, y=57)

radio_button_2 = ttk.Radiobutton(master=main, variable=radio_button_var, text="Verde", value=2, style="radio_button.TRadiobutton")
radio_button_2.place(x=315, y=77)

# Función para cambiar color de fondo
def cambiar_color():
    opcion = radio_button_var.get()
    if opcion == 0:
        main.config(bg="olive")
    elif opcion == 1:
        main.config(bg="blue")
    elif opcion == 2:
        main.config(bg="green")
    else:
        main.config(bg="#E4E2E2")  # color por defecto si no selecciona nada

# Función para salir
def salir():
    main.destroy()

# Botón cambiar
style.configure("button.TButton", background="#E4E2E2", foreground="#000", cursor="dotbox")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Cambiar", style="button.TButton", command=cambiar_color)
button.place(x=317, y=159, width=80, height=40)

# Botón salir
style.configure("button1.TButton", background="#E4E2E2", foreground="#000", cursor="dotbox")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="Salir", style="button1.TButton", command=salir)
button1.place(x=322, y=225, width=80, height=40)

main.mainloop()
