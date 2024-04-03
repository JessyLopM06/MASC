import tkinter as tk

root = tk.Tk()
root.config(bg='gray84')
root.geometry('650x500') #ancho x largo
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

#Mass of active material
active_mass = tk.Label(root, text='Mass of active material :', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
active_mass.grid(row=0,column=0,pady=5,padx=10, sticky='w')

active_mass = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
active_mass.grid(row=0, column=1, pady=8, padx=10, sticky='w')

#density
density = tk.Label(root, text='Active material desnity (g cm³):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
density.grid(row=1,column=0,pady=5,padx=10, sticky='w')

ingresa_density = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
ingresa_density.grid(row=1, column=1, pady=8, padx=10, sticky='w')

#Mass of active material 
mass_elec = tk.Label(root, text='Molecular Mass of active (g mol⁻¹):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
mass_elec.grid(row=2,column=0,pady=8,padx=10, sticky='w')

mass_elec = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
mass_elec.grid(row=2, column=1, pady=5, padx=10, sticky='w')

#Potencial steps
div_win = tk.Label(root, text='Potencial steps:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
div_win.grid(row=3,column=0,pady=5,padx=10, sticky='w')

div_win = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
div_win.grid(row=3, column=1, pady=8, padx=10, sticky='w')

#Number of electons
electrons = tk.Label(root, text='Number of electrons:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
electrons.grid(row=4,column=0,pady=5,padx=10, sticky='w')

electrons = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
electrons.grid(row=4, column=1, pady=8, padx=10, sticky='w')

#Electic double layer capacitamce (Trassati)
DLC = tk.Label(root, text='Electric double layer capacitance (Trassati Cg⁻¹):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
DLC.grid(row=5,column=0,pady=5,padx=10, sticky='w')

DLC = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
DLC.grid(row=5, column=1, pady=8, padx=10, sticky='w')

#Reference electroide
REFERENCE_ELECTRODE = tk.Label(root, text='Reference electrode:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
REFERENCE_ELECTRODE.grid(row=6,column=0,pady=5,padx=10, sticky='w')

REFERENCE_ELECTRODE = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
REFERENCE_ELECTRODE.grid(row=6, column=1, pady=8, padx=10, sticky='w')

#Molar mass of active ion (g/mol ⁻¹)
Mmol = tk.Label(root, text='Molar mass of active ion (g/mol ⁻¹):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
Mmol.grid(row=7,column=0,pady=5,padx=10, sticky='w')

Mmol = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
Mmol.grid(row=7, column=1, pady=8, padx=10, sticky='w')

#Mass of active material (g)
mass_elec = tk.Label(root, text='Mass of active material (g):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
mass_elec.grid(row=8,column=0,pady=5,padx=10, sticky='w')

mass_elec = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
mass_elec.grid(row=8, column=1, pady=8, padx=10, sticky='w')

# Molar mass of active material (g/mol)
mol_weight= tk.Label(root, text='Molar mass of active material (g/mol):', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
mol_weight.grid(row=9,column=0,pady=5,padx=10, sticky='w')

mol_weight = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',highlightthickness=3)
mol_weight.grid(row=9, column=1, pady=8, padx=10, sticky='w')



# Función para manejar la acción de clic en el botón "Aceptar"
def aceptar():
    root.destroy()

## Botón "Aceptar"
boton_aceptar = tk.Button(root, text="✔Aceptar", command=aceptar, bg="blue4", fg="white", font=("Arial", 12,'bold'),activeforeground='#1414b8')
boton_aceptar.place(relx=0.5, rely=0.95, anchor='center')


root.mainloop()
