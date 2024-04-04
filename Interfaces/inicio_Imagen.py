"""
Este módulo proporciona una interfaz del inicio de sesion utilizando tkinter.
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image

class Ventana(Tk):
    def __init__(self):
        super().__init__()
        self.ventana_login()
    def ventana_login(self):
        self.geometry("2000x2000")
        # Frame para todo el contenido
        frame_contenido = Frame(self, bg='#003399')
        frame_contenido.pack(fill=BOTH, expand=True)
         # Etiqueta como título
        lbl_titulo = Label(frame_contenido, text=" LOGIN ", font=('Arial', 20, 'bold'),
            fg='snow', bg='#003399')
        lbl_titulo.pack(pady=(50,10))
        # Frame izquierdo para la imagen
        frame_izquierdo = Frame(frame_contenido, bg='#003399')
        frame_izquierdo.pack(side=LEFT, fill=Y)

        # Cargar imagen
        imagen = PhotoImage(file="imagenes/inicio.png")  # Ruta de tu imagen
        lbl_imagen = Label(frame_izquierdo, image=imagen, bg='#003399')
        lbl_imagen.image = imagen  # ¡Importante! Para evitar que la imagen se borre
        lbl_imagen.pack(pady=50, padx=100)

        # Frame derecho para el contenido de acceso
        frame_derecho = Frame(frame_contenido, bg='#003399')
        frame_derecho.pack(side=RIGHT, fill=BOTH, expand=True)
        lblframe_login = LabelFrame(master=frame_derecho, text='Access',
            font=('Arial', 20, 'bold'), fg='snow', bg='#003399', padx=20, pady=20,
            borderwidth=10, highlightbackground='blue4')
        lblframe_login.pack(fill=BOTH, padx=80, pady=(100,100))

        lbl_usuario = Label(master=lblframe_login, text='👤 User : ',
            font=('Arial', 15, 'bold'), fg='snow', bg='#003399')
        lbl_usuario.grid(row=2, column=0, padx=5, pady=10)

        self.ent_usuario = ttk.Entry(master=lblframe_login, width=15,
            justify=CENTER, font=('Arial',15,'bold'))
        self.ent_usuario.grid(row=2, column=1, padx=5, pady=10)

        lbl_clave = Label(master=lblframe_login, text='🔑 Password :  ', 
            font=('Arial', 15, 'bold'), fg='snow', bg='#003399')
        lbl_clave.grid(row=3, column=0, padx=5, pady=15)

        self.ent_clave = ttk.Entry(master=lblframe_login, width=15, justify=CENTER, 
            show='*', font=('Arial',15,'bold'))
        self.ent_clave.grid(row=3, column=1, padx=5, pady=5)

        self.btn_acceso = ttk.Button(master=lblframe_login,text='Enter', style='TButton',
            command=self.login)
        self.btn_acceso.grid(row=4, column=0, columnspan=2, pady=30, padx=50)

        style = ttk.Style()
        style.configure('Custom.TButton', font=('Arial', 15, 'bold'))
        self.btn_acceso = ttk.Button(master=lblframe_login, text='Enter',
            style='Custom.TButton', command=self.login)
        self.btn_acceso.grid(row=4, column=0, columnspan=2, pady=30, padx=50)

    def login(self):
        usuario = self.ent_usuario.get()
        contr = self.ent_clave.get()
        if usuario == "GENANO" and contr == "CIDIIT":
            messagebox.showinfo(title="Correct Login", message="Successful login!")
            try:
                subprocess.Popen(['python', 'Interfaces/modern.py'])
            except Exception as e:
                messagebox.showerror(title="Error",
                    message=f"Could not open modern.py {e}")
        else:
            messagebox.showerror(title="Incorrect login",
                message="Incorrect username or password!")
def main():
    app = Ventana()
    ruta_icono = "./imagenes/Login.ico"
    app.iconbitmap(ruta_icono)
    app.title('Login')
    app.mainloop()

if __name__ == '__main__':
    main()
