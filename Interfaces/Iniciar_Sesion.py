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
        self.geometry("450x550+10+10")
        color = '#2c277a'
        self['bg'] = color

        lblframe_login = LabelFrame(master=self, text='Access', font=('Arial', 14, 'bold'), fg='snow', bg='#003399', padx=20, pady=20, borderwidth=10, highlightbackground='blue4')
        lblframe_login.pack(expand=True, fill=BOTH, padx=55, pady=50)

        lbltitulo = Label(master=lblframe_login, text='Login', font=('Arial', 18, 'bold'), fg='snow', bg='#003399')
        lbltitulo.grid(row=0, column=0, padx=5 , pady=5, columnspan=2)

        imagen = Image.open("imagenes/m2.png")
        imagen = imagen.resize((180, 180))
        photoImg = ImageTk.PhotoImage(imagen)
        panel = Label(master=lblframe_login, image=photoImg, bg='#003399')
        panel.image = photoImg
        panel.grid(row=1, column=0, columnspan=2, pady=10)

        lbl_usuario = Label(master=lblframe_login, text='User : ', font=('Arial', 12, 'bold'), fg='snow', bg='#003399')
        lbl_usuario.grid(row=2, column=0, padx=5, pady=5)

        self.ent_usuario = ttk.Entry(master=lblframe_login, width=15, justify=CENTER, font=('Arial',12,'bold'))
        self.ent_usuario.grid(row=2, column=1, padx=5, pady=5)

        lbl_clave = Label(master=lblframe_login, text='Password :  ', font=('Arial', 12, 'bold'), fg='snow', bg='#003399')
        lbl_clave.grid(row=3, column=0, padx=5, pady=5)

        self.ent_clave = ttk.Entry(master=lblframe_login, width=15, justify=CENTER, show='*', font=('Arial',12,'bold'))
        self.ent_clave.grid(row=3, column=1, padx=5, pady=5)
        

        self.btn_acceso = ttk.Button(master=lblframe_login,text='Enter', style='TButton', command=self.login)
        self.btn_acceso.grid(row=4, column=0, columnspan=2, pady=30, padx=50)

       

        style = ttk.Style()
        style.configure('Custom.TButton', font=('Arial', 15, 'bold'))
        self.btn_acceso = ttk.Button(master=lblframe_login, text='Enter', style='Custom.TButton', command=self.login)
        self.btn_acceso.grid(row=4, column=0, columnspan=2, pady=30, padx=50)

    def login(self):
        usuario = self.ent_usuario.get()
        contr = self.ent_clave.get()
        if usuario == "GENANO" and contr == "CIDIIT":
            messagebox.showinfo(title="Correct Login", message="Successful login!")
            try:
                subprocess.Popen(['python', 'modern.py'])
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Could not open modern.py {e}")
        else:
            messagebox.showerror(title="Incorrect login", message="Incorrect username or password!")

def main():
    app = Ventana()
    ruta_icono = "./imagenes/Login.ico"
    app.iconbitmap(ruta_icono)
    app.title('Login')
    app.mainloop()

if __name__=='__main__':
    main()
