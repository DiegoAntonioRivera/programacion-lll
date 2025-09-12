import tkinter as tk
from tkinter import ttk, messagebox

def calcular_promedio():
    try:
        lab1 = float(entry_lab1.get())
        lab2 = float(entry_lab2.get())
        parcial = float(entry_parcial.get())

        if not (0 <= lab1 <= 10 and 0 <= lab2 <= 10 and 0 <= parcial <= 10):
            messagebox.showerror("Error", "Las notas deben estar entre 0 y 10")
            return

        promedio = (lab1 * 0.30) + (lab2 * 0.30) + (parcial * 0.40)
        messagebox.showinfo("Resultado", f"Tu promedio es: {promedio:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

ventana = tk.Tk()
ventana.title("Promedio Cómputo 1")
ventana.geometry("400x200")
ventana.configure(bg="#f7f7f7")

frame = ttk.Frame(ventana, padding="20 20 20 20")
frame.pack(expand=True)

ttk.Label(frame, text="Nota Lab 1 (30%):").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_lab1 = ttk.Entry(frame, width=15)
entry_lab1.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Nota Lab 2 (30%):").grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_lab2 = ttk.Entry(frame, width=15)
entry_lab2.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Nota Parcial (40%):").grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_parcial = ttk.Entry(frame, width=15)
entry_parcial.grid(row=3, column=1, pady=5)

btn_calcular = ttk.Button(frame, text="Calcular Promedio", command=calcular_promedio)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=15)

ventana.mainloop()
