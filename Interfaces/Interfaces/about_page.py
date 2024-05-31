import tkinter as tk

def about_page():
    global image_left, image_center, image_right  # Hacer las variables de imagen globales
    about_page_fm = tk.Frame(main_fm, bg='gray84')  # Cambiar el fondo del marco a gris
    about_page_fm.pack(fill=tk.BOTH, expand=True)

    about_page_lb = tk.Label(about_page_fm, text='About MASSC: Multiple Analyses Software for Supercapacitors',
                             font=('Arial', 15, 'bold'), fg='#1414b8', bg='gray84')
    about_page_lb.pack(pady=10, padx=10)

    # Crear un marco para contener las imágenes
    image_frame = tk.Frame(about_page_fm, bg='gray84')
    image_frame.pack(side=tk.TOP, fill=tk.X)

    # Configurar columnas para que se expandan y centren las imágenes
    image_frame.columnconfigure(0, weight=1)
    image_frame.columnconfigure(1, weight=1)
    image_frame.columnconfigure(2, weight=1)

    # Cargar las imágenes
    image_left = tk.PhotoImage(file="imagenes/uniM.png")
    label_left = tk.Label(image_frame, image=image_left, bg='gray84')
    label_left.grid(row=0, column=0, padx=10)

    image_center = tk.PhotoImage(file="imagenes/logM1.png")  # m2ph
    label_center = tk.Label(image_frame, image=image_center, bg='gray84')
    label_center.grid(row=0, column=1)

    image_right = tk.PhotoImage(file="imagenes/92.png")
    label_right = tk.Label(image_frame, image=image_right, bg='gray84')
    label_right.grid(row=0, column=2, padx=10)

    texto_copyright = "Copyright © rlucioporto.com\nLa ciencia, una luz en la oscuridad.\n   "
    label_copyright = tk.Label(about_page_fm, text=texto_copyright, bg="navy", fg="white", font=("Arial", 8, 'bold'))
    label_copyright.pack(side="bottom", fill="both")

    # Texto debajo de las imágenes
    texto = "Dr. Raúl Lucio Porto\nCentro de Innovación, Investigación y Desarrollo en Ingeniería y Tecnología\nCentro de Innovación en Ingeniería de Tecnología Inteligente Biomédica y Mecatrónica\n"
    label_texto = tk.Label(about_page_fm, text=texto, justify="center", wraplength=1000, bg="blue4", fg="white", font=("Arial", 9, 'bold'))
    label_texto.pack(fill="both", expand=True, padx=10, pady=10)

    about_text = (
        "Welcome to MASSC (Multiple Analyses Software for Supercapacitors), the ultimate software solution for advanced "
        "electrochemical analysis of supercapacitors. Designed with researchers and engineers in mind, our platform offers "
        "a comprehensive suite of tools for conducting cyclic voltammetry, galvanostatic charge-discharge, chronoamperometry, "
        "electrochemical impedance spectroscopy analyses, and more. With intuitive data visualization, robust analytical "
        "capabilities, and seamless integration with your laboratory equipment, MASSC empowers you to gain deeper insights "
        "into the performance and optimization of supercapacitors. Join a community of innovators who are pushing the boundaries "
        "of energy storage technology with the precision and reliability that only MASSC can provide.\n\n"
        "MASSC was designed in the Facultad de Ingeniería Mecánica y Eléctrica from the Universidad Autónoma de Nuevo León. "
        "If you are going to use MASSC, please cite the following two scientific articles.\n\n"
        "◾Layered Vanadium Phosphates as Electrodes for Electrochemical Capacitors Part I: The Case of VOPO₄·2H₂O. Journal of "
        "The Electrochemical Society, 2021, 168, 070531.DOI 10.1149/1945-7111/ac11a3.\n"
        "◾Layered Vanadium Phosphates as Electrodes for Electrochemical Capacitors Part II: The Case of VOPO₄·CTAB and "
        "K₀.₅VOPO₄·1.5H₂O. Journal of The Electrochemical Society, 2021, 168, 090520.DOI 10.1149/1945-7111/ac23a0."
    )
    about_text_txt = tk.Text(about_page_fm, wrap="word")
    about_text_txt.insert(tk.END, about_text)
    about_text_txt.config(state="disabled", font=("Arial", 12), bg="gray84", fg="black")
    about_text_txt.pack(expand=True, fill="both", padx=60, pady=10)
    
    about_page_fm.pack(fill=tk.BOTH, expand=True)

# Crear la ventana principal de Tkinter
root = tk.Tk()

ruta_icono = "./imagenes/wh.ico"
root.iconbitmap(ruta_icono)

root.title("MASSC - About Page")

# Crear el marco principal
main_fm = tk.Frame(root, bg='gray84')  # Cambiar el fondo del marco principal a gris
main_fm.pack(fill=tk.BOTH, expand=True)

# Llamar a la función para mostrar la página "About"
about_page()

# Iniciar el bucle principal de Tkinter
root.mainloop()
