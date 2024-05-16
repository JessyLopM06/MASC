"""
Este módulo proporciona una interfaz de para que el usario descargue sus archivos 
utilizando tkinter.
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd

class DownloadFiles(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Download Files")
        self.resizable(False, False)
        self.parent = parent
        self.list_of_checkboxes = list()
        self.checkboxes = ['Interpolation', 'K₁ y K₂', 'VOLTAMPEROGRAM',
            'Total Q', 'Q%', 'MASSOGRAM', 'ACTIVE THICKNESS']
        self.list_of_checks = list()
        self.path = ''

        # Frame que contiene información
        self.frame_info = tk.Frame(self, bg='#003399')
        self.frame_info.grid_rowconfigure(0, weight=1)
        self.frame_info.grid_columnconfigure(0, weight=1)
        self.frame_info.grid(sticky='nswe', padx=20, pady=20)

# Checkbox para seleccionar los archivos dentro de frame_info
        for i in range(len(self.checkboxes)):
            if i % 2 == 0:
                actual_checkbox = tk.Checkbutton(self.frame_info, text=self.checkboxes[i],
                    variable=tk.BooleanVar(), fg='black', selectcolor='gray84',font=('Arial',12))
                actual_checkbox.grid(row=i, column=0, sticky='nswe', padx=20, pady=10)
                self.list_of_checkboxes.append(actual_checkbox)
            else:
                actual_checkbox = tk.Checkbutton(self.frame_info, text=self.checkboxes[i], variable=tk.BooleanVar(), fg='black', selectcolor='gray84',font=('Arial',12))
                actual_checkbox.grid(row=i-1, column=1, sticky='nswe', padx=20, pady=10)
                self.list_of_checkboxes.append(actual_checkbox)

        # Botón para seleccionar la carpeta donde se guardarán los archivos
        self.btn_select_folder = tk.Button(self, text='📁 Select Folder', bg='blue4',
                font=('Arial',12,'bold'),fg='white', command=lambda: self.select_folder())
        self.btn_select_folder.grid(row=1, column=0, sticky='nswe', padx=10, pady=10)

        # Botón para cancelar la selección de archivos
        self.btn_cancel = tk.Button(self, text='❌ Cancel', bg='blue4',
            font=('Arial',12,'bold'),fg='white', command=lambda: self.destroy())
        self.btn_cancel.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
        
        # Botón para aceptar los archivos seleccionados
        self.btn_accept = tk.Button(self, text='✔ Accept', bg='blue4',
            font=('Arial',12,'bold'), fg='white', command=lambda: self.handler_submit())
        self.btn_accept.grid(row=2, column=1, sticky='nswe', padx=10, pady=10)

    def select_folder(self):
        """
        Selecciona la carpeta donde se guardarán los archivos
        """
        self.path = fd.askdirectory(initialdir='/', title='Select Folder')
        print(self.path)

    def handler_submit(self):
        if self.path:
            for checkbox in self.list_of_checkboxes:
                self.list_of_checks.append(checkbox.var.get())

            self.parent.download_files_path = self.path
            self.parent.list_of_checks = self.list_of_checks
            print('FROM DOWNLOAD FILES TOP LEVEL')
            print(self.parent.download_files_path)
            print(self.parent.list_of_checks)
            print(self.parent)
            print(self.list_of_checks)
        else:
            messagebox.showinfo('Error', 'Select a folder')

# Uso de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    DownloadFiles(root)
    root.mainloop()
