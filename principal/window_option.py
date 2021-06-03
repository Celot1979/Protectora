from tkinter import Tk
from tkinter import *
"""La finalidad de este archivo es organizar los botones de una segunda ventana que contenga los botones 
para elegir que opción interesa más al usuario"""
def opciones_protectora():
    r = Tk()
    class Opciones():
        def __init__(self,opcion):
            self.opcion = opcion
            self.opcion.title("REGISTROS EN PALEVLAS ")
            self.frame_dos = Frame(self.opcion)
            self.frame_dos.place(x =50 , y = 50)
            self.frame_dos.config(bg="lightblue",width= 800, height= 600)
            

        

    op = Opciones(r)
    
    r.mainloop()   