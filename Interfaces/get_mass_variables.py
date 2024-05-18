"""
Este modulo proporciona una interfaz de masa_activa de usuario utilizando tkinter.
"""
import tkinter as tk
from tkinter import messagebox

def ejecutar_mass_variables():
    root = tk.Tk()

    # Configurar la ventana de Tkinter y los elementos de la interfaz de usuario
    root.config(bg='gray84')
    root.geometry('650x500') #ancho x largo
    root.resizable(0, 0)
    root.title("Active Mass")

    # Definir las variables globales
    global active_mass_entry, density_entry, mol_weight_entry, div_win_entry, electrons_entry, DLC_entry, REFERENCE_ELECTRODE_entry, Mmol_entry, surface_area_entry

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
    mol_weight_label = tk.Label(root, text='Molar mass of active material (gmol⁻¹)',
        bg='#003399', font=('Arial',12,'bold'), fg='white',width=40)
    mol_weight_label.grid(row=2,column=0,pady=8,padx=10, sticky='w')

    mol_weight_entry = tk.Entry(root,width=20, font=('Arial',12),highlightbackground='blue4',
        highlightthickness=3)
    mol_weight_entry.grid(row=2, column=1, pady=5, padx=10, sticky='w')

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

    def cerrar_ventana():
        active_mass, density, mol_weight, div_win, electrons, DLC, REFERENCE_ELECTRODE, Mmol, surface_area = obtener_valores()
        print(f'{active_mass}')
        # Verificar si algún campo está vacío
        if not all((active_mass, density, mol_weight, div_win, electrons, DLC, REFERENCE_ELECTRODE, Mmol, surface_area)):
            # Mostrar mensaje de advertencia
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
        else:
            # Cerrar la ventana si todos los campos están completos
            root.destroy()

    # Botón "Aceptar"
    boton_aceptar = tk.Button(root, text="✔Aceptar", command=cerrar_ventana, bg="blue4",
        fg="white", font=("Arial", 12,'bold'),activeforeground='#1414b8')
    boton_aceptar.place(relx=0.5, rely=0.90, anchor='center')

    root.mainloop()

def obtener_valores():
    return active_mass_entry.get(), density_entry.get(), mol_weight_entry.get(), div_win_entry.get(), electrons_entry.get(), DLC_entry.get(), REFERENCE_ELECTRODE_entry.get(), Mmol_entry.get(), surface_area_entry.get()
