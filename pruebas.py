import tkinter as tk

class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        # Puedes agregar más atributos según sea necesario

class Formulario(tk.Tk):
    def __init__(self):
        super().__init__()

        self.entry_nombre = None
        self.entry_edad = None
        # Puedes agregar más Entry widgets aquí

        self.persona = Persona()  # Instanciamos un objeto Persona

        self.crear_formulario()

    def crear_formulario(self):
        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Edad:").pack()
        self.entry_edad = tk.Entry(self)
        self.entry_edad.pack()

        # Puedes agregar más Entry widgets aquí

        boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        boton_guardar.pack()

    def guardar_datos(self):
        # Guardamos los valores ingresados en el objeto Persona
        self.persona.nombre = self.entry_nombre.get()
        self.persona.edad = int(self.entry_edad.get())  # Suponiendo que la edad es un número

        # Puedes hacer más asignaciones para otros atributos del objeto Persona

        # Mostramos los datos guardados en el objeto Persona
        print("Nombre:", self.persona.nombre)
        print("Edad:", self.persona.edad)

# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = Formulario()
    app.mainloop()