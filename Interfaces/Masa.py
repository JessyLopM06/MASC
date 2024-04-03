import tkinter as tk

root = tk.Tk()
root.config(bg='gray84')
root.geometry('650x400') #ancho x largo
root.resizable(0, 0)
root.title("Active Mass")

"""# Función para crear una etiqueta y una caja de texto
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
"""


#mol
mol = tk.Label(root, text='Molecular Mass of active (g mol⁻¹):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
mol.grid(row=0,column=0,pady=8,padx=10, sticky='w')

ingresa_mol = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_mol.grid(row=0, column=1, pady=5, padx=10, sticky='w')

#density
density = tk.Label(root, text='Active material desnity (g cm³):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
density.grid(row=1,column=0,pady=5,padx=10, sticky='w')

ingresa_density = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_density.grid(row=1, column=1, pady=8, padx=10, sticky='w')

#Mass of Active Material
act_material = tk.Label(root, text='Mass of Active Material:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
act_material.grid(row=2,column=0,pady=5,padx=10, sticky='w')

ingresa_material = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_material.grid(row=2, column=1, pady=8, padx=10, sticky='w')

#Potencial steps
pot_steps = tk.Label(root, text='Potencial steps:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
pot_steps.grid(row=3,column=0,pady=5,padx=10, sticky='w')

ingresa_steps = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_steps.grid(row=3, column=1, pady=8, padx=10, sticky='w')

#Number of electons
num_elec = tk.Label(root, text='Number of electrons:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
num_elec.grid(row=4,column=0,pady=5,padx=10, sticky='w')

ingresa_elec = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_elec.grid(row=4, column=1, pady=8, padx=10, sticky='w')

#Electic double layer capacitamce (Trassati)
trassati = tk.Label(root, text='Electric double layer capacitance (Trassati Cg⁻¹):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
trassati.grid(row=5,column=0,pady=5,padx=10, sticky='w')

ingresa_trassati = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_trassati.grid(row=5, column=1, pady=8, padx=10, sticky='w')

#Reference electroide
ref_elec = tk.Label(root, text='Reference electroide:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
ref_elec.grid(row=6,column=0,pady=5,padx=10, sticky='w')

ingresa_reference = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_reference.grid(row=6, column=1, pady=8, padx=10, sticky='w')

"""#Current Density (mAcm⁻²)
current = tk.Label(root, text='Current Density (mAcm⁻²):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
current.grid(row=7,column=0,pady=5,padx=10, sticky='w')

ingresa_current = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_current.grid(row=7, column=1, pady=8, padx=10, sticky='w')
"""


# Función para manejar la acción de clic en el botón "Aceptar"
def aceptar():
    root.destroy()

## Botón "Aceptar"
boton_aceptar = tk.Button(root, text="✔Aceptar", command=aceptar, bg="blue4", fg="white", font=("Arial", 12,'bold'),activeforeground='#1414b8')
boton_aceptar.place(relx=0.5, rely=0.95, anchor='center')


root.mainloop()
