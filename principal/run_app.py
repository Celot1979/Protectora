from tkinter import *
from window_user import *

from tkinter import messagebox
raiz = Tk()


class Protectora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("BIENVENIDO A PALEVLAS ")
        self.ventana.attributes('-fullscreen', True)#Apertura en ventana completa
        self.frame = Frame(self.ventana)
        
        self.frame.pack(expand=1)
        #self.frame.config(bg="lightblue")
        self.frame.config(width=1200, height=5000)
        self.frame = principal(self)
        


Proyecto = Protectora(raiz)
raiz.mainloop()
