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
#00ff00,#ffffff,#ff0000,#ffff00,#ff00ff

#Azules
#0000ff ,#5353ec, #1919e6,#1414b8,#2c2c7d,#00aaff,#0066cc,#003399,#000080           
Verdes= "#00A000"                   '                       '        
Grises="#C0C0C0"                



class TabView:
    def __init__(self, root) -> None:
        self.root = root
        self.TabTree = CTkTabview(root, fg_color='silver')
        self.TabTree.grid(row=2, column=3, rowspan=8, columnspan=7, sticky='nswe')

        # Crear un estilo personalizado para las pestañas
        self.tab_style = ttk.Style()
        self.tab_style.configure("CustomTab.TNotebook.Tab", font=("Helvetica", 12))  # Tamaño de fuente predeterminado

        # Agregar las pestañas al Tabview
        for tab_name in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            self.TabTree.add(tab_name)

        # Configurar el tamaño de la fuente para pestañas específicas
        self.set_tab_font('Interpolation', 100)  # Cambiar el tamaño de fuente para la pestaña 'Interpolation' a 16
        self.set_tab_font('Obtaining of K', 14)  # Cambiar el tamaño de fuente para la pestaña 'Obtaining of K' a 14

    def set_tab_font(self, tab_name, font_size):
        # Configurar el tamaño de la fuente para una pestaña específica
        self.tab_style.configure(f"CustomTab.TNotebook.Tab.{tab_name}", font=("Helvetica", font_size))


#List box
def choose_files(listbox):
    file_paths = filedialog.askopenfilenames(filetypes=[('Text Files', '*.txt')])
    for file_path in file_paths:
        listbox.insert(tk.END, file_path)

def clear_selected_files(listbox):
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

def abrir_registro():
    subprocess.Popen(['python', 'excel.py'])

#Aun en desarrollo 
def abrir_script_python():
    ruta_script = "masa.py"  # Reemplaza con la ruta de tu script
    subprocess.Popen(['python', ruta_script])  

def ejecutar_descarga():
    # Ejecutar el script descarga.py
    subprocess.Popen(["python", "descarga.py"])



def ejecutar_settings():
#Ejecutar el script donde se van a subir las velociadades de barrido y
#conforme a eso se va apoder saber cuando el usuario ingrese la velocidad de barrido
#a que archivo pertenece"""

    subprocess.Popen(["python", "archivos.py"])


def funcion_del_boton_Masa():
    subprocess.run(["python", "Masa.py"])


def funcion_del_boton_Area():
    subprocess.run(["python", "Area_activa.py"]) 

def ejecutar_velocities():
    #Ejecutar el script usuario_M.py
    subprocess.Popen(['python',"Avancess/usuario_M.py"])

root = tk.Tk()
root.geometry('1000x1000')

'''

scrollbar_vertical=tk.Scrollbar(root)
scrollbar_vertical.pack(side='right', fill='y')



scrollbar_horizontal=tk.Scrollbar(root)
scrollbar_horizontal.pack(side='bottom', fill='x')
'''

# Crear un frame principal
main_frame = tk.Frame(root)
main_frame.pack()
ruta_icono = "./imagenes/wh.ico"
root.iconbitmap(ruta_icono)
root.title('MASC: Multiple Analysis Software for Capacitors')

texto_copyright = "Copyright © rlucioporto.com\nLa ciencia, una luz en la oscuridad.\n   "
label_copyright = tk.Label(root, text=texto_copyright, bg="navy", fg="white", font=("Arial", 11,'bold'))
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

#Prueba
#Boton 5
about_inidicator_lb = tk.Label(options_fm)
about_inidicator_lb.place(x=525, y=30, width=80, height=2)

                   
#Segundo Boton
modelo1_btn = tk.Button(options_fm, text='Model 1', font=('Arial', 13,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo1_inidicator_lb,
                     page=modelo1_page))

modelo1_btn.place(x=125 , y=0, width=125  )

#Tercer Boton
modelo2_btn = tk.Button(options_fm, text='Model 2' , font=('Arial', 13,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo2_inidicator_lb,
                                           page=modelo2_page))

modelo2_btn.place(x=250 , y=0, width=125  )

#Cuarto Boton
modelo3 = tk.Button(options_fm, text='Model 3' , font=('Arial', 13,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo3_inidicator_lb,
                                           page=modelo3_page))

modelo3.place(x=375 , y=0, width=125  )

#Quinto Boton
modelo3_btn = tk.Button(options_fm, text='About' , font=('Arial', 13,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=about_inidicator_lb,
                                           page=about_page))

modelo3_btn.place(x=500 , y=0, width=125  )
options_fm.pack(pady=5)

#Tamaño del menu
options_fm.pack_propagate(False)
options_fm.configure(width=1400 ,height=35)

# Crear un marco para contener las imágenes
image_frame = tk.Frame(root,bg='gray87')
image_frame.pack(side=tk.TOP, fill=tk.X)

# Configurar columnas para que se expandan y centren las imágenes
image_frame.columnconfigure(0, weight=1)
image_frame.columnconfigure(1, weight=1)
image_frame.columnconfigure(2, weight=1)

# Cargar las imágenes
image_left = tk.PhotoImage(file="imagenes/uni1.png")
label_left = tk.Label(image_frame, image=image_left,bg='gray87')
label_left.grid(row=0, column=0, padx=10)

image_center = tk.PhotoImage(file="imagenes/m2.png")
label_center = tk.Label(image_frame, image=image_center,bg='gray87')
label_center.grid(row=0, column=1)

image_right = tk.PhotoImage(file="imagenes/fime2.png")
label_right = tk.Label(image_frame, image=image_right,bg='gray87')
label_right.grid(row=0, column=2, padx=10)

# Texto debajo de las imágenes
texto = "Dr. Raúl Lucio Porto\nCentro de Innovación, Investigación y Desarrollo en Ingeniería y Tecnología\nCentro de Innovación en Ingeniería de Tecnología Inteligente Biomédica y Mecatrónica"
label_texto = tk.Label(root, text=texto, justify="center",wraplength=1000, width=1400,bg="blue4", fg="white", font=("Arial", 12,'bold'))
label_texto.pack(side="top")


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
    canvas = tk.Canvas(main_fm, bg='#0097e8', highlightthickness=0)#main_fm, bg='#0097e8', highlightthickness=0
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

    V = tk.Label(frame1, text='Select one or more text files:', bg='gray84', font=('Arial', 12, 'bold'), fg='#003399', width=30)
    V.grid(column=0, row=0, pady=10, padx=20)


    # Listbox para mostrar archivos seleccionados
    file_listbox = tk.Listbox(frame1, selectmode=tk.MULTIPLE, bg='white',font=('Arial',10,'bold'), selectbackground='#0097e8', width=50, height=10)
    file_listbox.grid(column=0, row=1, pady=10, padx=20)

    # Botón para elegir archivos .txt
    btn_choose_files = tk.Button(frame1, text='📁 Select Files', bg='blue4', fg='snow', font=('Arial',12,'bold'),
                             command=lambda: choose_files(file_listbox),activeforeground='blue4')
    btn_choose_files.grid(column=0, row=2, pady=5, padx=(10,5),sticky='w')

    # Botón para eliminar archivos seleccionados
    btn_clear_files = tk.Button(frame1, text='❌ Delete Files', bg='blue4', fg='snow', font=('Arial', 12,'bold'),
                            command=lambda: clear_selected_files(file_listbox),activeforeground='blue4')
    btn_clear_files.grid(column=0, row=2, pady=5, padx=(5,10),sticky='e')

    """Velocities = tk.Label(frame1, text='Enter velocity m v⁻¹', bg='gray84', font=('Arial', 12, 'bold'), fg='#003399', width=30)
    Velocities.grid(column=0, row=3, pady=2, padx=20)

    #Buttton to velocities
    btn_velocities = Button(frame1, text='Velocites', font=('Arial', 12, 'bold'), bg='blue4', fg='white',activebackground='snow',activeforeground='blue4', command=ejecutar_velocities)
    btn_velocities.grid(row=4, column=0, columnspan=2, pady=10, padx=(10,10), sticky='ns')  # Alinea al centro"""

    # Button to download
    btn_download = Button(frame1, text='⬇ Download Files', font=('Arial', 12, 'bold'), bg='blue4', fg='white',activebackground='snow',activeforeground='blue4', command=ejecutar_descarga)
    btn_download.grid(row=5, column=0, columnspan=2, pady=10, padx=(10,10), sticky='w')  # Alinea a la derecha
    
    #Button to setiings
    btn_settings = Button(frame1, text='⚙ Settings', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activeforeground='blue4',command=ejecutar_settings)
    btn_settings.grid(row=5,column=0,columnspan=2,pady=10,padx=(10,10),sticky='e')

    """#Button to mass
    btn_mass = Button(frame1, text='Normalize by Mass', bg='blue4', fg='white', font=('Arial', 12, 'bold'), activebackground='snow',activeforeground='blue4',command=funcion_del_boton_Masa)
    btn_mass.grid(row=6,column=0,columnspan=2,pady=10,padx=(10,5),sticky='w')

    #Button to area
    btn_area = tk.Button(frame1, text='Normalize by Area', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activebackground='snow',activeforeground='blue4', command=funcion_del_boton_Area)
    btn_area.grid(row=6,column=0,columnspan=2,pady=10,padx=(10,10),sticky='e')"""

    #Button to continue
    btn_continue = tk.Button(frame1, text='➡ Continue', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activebackground='snow',activeforeground='blue4')
    btn_continue.grid(row=7,column=0,columnspan=2,pady=10,padx=(10,10),sticky='nsew')
     
    #Button to open 
    """btn_open = tk.Button(frame1, text='Open form', bg='blue4', fg='white', font=('Arial', 12, 'bold'),activebackground='snow',activeforeground='blue4')
    btn_open.grid(row=7,column=0,columnspan=2,pady=10,padx=(10,10),sticky='e')  """

    

# Etiqueta Velocidades
    #Velocidades = tk.Label(frame1, text='Speeds', bg='gray16', font=('Arial', 12, 'bold'), fg='white', width=10)
    #Velocidades.grid(column=0, row=4, pady=20, padx=10)

    # Crear el segundo frame dentro del frame interior
    frame2 = Frame(inner_frame, bg='gray64', width=900, height=7000)
    frame2.grid(column=1, row=0, sticky='nsew')


    # Agregar el código TabView al frame2
    app = TabView(frame2)


    
   

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

def about_page():
    about_page_fm = tk.Frame(main_fm)  # Cambiar el fondo del marco a gris

    about_page_lb = tk.Label(about_page_fm, text='About MASC: Multiple Analysis Software for Capacitors',
                            font=('Arial',15,'bold'), fg='#1414b8')
    about_page_lb.pack(pady=10,padx=10)

    about_text = """
    Description:
    MASC is software designed to simplify the analysis of voltage and current intensity data on specific materials, such as supercapacitors. It uses CSV files as input to calculate  
    key electrical and electrochemical properties using specialized techniques.

    Objectives:
    -Provide an intuitive and accessible tool for materials analysis in laboratory or office environments. MASC features an easy-to-use graphical interface implemented in Python.
   - Facilitate a variety of calculations, including interpolation and oxidation-reduction, through a simple and aesthetically pleasing graphical interface.
    
    Background:
    Based on previous research on energy storage in supercapacitors, MASC offers an efficient solution for data analysis in this growing field.
    
    Problem:
    Lack of specialized software hinders accurate data analysis in supercapacitor research laboratories, especially for non-programming users.
    
    Rationale:
    MASC seeks to improve accuracy and efficiency in data analysis by filling the gap in intuitive, specialized software.
    
    Limitations:
    Requires a device with a Pentium processor and basic knowledge in materials for effective use.

    Scope:
    Initially targeted at the supercapacitor research lab at CIIDIT, future versions are expected to be accessible to users with varying levels of experience.
    
    Benefits:
    - Multiplatform: Compatible with various operating systems.
    - Simplified management: Graphical interface that facilitates file selection and calculations.
    - Easy to use: Accessible even to users with no programming experience.
    """

    about_text_txt = tk.Text(about_page_fm, wrap="word")
    about_text_txt.insert(tk.END, about_text)
    about_text_txt.config(state="disabled", font=("Arial", 12), bg="gray84", fg="black")
    about_text_txt.pack(expand=True, fill="both", padx=20, pady=20)

    about_page_fm.pack(fill=tk.BOTH, expand=True)

main_fm = tk.Frame(root, bg='gray84')  # Cambiar el fondo del marco principal a gris
main_fm.pack(fill=tk.BOTH, expand=True)

home_page()

root.mainloop()