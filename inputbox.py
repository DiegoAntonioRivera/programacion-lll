import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.formulario01 = tk.Tk()
        self.formulario01.title('Suma y Resta')

        self.label01 = tk.Label(self.formulario01, text='Ingrese el primer número:')
        self.label01.grid(column=0, row=0, padx=5, pady=5)

        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable=self.dato01)
        self.entry01.grid(column=1, row=0, padx=5, pady=5)

        self.label02 = tk.Label(self.formulario01, text='Ingrese el segundo número:')
        self.label02.grid(column=0, row=1, padx=5, pady=5)

        self.dato02 = tk.StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.grid(column=1, row=1, padx=5, pady=5)

        self.boton_suma = tk.Button(self.formulario01, text='Sumar', command=self.sumar)
        self.boton_suma.grid(column=0, row=2, padx=5, pady=10)

        self.boton_resta = tk.Button(self.formulario01, text='Restar', command=self.restar)
        self.boton_resta.grid(column=1, row=2, padx=5, pady=10)

        self.resultado = tk.Label(self.formulario01, text='Resultado:')
        self.resultado.grid(column=0, row=3, columnspan=2, pady=5)

        self.formulario01.mainloop()

    def sumar(self):
        try:
            num1 = float(self.dato01.get())
            num2 = float(self.dato02.get())
            self.resultado.configure(text=f"Resultado: {num1 + num2}")
        except ValueError:
            self.resultado.configure(text="Ingrese números válidos.")

    def restar(self):
        try:
            num1 = float(self.dato01.get())
            num2 = float(self.dato02.get())
            self.resultado.configure(text=f"Resultado: {num1 - num2}")
        except ValueError:
            self.resultado.configure(text="Ingrese números válidos.")

ejecuta = Aplicacion()