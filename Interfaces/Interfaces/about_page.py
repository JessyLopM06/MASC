import tkinter as tk

def about_page(root):
    about_page_fm = tk.Frame(root)
    
    about_page_lb = tk.Label(about_page_fm, text='About', font=('Arial', 18, 'bold'), fg='#1414b8')
    about_page_lb.pack(pady=20)
    
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

# Crear la ventana principal
root = tk.Tk()
root.title("About Page")

root.geometry("800x600")

# Llamar a la función para mostrar la página "About"
about_page(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()
