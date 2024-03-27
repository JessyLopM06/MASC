"""from tkinter import Tk, Label, Button, Entry, Text, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='gray84')
ventana.geometry('580x480')#Ancho x largo
ventana.resizable(0, 0)
ventana.title('Save data in Excel')

nombre1, apellido1, edad1, correo1, telefono1, comentarios1 = [], [], [], [], [], []

def agregar_datos():
    global nombre1, apellido1, edad1, correo1, telefono1, comentarios1

    nombre1.append(ingresa_nombre.get())
    apellido1.append(ingresa_apellido.get())
    edad1.append(ingresa_edad.get())
    correo1.append(ingresa_correo.get())
    telefono1.append(ingresa_telefono.get())
    comentarios1.append(ingresa_comentarios.get("1.0", END).strip())

    ingresa_nombre.delete(0, END)
    ingresa_apellido.delete(0, END)
    ingresa_edad.delete(0, END)
    ingresa_correo.delete(0, END)
    ingresa_telefono.delete(0, END)
    ingresa_comentarios.delete("1.0", END)

def guardar_datos():
    global nombre1, apellido1, edad1, correo1, telefono1, comentarios1
    datos = {'Nombres': nombre1, 'Apellidos': apellido1, 'Fecha': edad1, 'Correo': correo1, 'Telefono': telefono1, 'Comentarios': comentarios1}
    nom_excel = str(nombre_archivo.get() + ".xlsx")
    df = pd.DataFrame(datos, columns=['Nombres', 'Apellidos', 'Fecha', 'Correo', 'Telefono', 'Comentarios'])
    df.to_excel(nom_excel)
    nombre_archivo.delete(0, END)

frame1 = Frame(ventana, bg='gray84')##87CEEB
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray84')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text='Name',bg='#003399', font=('Arial', 12, 'bold'),fg='white', width=10).grid(column=0, row=0, pady=20, padx=10)
ingresa_nombre = Entry(frame1, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=3)
ingresa_nombre.grid(column=1, row=0)

apellido = Label(frame1, text='Last name', bg='#003399', font=('Arial', 12, 'bold'),fg='white',width=10).grid(column=0, row=1, pady=20, padx=10)
ingresa_apellido = Entry(frame1, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=3)
ingresa_apellido.grid(column=1, row=1)

edad = Label(frame1, text='Date', bg='#003399', font=('Arial', 12, 'bold'),fg='white',width=10).grid(column=0, row=2, pady=20, padx=10)
ingresa_edad = Entry(frame1, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=3)
ingresa_edad.grid(column=1, row=2)

correo = Label(frame1, text='Mail',bg='#003399', font=('Arial', 12, 'bold'),fg='white', width=10).grid(column=0, row=3, pady=20, padx=10)
ingresa_correo = Entry(frame1, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=3)
ingresa_correo.grid(column=1, row=3)

telefono = Label(frame1, text='Phone',bg='#003399', font=('Arial', 12, 'bold'),fg='white', width=10).grid(column=0, row=4, pady=20, padx=10)
ingresa_telefono = Entry(frame1, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=3)
ingresa_telefono.grid(column=1, row=4)

comentarios_label = Label(frame1, text='Comments',bg='#003399', font=('Arial', 12, 'bold'),fg='white',width=10).grid(column=0, row=6, pady=20, padx=10)
ingresa_comentarios = Text(frame1, height=4, width=20, font=('Arial', 12),highlightbackground="blue4", highlightthickness=4)
ingresa_comentarios.grid(column=1, row=6)

#Boton Agregar
agregar = Button(frame1, width=20, font=('Arial', 12, 'bold'),fg='white', text='Add', bg='blue4', bd=5, command=agregar_datos)
agregar.grid(columnspan=2, row=7, pady=20, padx=10)


archivo = Label(frame2, text='Enter File Name', width=20, bg='#003399', font=('Arial', 12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=30 , padx=40)

nombre_archivo = Entry(frame2, width=23, font=('Arial', 12), highlightbackground="blue4", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx=10)

#Boton Guardar
guardar = Button(frame2, width=20, font=('Arial', 12, 'bold') ,fg='white',text='Save data', bg='blue4', bd=5, command=guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx=10)

ventana.mainloop()

"""





from tkinter import Tk, Label, Button, Entry, Text, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='gray84')
ventana.geometry('750x550')  # Ancho x largo
ventana.resizable(0, 0)
ventana.title('Save data in Excel')

nombre1, apellido1, edad1, correo1, telefono1, comentarios1 = [], [], [], [], [], []

def agregar_datos():
    global nombre1, apellido1, edad1, correo1, telefono1, comentarios1

    nombre1.append(ingresa_nombre.get())
    apellido1.append(ingresa_apellido.get())
    edad1.append(ingresa_edad.get())
    correo1.append(ingresa_correo.get())
    telefono1.append(ingresa_telefono.get())
    comentarios1.append(ingresa_comentarios.get("1.0", END).strip())

    ingresa_nombre.delete(0, END)
    ingresa_apellido.delete(0, END)
    ingresa_edad.delete(0, END)
    ingresa_correo.delete(0, END)
    ingresa_telefono.delete(0, END)
    ingresa_comentarios.delete("1.0", END)

def guardar_datos():
    global nombre1, apellido1, edad1, correo1, telefono1, comentarios1
    datos = {'Nombres': nombre1, 'Apellidos': apellido1, 'Fecha': edad1, 'Correo': correo1, 'Telefono': telefono1, 'Comentarios': comentarios1}
    nom_archivo = nombre_archivo.get() + ".xlsx"

    try:
        # Intenta cargar el archivo existente
        df_existente = pd.read_excel(nom_archivo)
        
        # Combina los datos existentes con los nuevos
        df_nuevo = pd.concat([df_existente, pd.DataFrame(datos)])
    except FileNotFoundError:
        # Si el archivo no existe, crea un DataFrame con los nuevos datos
        df_nuevo = pd.DataFrame(datos)

    # Guarda el DataFrame en el archivo Excel
    df_nuevo.to_excel(nom_archivo, index=False)
    nombre_archivo.delete(0, END)

frame1 = Frame(ventana, bg='gray84')  ##87CEEB
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray84')
frame2.grid(column=1, row=0, sticky='nsew')



etiqueta_superior = Label(frame1, text=
                          '''
Please complete all fields, then press "Add" to 
save your data.Finally, type the filename in 
which your data will be saved and press "Save data".
'''
                          , bg='gray84', font=('Arial', 12, 'bold'))
etiqueta_superior.grid(columnspan=3, row=0, pady=5, padx=5)

nombre = Label(frame1, text='👤 Name', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=1, pady=10, padx=10)
ingresa_nombre = Entry(frame1, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_nombre.grid(column=1, row=1)

apellido = Label(frame1, text='👥 Last name', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=2, pady=10, padx=10)
ingresa_apellido = Entry(frame1, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_apellido.grid(column=1, row=2)

edad = Label(frame1, text='📅 Date', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=3, pady=10, padx=10)
ingresa_edad = Entry(frame1, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_edad.grid(column=1, row=3)

correo = Label(frame1, text='@ Mail', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=4, pady=10, padx=10)
ingresa_correo = Entry(frame1, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_correo.grid(column=1, row=4)

telefono = Label(frame1, text='📞 Phone', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=5, pady=10, padx=10)
ingresa_telefono = Entry(frame1, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=3)
ingresa_telefono.grid(column=1, row=5)

comentarios_label = Label(frame1, text='💬 Comments', bg='#003399', font=('Arial', 12, 'bold'), fg='white', width=12).grid(column=0, row=6, pady=40, padx=10)
ingresa_comentarios = Text(frame1, height=4, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=4)
ingresa_comentarios.grid(column=1, row=6)

# Boton Agregar
agregar = Button(frame1, width=20, font=('Arial', 12, 'bold'), fg='white', text='✔ Add', bg='blue4', bd=5, command=agregar_datos)
agregar.grid(columnspan=2, row=7, pady=20, padx=10)

archivo = Label(frame2, text='📁 Enter File Name', width=20, bg='#003399', font=('Arial', 12, 'bold'), fg='white')
archivo.grid(column=0, row=1, pady=(120, 10), padx=20)  # Reducir el espacio vertical entre el label y el resto de widgets

nombre_archivo = Entry(frame2, width=20, font=('Arial', 12), highlightbackground="blue4", highlightthickness=4)
nombre_archivo.grid(column=0, row=2, padx=20, pady=(0, 20), sticky="n") 
# Boton Guardar
guardar = Button(frame2, width=20, font=('Arial', 12, 'bold'), fg='white', text='💾 Save data', bg='blue4', bd=5, command=guardar_datos)
guardar.grid(column=0, row=3, pady=0, padx=10)

# Función para manejar la acción de clic en el botón "Aceptar"
def cerrar_ventana():
    ventana.destroy()   

# Boton Salir
guardar = Button(frame2, width=20, font=('Arial', 12, 'bold'), fg='white', text='❌ Close', bg='blue4', bd=5, command=cerrar_ventana)
guardar.grid(column=0, row=90, pady=218, padx=10)


ventana.mainloop()
