"""
Este modulo proporciona una interfaz de masa_activa de usuario utilizando tkinter.
"""
import tkinter as tk

# Declarar variables globales
active_mass = tk.StringVar()
density = tk.StringVar()
mass_elec = tk.StringVar()
div_win = tk.StringVar()
electrons = tk.StringVar()
DLC = tk.StringVar()
REFERENCE_ELECTRODE = tk.StringVar()
Mmol = tk.StringVar()
surface_area = tk.StringVar()

root = tk.Tk()
root.config(bg='gray84')
root.geometry('650x500') #ancho x largo
root.resizable(0, 0)
root.title("Active Mass")

# Mass of active material
active_mass_label = tk.Label(root, text='Mass of active material :', bg='#003399',
        font=('Arial',12,'bold'), fg='white',width=40)
active_mass_label.grid(row=0,column=0,pady=5,padx=10, sticky='w')

active_mass_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
active_mass_entry.grid(row=0, column=1, pady=8, padx=10, sticky='w')

# Density
density_label = tk.Label(root, text='Active material density (g cm³):', bg='#003399',
    font=('Arial',12,'bold'), fg='white',width=40)
density_label.grid(row=1,column=0,pady=5,padx=10, sticky='w')

density_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
density_entry.grid(row=1, column=1, pady=8, padx=10, sticky='w')

# Mass of active material 
mass_elec_label = tk.Label(root, text='Molar mass of active material (gmol⁻¹)',
    bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
mass_elec_label.grid(row=2,column=0,pady=8,padx=10, sticky='w')

mass_elec_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
mass_elec_entry.grid(row=2, column=1, pady=5, padx=10, sticky='w')

# Potencial steps
div_win_label = tk.Label(root, text='Potencial steps:', bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
div_win_label.grid(row=3,column=0,pady=5,padx=10, sticky='w')

div_win_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
div_win_entry.grid(row=3, column=1, pady=8, padx=10, sticky='w')

# Number of electons
electrons_label = tk.Label(root, text='Number of electrons:', bg='#003399',
    font=('Arial',12,'bold'), fg='white',width=40)
electrons_label.grid(row=4,column=0,pady=5,padx=10, sticky='w')

electrons_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
electrons_entry.grid(row=4, column=1, pady=8, padx=10, sticky='w')

# Electic double layer capacitamce (Trassati)
DLC_label = tk.Label(root, text='Electric double layer capacitance (Trassati Cg⁻¹):',
    bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
DLC_label.grid(row=5,column=0,pady=5,padx=10, sticky='w')

DLC_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
DLC_entry.grid(row=5, column=1, pady=8, padx=10, sticky='w')

# Reference electroide
REFERENCE_ELECTRODE_label = tk.Label(root, text='Reference electrode:', bg='#003399', 
    font=('Arial',12,'bold'), fg='white',width=40)
REFERENCE_ELECTRODE_label.grid(row=6,column=0,pady=5,padx=10, sticky='w')

REFERENCE_ELECTRODE_entry = tk.Entry(root,width=20, font=('Arial',12),
    highlightbackground='blue4',highlightthickness=3)
REFERENCE_ELECTRODE_entry.grid(row=6, column=1, pady=8, padx=10, sticky='w')

# Molar mass of active ion (g/mol ⁻¹)
Mmol_label = tk.Label(root, text='Molar mass of active ion (gmol⁻¹):', bg='#003399',
    font=('Arial',12,'bold'), fg='white',width=40)
Mmol_label.grid(row=7,column=0,pady=5,padx=10, sticky='w')

Mmol_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
Mmol_entry.grid(row=7, column=1, pady=8, padx=10, sticky='w')

# Specific surface area
surface_area_label = tk.Label(root, text='Specific surface area:', bg='#003399', 
    font=('Arial',12,'bold'), fg='white',width=40)
surface_area_label.grid(row=8,column=0,pady=5,padx=10, sticky='w')

surface_area_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
    highlightthickness=3)
surface_area_entry.grid(row=8, column=1, pady=8, padx=10, sticky='w')


def aceptar():
    # Obtener los valores de los Entry
    active_mass = active_mass_entry.get()
    density = density_entry.get()
    mass_elec = mass_elec_entry.get()
    div_win = div_win_entry.get()
    electrons = electrons_entry.get()
    DLC = DLC_entry.get()
    REFERENCE_ELECTRODE = REFERENCE_ELECTRODE_entry.get()
    Mmol = Mmol_entry.get()
    surface_area = surface_area_entry.get()

    # Aquí puedes usar los valores como desees, por ejemplo, imprimirlos
    print("Valor de Mass of active material:", active_mass)
    print("Valor de Active material density:", density)
    print("Valor de Molar mass of active material:", mass_elec)
    print("Valor de Potencial steps:", div_win)
    print("Valor de Number of electrons:", electrons)
    print("Valor de Electric double layer capacitance:", DLC)
    print("Valor de Reference electrode:", REFERENCE_ELECTRODE)
    print("Valor de Molar mass of active ion:", Mmol)
    print("Valor de Specific surface area:", surface_area)

    # Cerrar la ventana
    root.destroy()

## Botón "Aceptar"
boton_aceptar = tk.Button(root, text="✔Aceptar", command=aceptar, bg="blue4",
    fg="white", font=("Arial", 12,'bold'),activeforeground='#1414b8')
boton_aceptar.place(relx=0.5, rely=0.90, anchor='center')

root.mainloop()
