import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

def calcular_edad():
    try:
        anio = int(entry_anio.get())
        mes = int(entry_mes.get())
        dia = int(entry_dia.get())

        hoy = date.today()
        nacimiento = date(anio, mes, dia)
        edad = hoy.year - nacimiento.year

        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        messagebox.showinfo("Resultado", f"Tienes {edad} años.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("400x250")
ventana.configure(bg="#f0f0f0")

frame = ttk.Frame(ventana, padding="20 20 20 20")
frame.pack(expand=True)

ttk.Label(frame, text="Año de nacimiento:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_anio = ttk.Entry(frame, width=15)
entry_anio.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Mes de nacimiento:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_mes = ttk.Entry(frame, width=15)
entry_mes.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Día de nacimiento:").grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_dia = ttk.Entry(frame, width=15)
entry_dia.grid(row=3, column=1, pady=5)

btn_calcular = ttk.Button(frame, text="Calcular Edad", command=calcular_edad)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=15)

ventana.mainloop()
