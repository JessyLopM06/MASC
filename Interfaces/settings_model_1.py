# Importa las bibliotecas necesarias
from tkinter import Tk, Label, Button, Entry, END, filedialog, Scrollbar, Listbox
from tkinter import messagebox
from tkinter import Toplevel
import importlib.util
import subprocess
import get_mass_variables

# Define las variables globales para las rutas de archivo y velocidades
file_paths = []
speeds = []
velocities_entry = None

# Define la función para seleccionar un archivo
def select_file(archivos_seleccionados, vel, listbox):
    ventana.attributes('-topmost', False)
    filepath = filedialog.askopenfilename()
    if filepath:
        archivos_seleccionados.append(filepath)
        actualizar_texto(archivos_seleccionados, vel, listbox)
        ventana.attributes('-topmost', True)

def delete_file(archivos_seleccionados, velocidades, listbox):
    selected_index = listbox.curselection()  # Obtiene el índice del elemento seleccionado
    if selected_index:
        index = selected_index[0]  # Obtiene el primer índice seleccionado (puede haber múltiples selecciones)
        del archivos_seleccionados[index]
        del velocidades[index]
        listbox.delete(index)  # Elimina el elemento seleccionado del Listbox

# Define la función para agregar una velocidad
def agregar_velocidad(velocidad, velocities, listbox):
    if velocidad:
        velocities.append(velocidad)
        actualizar_texto(file_paths, velocities, listbox)

# Define la función para actualizar el texto en la lista
def actualizar_texto(archivos_seleccionados, velocidades, listbox):
    listbox.delete(0, END)
    for i, (archivo, velocidad) in enumerate(zip(archivos_seleccionados, velocidades), start=1):
        listbox.insert(END, f"Speed {i}: {velocidad}, File: {archivo}")

# Define la función que se llama cuando se hace clic en el botón "Generate by Mass"
def generar_por_masa():
    get_mass_variables.object.file_paths = file_paths
    get_mass_variables.object.speeds = speeds
    print(get_mass_variables.object.active_mass)
    print(get_mass_variables.object.file_paths)
    print(get_mass_variables.object.speeds)
    #subprocess.run(["python", "Interfaces/brain_model_1_mass.py"], shell=True)

def mostrar_masa():
    ventana.attributes('-topmost', False)
    get_mass_variables.ejecutar_mass_variables()
    ventana.attributes('-topmost', True)

def mostrar_area():
    ventana.attributes('-topmost', False)
    subprocess.run(["python", "Interfaces/get_area_variables.py"], shell=True)
    ventana.attributes('-topmost', True)

def abrir_settings():
    global ventana
    ventana = Tk()
    ventana.config(bg='gray84')
    ventana.geometry('700x800')
    ventana.resizable(0, 0)
    ventana.title('Settings')

    # Etiqueta
    Label(ventana, text='Scan rate mVs⁻¹', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=20).grid(column=0, row=0, pady=15, padx=10)

    # Entrada
    velocities_entry = Entry(ventana, width=10, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
    velocities_entry.grid(column=1, row=0)

    # Botones
    Button(ventana, width=10, font=('Arial', 12, 'bold'), fg='white', text='📁Select File', bg='blue4', bd=5, command=lambda: select_file(file_paths, speeds, lista)).grid(column=2, row=0, pady=10, padx=20)
    Button(ventana, width=10, font=('Arial', 12, 'bold'), fg='white', text='❌Delete', bg='blue4', bd=5, command=lambda: delete_file(file_paths, speeds, lista)).grid(column=3, row=0, pady=10, padx=20)
    Button(ventana, width=10, font=('Arial', 12, 'bold'), fg='white', text='➕Add', bg='blue4', bd=5, command=lambda: agregar_velocidad(velocities_entry.get(), speeds, lista)).grid(column=0, row=1, pady=10, padx=20)
    Button(ventana, width=10, font=('Arial', 12, 'bold'), fg='white', text='Area', bg='blue4', bd=5, command=mostrar_area).grid(column=0, row=3, columnspan=3, pady=10, padx=(20,6))
    Button(ventana, width=10, font=('Arial', 12, 'bold'), fg='white', text='Mass', bg='blue4', bd=5, command=mostrar_masa).grid(column=1, row=3, columnspan=2, pady=5, padx=(50, 6))
    Button(ventana, width=13, font=('Arial', 11, 'bold'), fg='white', text='Generate by Area', bg='#116c2c', bd=5, command=lambda:mostrar_area).grid(column=0, row=4, columnspan=3, pady=10, padx=(30,6))
    Button(ventana, width=14, font=('Arial', 11, 'bold'), fg='white', text='Guardar', bg='#116c2c', bd=5, command=generar_por_masa).grid(column=1, row=4, columnspan=2, pady=5, padx=(100,6)) #Generate by Mass

    # Lista y scrollbar
    scrollbar = Scrollbar(ventana, orient="vertical")
    scrollbar.grid(row=2, column=4, sticky="ns")
    lista = Listbox(ventana, yscrollcommand=scrollbar.set, width=60, height=20)
    lista.grid(column=0, row=2, columnspan=4, padx=10, pady=10)
    scrollbar.config(command=lista.yview)

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()
