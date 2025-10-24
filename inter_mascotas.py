import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import mascotas

class FormularioMascotas:
    def __init__(self):
        self.mascota1 = mascotas.Mascotas()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Gestión de Mascotas")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_mascotas()
        self.consulta_por_codigo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=30, pady=30)
        self.ventana1.mainloop()

    def carga_mascotas(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Mascota")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe1, text="Nombre:").grid(column=0, row=0, padx=4, pady=4)
        self.nombre = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.nombre).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Especie:").grid(column=0, row=1, padx=4, pady=4)
        self.especie = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.especie).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Sexo:").grid(column=0, row=2, padx=4, pady=4)
        self.sexo = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.sexo).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Fecha Nacimiento:").grid(column=0, row=3, padx=4, pady=4)
        self.nacimiento = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.nacimiento).grid(column=1, row=3, padx=4, pady=4)

        ttk.Button(self.labelframe1, text="Guardar", command=self.agregar).grid(column=1, row=4, padx=4, pady=4)

    def agregar(self):
        datos = (self.nombre.get(), self.especie.get(), self.sexo.get(), self.nacimiento.get())
        self.mascota1.alta(datos)
        mb.showinfo("Información", "La mascota fue registrada correctamente")
        self.nombre.set("")
        self.especie.set("")
        self.sexo.set("")
        self.nacimiento.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consultar")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Mascota")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe2, text="Código (PetID):").grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.codigo).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Nombre:").grid(column=0, row=1, padx=4, pady=4)
        self.nombrec = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.nombrec, state="readonly").grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Especie:").grid(column=0, row=2, padx=4, pady=4)
        self.especiec = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.especiec, state="readonly").grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Sexo:").grid(column=0, row=3, padx=4, pady=4)
        self.sexoc = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.sexoc, state="readonly").grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Nacimiento:").grid(column=0, row=4, padx=4, pady=4)
        self.birthc = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.birthc, state="readonly").grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(self.labelframe2, text="Consultar", command=self.consultar).grid(column=1, row=5, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(),)
        respuesta = self.mascota1.consulta(datos)
        if len(respuesta) > 0:
            self.nombrec.set(respuesta[0][0])
            self.especiec.set(respuesta[0][1])
            self.sexoc.set(respuesta[0][2])
            self.birthc.set(respuesta[0][3])
        else:
            self.nombrec.set("")
            self.especiec.set("")
            self.sexoc.set("")
            self.birthc.set("")
            mb.showinfo("Información", "No existe una mascota con ese código")

    def borrado(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Eliminar")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Mascota")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe3, text="Código (PetID):").grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra = tk.StringVar()
        ttk.Entry(self.labelframe3, textvariable=self.codigoborra).grid(column=1, row=0, padx=4, pady=4)
        ttk.Button(self.labelframe3, text="Eliminar", command=self.borrar).grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(),)
        cantidad = self.mascota1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Mascota eliminada correctamente")
        else:
            mb.showinfo("Información", "No existe una mascota con ese código")

    def modificar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Modificar")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Mascota")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe4, text="Código (PetID):").grid(column=0, row=0, padx=4, pady=4)
        self.codigomod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.codigomod).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Nombre:").grid(column=0, row=1, padx=4, pady=4)
        self.nombremod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.nombremod).grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Especie:").grid(column=0, row=2, padx=4, pady=4)
        self.especiemod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.especiemod).grid(column=1, row=2, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Sexo:").grid(column=0, row=3, padx=4, pady=4)
        self.sexomod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.sexomod).grid(column=1, row=3, padx=4, pady=4)

        ttk.Label(self.labelframe4, text="Nacimiento:").grid(column=0, row=4, padx=4, pady=4)
        self.birthmod = tk.StringVar()
        ttk.Entry(self.labelframe4, textvariable=self.birthmod).grid(column=1, row=4, padx=4, pady=4)

        ttk.Button(self.labelframe4, text="Modificar", command=self.modifica).grid(column=1, row=5, padx=4, pady=4)

    def modifica(self):
        datos = (self.nombremod.get(), self.especiemod.get(), self.sexomod.get(), self.birthmod.get(), self.codigomod.get())
        cantidad = self.mascota1.modificacion(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Datos modificados correctamente")
        else:
            mb.showinfo("Información", "No existe una mascota con ese código")

aplicacion1 = FormularioMascotas()
