"""
Este módulo proporciona una interfaz de los menu del modelo 1-3 utilizando tkinter.
"""

import tkinter as tk
import os
from tkinter import*
from tkinter import Frame
from tkinter import filedialog 

#Para poder abrir los xcript
import subprocess

#Para las graficas   
from customtkinter import CTk, CTkTabview
import tkinter.ttk as ttk

#Colors
#00ff00,#ffffff,#ff0000,#ffff00,#ff00ff,#00A000,#C0C0C0

#Azules
#0000ff ,#5353ec, #1919e6,#1414b8,#2c2c7d,#00aaff,#0066cc,#003399,#000080
class TabViewWithColoredMargin:
    def __init__(self, root) -> None:
        self.root = root

        # Creamos un Frame adicional para el margen con color personalizado
        self.margin_frame = tk.Frame(root, padx=10, pady=10, bg='#116c2c',width=1000,height=1000)  # Cambia 'verde' por el color que desees
        self.margin_frame.pack(fill=tk.BOTH)

        # Creamos el TabView dentro del Frame con margen
        self.tabview = CTkTabview(self.margin_frame, fg_color='#abbbb0',width=1070,height=470)#ancho x largo 840 x 320
        self.tabview.pack(side='right',fill=tk.BOTH)

        # Agregamos las pestañas al TabView
        for tab_name  in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            self.tabview.add(tab_name)

#List box de inico del modelo 1
def choose_files(listbox):
    file_paths = filedialog.askopenfilenames(filetypes=[('Text Files', '*.txt')])
    for file_path in file_paths:
        listbox.insert(tk.END, file_path)

def clear_selected_files(listbox):
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

def abrir_registro():
    subprocess.Popen(['python', 'Interfaces/excel.py'])

def ejecutar_descarga():
    # Ejecutar el script descarga.py
    subprocess.Popen(["python", "Interfaces/descarga.py"])


def ejecutar_settings():
#Ejecutar el script donde se van a subir las velociadades de barrido y
#conforme a eso se va apoder saber cuando el usuario ingrese la velocidad de barrido
#a que archivo pertenece"""

    subprocess.Popen(["python", "Interfaces/archivos.py"])


root = tk.Tk()
root.geometry('1000x1000')#Ancho x Largo
#root.resizable(0, 0)


# Crear un frame principal
main_frame = tk.Frame(root)
main_frame.pack()

ruta_icono = "./imagenes/wh.ico"
root.iconbitmap(ruta_icono)
root.title('MASC: Multiple Analysis Software for Supercapacitors')

texto_copyright = "Copyright © rlucioporto.com\nLa ciencia, una luz en la oscuridad.\n   "
label_copyright = tk.Label(root, text=texto_copyright, bg="navy", fg="white", font=("Arial", 8,'bold'))
label_copyright.pack(side="bottom", fill="both")

#Se desliza el inidicador
def switch(indicator_lb, page):

    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg']= 'SystemButtonFace'


# Ajusta el grosor del borde para hacer el indicador más grande
    indicator_lb['bg'] = '#0097e8'
    #indicator_lb['borderwidth'] = 100  # Puedes ajustar el valor según tu preferencia
    indicator_lb['width'] = 100 # Puedes ajustar el valor según tu preferencia
    indicator_lb['height'] = 100# Puedes ajustar el valor según tu preferencia

#Para que aparezca informacion en diferente boton
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update() 
    page()
    
#Color de la barra de menu
options_fm= tk.Frame(root,bg='blue4')#bg=gray 

#Primer Boton
home_btn = tk.Button(options_fm, text='Comments', font=('Arial', 13,'bold'),bg='blue4',
                    bd=0, fg='snow', activeforeground='#1414b8',
                    command=abrir_registro)

'''home_btn = tk.Button(options_fm, text='' , font=('Arial, 13'),
                    bd=0, fg='#0097e8' ,activeforeground='#0097e8',
                    command=lambda:switch(indicator_lb=home_inidicator_lb,
                                        page=home_page))'''

home_btn.place(x=0 , y=0, width=125  )

#Indicadores 
#Boton 1
home_inidicator_lb = tk.Label(options_fm, bg='blue4')
home_inidicator_lb.place(x=22, y=30, width=80, height=2)

#boton 2
modelo1_inidicator_lb = tk.Label(options_fm)
modelo1_inidicator_lb.place(x=147, y=30, width=80, height=2)

#Boton 3
modelo2_inidicator_lb = tk.Label(options_fm)
modelo2_inidicator_lb.place(x=272, y=30, width=80, height=2)

#Boton 4
modelo3_inidicator_lb = tk.Label(options_fm)
modelo3_inidicator_lb.place(x=397, y=30, width=80, height=2)

#Boton 5
about_inidicator_lb = tk.Label(options_fm)
about_inidicator_lb.place(x=525, y=30, width=80, height=2)

#Segundo Boton
modelo1_btn = tk.Button(options_fm, text='Model 1', font=('Arial', 11,'bold'),bg='blue4',
                    bd=0, fg='snow' ,activeforeground='#1414b8',
                    command=lambda:switch(indicator_lb=modelo1_inidicator_lb,
                    page=modelo1_page))

modelo1_btn.place(x=125 , y=0, width=125  )

#Tercer Boton
modelo2_btn = tk.Button(options_fm, text='Model 2' , font=('Arial', 11,'bold'),bg='blue4',
                    bd=0, fg='snow' ,activeforeground='#1414b8',
                    command=lambda:switch(indicator_lb=modelo2_inidicator_lb,
                        page=modelo2_page))

modelo2_btn.place(x=250 , y=0, width=125  )

#Cuarto Boton
modelo3 = tk.Button(options_fm, text='Model 3' , font=('Arial', 11,'bold'),bg='blue4',
                    bd=0, fg='snow' ,activeforeground='#1414b8',
                    command=lambda:switch(indicator_lb=modelo3_inidicator_lb,
                                        page=modelo3_page))

modelo3.place(x=375 , y=0, width=125  )

#Quinto Boton
modelo3_btn = tk.Button(options_fm, text='About' , font=('Arial', 11,'bold'),bg='blue4',
                    bd=0, fg='snow' ,activeforeground='#1414b8',
                    command=lambda:switch(indicator_lb=about_inidicator_lb,
                                        page=about_page))

modelo3_btn.place(x=500 , y=0, width=125  )
options_fm.pack(pady=5)

#Tamaño del menu
options_fm.pack_propagate(False)
options_fm.configure(width=1400 ,height=35)


"""# Función para mostrar las imágenes y el texto
def mostrar_todo(event=None):
    label_left.grid(row=0, column=0, padx=10)
    label_center.grid(row=0, column=1)
    label_right.grid(row=0, column=2, padx=10)
    label_texto.grid(side="top")

# Función para ocultar las imágenes y el texto
def ocultar_todo(event=None):
    label_left.grid_forget()
    label_center.grid_forget()
    label_right.grid_forget()
    label_texto.pack_forget()"""


# Texto debajo de las imágenes
texto = "Dr. Raúl Lucio Porto\nCentro de Innovación, Investigación y Desarrollo en Ingeniería y Tecnología\nCentro de Innovación en Ingeniería de Tecnología Inteligente Biomédica y Mecatrónica\n"
label_texto = tk.Label( root,text=texto, justify="center", wraplength=1000, width=1400, bg="blue4", fg="white", font=("Arial", 9, 'bold'))
label_texto.pack()


def home_page():
    home_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    home_page_lb = tk.Label(home_page_fm,
                            font=('Arial',25), fg='#0097e8')

    home_page_lb.pack(pady=80)

    home_page_fm.pack(fill=tk.BOTH, expand=True)

def modelo1_page():
    
    # Elimina los frames existentes en main_fm
    for widget in main_fm.winfo_children():
        widget.destroy()

    # Crear un canvas para contener el frame interior,es el fondo
    canvas = tk.Canvas(main_fm, bg='gray84', highlightthickness=0)#main_fm, bg='#0097e8', highlightthickness=0
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Crear un scrollbar para el canvas
    scrollbar = tk.Scrollbar(main_fm, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Crear el frame interior que contendrá todos los elementos deslizables
    inner_frame = tk.Frame(canvas, bg='navy')
    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Crear el primer frame dentro del frame interior 
    frame1 = Frame(inner_frame, bg='gray84', width=3000, height=3000)
    frame1.grid(column=0, row=0, sticky='nsew')

    """V = tk.Label(frame1, text='Select one or more text files:', bg='gray84', font=('Arial', 12, 'bold'), fg='#003399', width=30)
    V.grid(column=0, row=0, pady=10, padx=20)"""

#Botones para el inicio del modelo 1 download,setings y continue
    # Button to download
    btn_download = Button(frame1, text='⬇ Download Files', font=('Arial', 12, 'bold'), bg='blue4', fg='white',activebackground='snow',activeforeground='blue4', command=ejecutar_descarga)
    btn_download.grid(row=4, column=0, columnspan=2, pady=2, padx=(10,10), sticky='nsew')  # Alinea a la derecha
    
    #Button to setiings
    btn_settings = Button(frame1, text='⚙ Settings', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activeforeground='blue4',command=ejecutar_settings)
    btn_settings.grid(row=5,column=0,columnspan=2,pady=2,padx=(10,10),sticky='nsew')

    """#Button to continue
    btn_continue = tk.Button(frame1, text='➡ Start', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activebackground='snow',activeforeground='blue4')
    btn_continue.grid(row=7,column=0,columnspan=2,pady=2,padx=(5,5),sticky='nsew')
"""
    # Crear el segundo frame dentro del frame interior
    frame2 = Frame(inner_frame, bg='gray84', width=2000, height=2000)#ancho x alto
    frame2.grid(column=1, row=0, sticky='nsew')

    # Agregar el código TabView al frame2
    app = TabViewWithColoredMargin(frame2)

    # Hacer que los frames sean expansibles
    main_fm.columnconfigure(0, weight=1)
    main_fm.rowconfigure(0, weight=1)

def modelo2_page():
    modelo2_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    modelo2_page_lb = tk.Label(modelo2_page_fm, text='Model 2',
                            font=('Arial',18,'bold'), fg='#1414b8')

    modelo2_page_lb.pack(pady=20)

    modelo2_page_fm.pack(fill=tk.BOTH, expand=True)

def modelo3_page():
    modelo3_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    modelo3_page_lb = tk.Label(modelo3_page_fm, text='Model 3',
                            font=('Arial',18,'bold'), fg='#1414b8')

    modelo3_page_lb.pack(pady=20)

    modelo3_page_fm.pack(fill=tk.BOTH, expand=True)
    
        
image_left = None
image_center = None
image_right = None

def about_page():
    global image_left, image_center, image_right  # Hacer las variables de imagen globales
    about_page_fm = tk.Frame(main_fm)  # Cambiar el fondo del marco a gris
    about_page_fm.pack(fill=tk.BOTH, expand=True)

    about_page_lb = tk.Label(about_page_fm, text='About MASC: Multiple Analysis Software for Capacitors',
                            font=('Arial', 15, 'bold'), fg='#1414b8')
    about_page_lb.pack(pady=10, padx=10)

    # Crear un marco para contener las imágenes
    image_frame = tk.Frame(about_page_fm)
    image_frame.pack(side=tk.TOP, fill=tk.X)

    # Configurar columnas para que se expandan y centren las imágenes
    image_frame.columnconfigure(0, weight=1)
    image_frame.columnconfigure(1, weight=1)
    image_frame.columnconfigure(2, weight=1)

    # Cargar las imágenes
    image_left = tk.PhotoImage(file="imagenes/uniM.png")
    label_left = tk.Label(image_frame, image=image_left)
    label_left.grid(row=0, column=0, padx=10)

    image_center = tk.PhotoImage(file="imagenes/logM1.png")  # m2ph
    label_center = tk.Label(image_frame, image=image_center)
    label_center.grid(row=0, column=1)

    image_right = tk.PhotoImage(file="imagenes/92.png")
    label_right = tk.Label(image_frame, image=image_right)
    label_right.grid(row=0, column=2, padx=10)

    about_text = """
    1. Introduction
The research on energy storage devices such as supercapacitors and batteries generates a lot of data that must be processed manually in several software, slowing down its analysis and interpretation. Thus, the lack of specialized software hinders accurate data analysis in the field of  supercapacitors, especially for non-programming users.
In this work we report a new software designed to simplify the electrochemical data analysis obtained in the study of new materials and devices for electrochemical capacitors and batteries. The Multiple Analyses of Supercapacitors Software (MASC) offers an efficient solution for electrochemical data analysis in this growing field.

2. Methodology​
MASC is purpose-built software for simplifying electrochemical data analysis in the quest for new supercapacitor materials and devices. Developed in Python with tkinter, MASC efficiently executes complex calculations using various functions.
Functionality: MASC accurately computes electrochemical properties, ensuring comprehensive coverage. Testing: Stringent testing protocols validate its accuracy and reliability across scenarios.
Structured in three modules, MASC seamlessly integrates data processing workflows, utilizing CSV files for input. Its goal is to offer an intuitive interface for researchers and scientists.
MASC aims to enhance data analysis efficiency by providing specialized and intuitive software. Initially targeted at CIIDIT's supercapacitor lab, future iterations will cater to users with diverse experience levels.
Requirements Analysis: Comprehensive understanding of project needs is key. Software Design: Focus on creating an intuitive and functional interface. Functionality Implementation: Robust algorithms for precise calculations. Testing and Validation: Extensive testing ensures reliability. Implementation and Distribution: Initial deployment planned in the research lab, with broader accessibility in future phases.​
    """
    about_text_txt = tk.Text(about_page_fm, wrap="word")
    about_text_txt.insert(tk.END, about_text)
    about_text_txt.config(state="disabled", font=("Arial", 11), bg="gray84", fg="black")
    about_text_txt.pack(expand=True, fill="both", padx=60, pady=10)

    about_page_fm.pack(fill=tk.BOTH, expand=True)

main_fm = tk.Frame(root, bg='gray84')  # Cambiar el fondo del marco principal a gris
main_fm.pack(fill=tk.BOTH, expand=True)

home_page()

root.mainloop()