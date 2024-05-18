# Importa las bibliotecas necesarias
from tkinter import Tk, Label, Button, Entry, END, filedialog, Scrollbar, Listbox
import subprocess

# Define las variables globales para las rutas de archivo y velocidades
file_paths = []
speeds = []
velocities = 0

# Define la función para seleccionar un archivo
def select_file(archivos_seleccionados, vel, listbox):
    filepath = filedialog.askopenfilename()
    if filepath:
        archivos_seleccionados.append(filepath)
        actualizar_texto(archivos_seleccionados, vel, listbox)

# Define la función para eliminar un archivo seleccionado
def delete_file(archivos_seleccionados, velocidades, row_num, listbox):
    if archivos_seleccionados:
        archivos_seleccionados.pop()
        velocidades.pop()
        row_num -= 1
        actualizar_texto(archivos_seleccionados, velocidades, listbox)
    return row_num

# Define la función para agregar una velocidad
def agregar_velocidad(velocities, velocidades, listbox):
    velocidad = velocities.get()
    if velocidad:
        velocidades.append(velocidad)
        velocities.delete(0, END)
        actualizar_texto(file_paths, velocidades, listbox)

# Define la función para agregar un conjunto de archivo y velocidad
def agregar_conjunto(row_num, archivos_seleccionados, velocidades, listbox):
    row_num += 1
    Label(text=f'Scan rate {row_num} mVs⁻¹', bg='#003399', font=('Arial', 12, 'bold'),
          fg='white', width=20).grid(column=0, row=row_num, pady=15, padx=10)
    Entry(width=10, font=('Arial', 12), highlightbackground="blue4",
          highlightthickness=3).grid(column=1, row=row_num)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='📁Select File',
           bg='blue4', bd=5, command=lambda: select_file(archivos_seleccionados,
                                                          velocidades, listbox)).grid(column=2, row=row_num,
                                                                                     pady=10, padx=20)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='❌Delete',
           bg='blue4', bd=5, command=lambda: delete_file(archivos_seleccionados,
                                                          velocidades, row_num, listbox)).grid(column=3, row=row_num,
                                                                                                 pady=10, padx=20)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='+', bg='blue4', bd=5,
           command=lambda: agregar_velocidad(velocities, velocidades,
                                             listbox)).grid(column=2, row=6, pady=10, padx=20)

# Define la función para actualizar el texto en la lista
def actualizar_texto(archivos_seleccionados, velocidades, listbox):
    listbox.delete(0, END)
    for i, (archivo, velocidad) in enumerate(zip(archivos_seleccionados, velocidades), start=1):
        listbox.insert(END, f"Speed {i}: {velocidad}, File: {archivo}")

# Define la función para obtener las velocidades y rutas de archivo seleccionadas
def obtener_archivos_y_velocidades():
    return file_paths, speeds

# Define la función que se llama cuando se hace clic en el botón "Generate by Mass"
def generar_por_masa():
    subprocess.run(["python", "Interfaces/brain_model1_mass.py"], shell=True)

def mostrar_masa():
    subprocess.run(["python", "Interfaces/get_mass_variables.py"], shell=True)
def mostrar_area():
    subprocess.run(["python", "Interfaces/get_area_variables.py"], shell=True)

def ejecutar_settings():
    # Configura la ventana principal
    ventana = Tk()
    ventana.config(bg='gray84')
    ventana.geometry('700x800')
    ventana.resizable(0, 0)
    ventana.title('Settings')

    # Añade los elementos de la interfaz de usuario y define sus funciones de callback
    #Introduce las velocidades de barrido
    Label(text='Scan rate mVs⁻¹', bg='#003399', font=('Arial', 12, 'bold'), fg='white',
        width=20).grid(column=0, row=0, pady=15, padx=10)
    velocities = Entry(width=10, font=('Arial', 12), highlightbackground="blue4",
                    highlightthickness=3)
    velocities.grid(column=1, row=0)

    #Button Select File
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='📁Select File',
        bg='blue4', bd=5, command=lambda: select_file(file_paths,
                            speeds, lista)).grid(column=2, row=0, pady=10, padx=20)
    #Button Delete
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='❌Delete', bg='blue4',
        bd=5, command=lambda: delete_file(file_paths,
                        speeds, row_numero, lista)).grid(column=3, row=0, pady=10, padx=20)
    #Button Add
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='➕Add', bg='blue4',
        bd=5, command=lambda: agregar_velocidad(velocities,
                                speeds, lista)).grid(column=0, row=1, pady=10, padx=20)
    #Button Area
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='Area', bg='blue4',
        bd=5, command=mostrar_area).grid(column=0, row=3, columnspan=3, pady=10, padx=(20,6))
    #Button Mass
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='Mass', bg='blue4',
        bd=5, command=mostrar_masa).grid(column=1, row=3, columnspan=2, pady=5,
                                        padx=(50, 6))
    #Button Generar Area
    Button(width=13, font=('Arial', 11, 'bold'), fg='white', text='Generate by Area', bg='#116c2c',
        bd=5, command=mostrar_area).grid(column=0, row=4, columnspan=3, pady=10, padx=(30,6))
    #Button  Generar Mass
    Button(width=14, font=('Arial', 11, 'bold'), fg='white', text='Generate by Mass', bg='#116c2c',
        bd=5, command=generar_por_masa).grid(column=1, row=4, columnspan=2, pady=5,
                                        padx=(100,6))

    """Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='✔ Accept', bg='blue4',
        bd=5, command=lambda: cerrar_ventana(ventana)).grid(column=2, row=3, columnspan=5,
            pady=10, padx=10)"""

    scrollbar = Scrollbar(ventana, orient="vertical")
    scrollbar.grid(row=2, column=4, sticky="ns")
    lista = Listbox(ventana, yscrollcommand=scrollbar.set, width=60, height=20)
    lista.grid(column=0, row=2, columnspan=4, padx=10, pady=10)
    scrollbar.config(command=lista.yview)
    row_numero = 1

    # Ejecuta el bucle principal de la ventana
    ventana.mainloop()