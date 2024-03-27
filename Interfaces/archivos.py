
from tkinter import Tk, Label, Button, Entry, END, filedialog, Scrollbar, Listbox, simpledialog

#Funcion para  abrir ventana emergente 
import subprocess

# Función para manejar la acción de seleccionar un archivo
def select_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        archivos_seleccionados.append(filepath)
        actualizar_texto()

# Función para manejar la acción de eliminar un archivo seleccionado
def delete_file():
    global row_num
    if archivos_seleccionados:
        archivos_seleccionados.pop()
        velocidades.pop()
        row_num -= 1
        actualizar_texto()

# Función para manejar la acción de agregar una velocidad
def agregar_velocidad():
    velocidad = ingresa_velocidad.get()
    if velocidad:
        velocidades.append(velocidad)
        ingresa_velocidad.delete(0, END)
        actualizar_texto()

# Función para agregar un nuevo conjunto de entrada, selección y eliminación de archivo
def agregar_conjunto():
    global row_num
    row_num += 1
    
    Label(text=f'Sweep Speeds {row_num} m v⁻¹', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=20).grid(column=0, row=row_num, pady=15, padx=10)
    Entry(width=10, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3).grid(column=1, row=row_num)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='📁Select File', bg='blue4', bd=5, command=select_file).grid(column=2, row=row_num, pady=10, padx=20)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='❌Delete', bg='blue4', bd=5, command=delete_file).grid(column=3, row=row_num, pady=10, padx=20)
    Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='+', bg='blue4', bd=5, command=mostrar_messagebox).grid(column=2, row=6, pady=10, padx=20)


# Función para actualizar el texto en el área de visualización
def actualizar_texto():
    listbox.delete(0, END)
    for i, (archivo, velocidad) in enumerate(zip(archivos_seleccionados, velocidades), start=1):
        listbox.insert(END, f"Speed {i}: {velocidad}, File: {archivo}")



"""# Función para abrir el script de acuerdo a la opción seleccionada
def abrir_script(opcion):
    if opcion == "Mass":
        subprocess.Popen(["python", "Interfaces/Masa.py"])  # Reemplaza "script_masa.py" con el nombre de tu script de masa
    elif opcion == "Area":
        subprocess.Popen(["python", "Interfaces/Area_activa.py"])  # Reemplaza "script_area.py" con el nombre de tu script de área

# Función para manejar la acción de clic en el botón "+"
def mostrar_dialogo():
    opcion = simpledialog.askstring("Select", "What do you want to select? (Mass/Area)")
    if opcion:
        abrir_script(opcion)"""

# Función para manejar la acción de clic en el botón "Aceptar"
def cerrar_ventana():
    ventana.destroy() 


#Para abrir las ventanas de area y masa
def mostrar_masa():
    subprocess.run(["python", "Interfaces/Masa.py"])

def mostrar_area():
    subprocess.run(["python", "Interfaces/Area_activa.py"])





# Configuración inicial
ventana = Tk()
ventana.config(bg='gray84')
ventana.geometry('700x800')
ventana.resizable(0, 0)
ventana.title('Settings')

# Listas para almacenar archivos seleccionados y velocidades ingresadas
archivos_seleccionados = []
velocidades = []

# Elementos de la interfaz
Label(text='Sweep Speeds m v⁻¹', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=20).grid(column=0, row=0, pady=15, padx=10)
ingresa_velocidad = Entry(width=10, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_velocidad.grid(column=1, row=0)
Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='📁Select File', bg='blue4', bd=5, command=select_file).grid(column=2, row=0, pady=10, padx=20)
Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='❌Delete', bg='blue4', bd=5, command=delete_file).grid(column=3, row=0, pady=10, padx=20)
Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='➕Add', bg='blue4', bd=5, command=agregar_velocidad).grid(column=0, row=1, pady=10, padx=20)

#Buttons area y masa
Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='Area', bg='blue4', bd=5, command=mostrar_area).grid(column=0, row=3, columnspan=3, pady=10, padx=10)
Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='Mass', bg='blue4', bd=5, command=mostrar_masa).grid(column=1, row=3, columnspan=2, pady=10, padx=10)


Button(width=10, font=('Arial', 12, 'bold'), fg='white', text='✔ Accept', bg='blue4', bd=5, command=cerrar_ventana).grid(column=2, row=3, columnspan=5, pady=10, padx=10)



scrollbar = Scrollbar(ventana, orient="vertical")
scrollbar.grid(row=2, column=4, sticky="ns")
listbox = Listbox(ventana, yscrollcommand=scrollbar.set, width=60, height=20)
listbox.grid(column=0, row=2, columnspan=4, padx=10, pady=10)
scrollbar.config(command=listbox.yview)




# Número de fila para el siguiente conjunto de entrada
row_num = 1

ventana.mainloop()
