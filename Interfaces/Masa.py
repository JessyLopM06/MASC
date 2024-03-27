import tkinter as tk

def aceptar():
    # Aquí puedes agregar la lógica para el botón "Aceptar"
    pass

root = tk.Tk()
root.title("Active Mass")

# Función para crear una etiqueta y una caja de texto
def crear_caja_texto(etiqueta_texto):
    frame = tk.Frame(root)
    frame.pack(pady=6)

    etiqueta = tk.Label(frame, text=etiqueta_texto, font=("Arial", 12,'bold'),fg='snow', bg='#003399',anchor=tk.CENTER, justify=tk.CENTER, width=40,)
    etiqueta.pack(side=tk.LEFT, padx=6, pady=10)

    caja_texto = tk.Entry(frame, width=10, font=('Arial', 12),highlightbackground="blue4", highlightthickness=4)
    caja_texto.pack(side=tk.LEFT, padx=12)

# Crear cajas de texto y etiquetas
etiquetas = [
    "Molecular Mass of active (g mol⁻¹):",
    "Active material desnity (g cm³):",
    "Mass of Active Material:",
    "Potencial steps:",
    "Number of electrons:",
    "Electric double layer capacitance (Trassati Cg⁻¹):",
    "Reference electroide:"
]

for etiqueta in etiquetas:
    crear_caja_texto(etiqueta)



# Función para manejar la acción de clic en el botón "Aceptar"
def aceptar():
    root.destroy()

# Botón "Aceptar"
boton_aceptar = tk.Button(root, text="✔Aceptar", command=aceptar, bg="blue4", fg="white", font=("Arial", 14,'bold'),activeforeground='#1414b8')
boton_aceptar.pack(pady=10)

root.mainloop()
