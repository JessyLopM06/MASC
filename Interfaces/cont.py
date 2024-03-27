"""import tkinter as tk
from customtkinter import CTk, CTkTabview
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

class TabView:
    def __init__(self, root) -> None:
        self.root = root
        self.TabTree = CTkTabview(root, state=tk.DISABLED, fg_color='#1D3F60')
        self.TabTree.grid(row=2, column=3, rowspan=8, columnspan=7, sticky='nswe')
        self.TabTree.add('Interpolation')  ## EJES J/cm-2 or J/g^-1 Normalizated vortagram
        self.TabTree.add('Obtaining of K')  ## Y m*V^1/2 miliamper mA*Vs-1/2 X   ##OBTENCION DE K
        self.TabTree.add('VOLTAMPEROGRAM')  ## VOLTAMPEROGRAMS ESTIMADA VOLTAPEROGRAM
        self.TabTree.add('Total Q')  ##  TOTAL 
        self.TabTree.add('Q%')  ## Q%   
        self.TabTree.add('MASOGRAMA')  ## MASOGRAM 
        self.TabTree.add('ACTIVE THICKNESS')  ## ACTIVE THICKNESS
        self.TabTree.add('Barras 2')  ## ACTIVE THICKNESS

        # Diccionario para almacenar los marcos asociados a cada pestaña
        self.tab_frames = {}

        for tab_name in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            frame = tk.Frame(self.root)
            self.tab_frames[tab_name] = frame
            self.TabTree.tab(tab_name, slave=frame)

        # Crear el gráfico de voltamperograma en la pestaña correspondiente
        self.create_voltamperogram_plot()

    def create_voltamperogram_plot(self):
        frame = self.tab_frames['VOLTAMPEROGRAM']
        fig, ax = plt.subplots()
        current = np.linspace(0, 1, 100)
        voltage = np.sin(2 * np.pi * current)
        ax.plot(current, voltage)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Crear la aplicación principal
root = CTk()
app = TabView(root)

# Ejecutar el bucle de eventos
root.mainloop()
"""


"""import tkinter as tk
from customtkinter import CTk, CTkTabview

class TabView:
    def __init__(self, root) -> None:
        self.root = root
        self.TabTree = CTkTabview(root, state=tk.DISABLED, fg_color='#1D3F60')
        self.TabTree.grid(row=2, column=3, rowspan=8, columnspan=7, sticky='nswe')
        self.TabTree.add('Interpolation')  ## EJES J/cm-2 or J/g^-1 Normalizated vortagram
        self.TabTree.add('Obtaining of K')  ## Y m*V^1/2 miliamper mA*Vs-1/2 X   ##OBTENCION DE K
        self.TabTree.add('VOLTAMPEROGRAM')  ## VOLTAMPEROGRAMS ESTIMADA VOLTAPEROGRAM
        self.TabTree.add('Total Q')  ##  TOTAL 
        self.TabTree.add('Q%')  ## Q%   
        self.TabTree.add('MASOGRAMA')  ## MASOGRAM 
        self.TabTree.add('ACTIVE THICKNESS')  ## ACTIVE THICKNESS
        self.TabTree.add('Barras 2')  ## ACTIVE THICKNESS

        # Diccionario para almacenar los marcos asociados a cada pestaña
        self.tab_frames = {}

        for tab_name in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            frame = tk.Frame(self.TabTree.tab(tab_name), bg='blue', padx=10, pady=10)  # Añadimos color y relleno para visualización
            self.tab_frames[tab_name] = frame

# Crear la aplicación principal
root = CTk()
app = TabView(root)

# Ejecutar el bucle de eventos
root.mainloop()
"""




"""import tkinter as tk
from customtkinter import CTk, CTkTabview

class TabView:
    def __init__(self, root) -> None:
        self.root = root
        self.TabTree = CTkTabview(root, fg_color='#003399')
        self.TabTree.grid(row=2, column=3, rowspan=8, columnspan=7, sticky='nswe')

        for tab_name in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            self.TabTree.add(tab_name)

# Crear la aplicación principal
root = CTk()
app = TabView(root)

# Ejecutar el bucle de eventos
root.mainloop()"""


"""
import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import CTk, CTkTabview




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

# Crear la aplicación principal
root = CTk()
app = TabView(root)



# Ejecutar el bucle de eventos
root.mainloop()
"""





import tkinter as tk
from customtkinter import CTk, CTkTabview

class TabViewWithColoredMargin:
    def __init__(self, root) -> None:
        self.root = root

        # Creamos un Frame adicional para el margen con color personalizado
        self.margin_frame = tk.Frame(root, padx=10, pady=10, bg='#003399')  # Cambia 'blue' por el color que desees
        self.margin_frame.pack()

        # Creamos el TabView dentro del Frame con margen
        self.tabview = CTkTabview(self.margin_frame, fg_color='silver')
        self.tabview.pack()

        # Agregamos las pestañas al TabView
        for tab_name in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            self.tabview.add(tab_name)

# Creamos la aplicación principal
root = CTk()
geometry(root,'1000x1000')
app = TabViewWithColoredMargin(root)

# Ejecutamos el bucle de eventos
root.mainloop()
