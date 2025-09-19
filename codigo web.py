# This code is generated using PyUIbuilder: https://pyuibuilder.com
import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crear ventana
ventana1 = tk.Tk()
ventana1.title("Controles TTK")
ventana1.config(bg="#E4E2E2")
ventana1.geometry("700x400")

# Variable para el valor mostrado en el Label
valor = tk.IntVar(value=0)

# Estilos
style = ttk.Style(ventana1)
style.theme_use("clam")

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

style.configure("label.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 14))

# Funciones
def aumentar():
    valor.set(valor.get() + 1)

def disminuir():
    valor.set(valor.get() - 1)

def salir():
    ventana1.destroy()

# Widgets
button = ttk.Button(master=ventana1, text="Aumentar", style="button.TButton", command=aumentar)
button.place(x=288, y=115, width=100, height=40)

button1 = ttk.Button(master=ventana1, text="Disminuir", style="button1.TButton", command=disminuir)
button1.place(x=288, y=181, width=100, height=40)

button2 = ttk.Button(master=ventana1, text="Salir", style="button2.TButton", command=salir)
button2.place(x=288, y=248, width=100, height=40)

label = ttk.Label(master=ventana1, textvariable=valor, style="label.TLabel", anchor="center")
label.place(x=284, y=35, width=100, height=40)

ventana1.mainloop()
