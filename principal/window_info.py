from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def info():
    i = Toplevel()
    class Informacion():
        def __init__(self,opcion_3):
            self.op_3 = opcion_3
            self.op_3.config(bg="white")
            self.op_3.title("INFORMACIÓN PROGRAMA")
            self.g = PhotoImage(file="Src/imag/Información programa.png")
            self.im_g=Label(self.op_3 , image= self.g)
            self.im_g.pack(expand=1)

            

    info = Informacion(i)
    i.mainloop()