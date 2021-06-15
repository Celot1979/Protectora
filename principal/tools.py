from tkinter import *

def perro(self, dire):
    file = dire
    self.imagen = PhotoImage(file="")
    self.Imagen2= Label(self.frame_dos, image=self.imagen)
    self.Imagen2.grid(row=4,columnspan=6)


"""self.imagen = PhotoImage(file="src/imag/Perro 2.png")
self.Imagen2= Label(self.frame_dos, image=self.imagen)
self.Imagen2.grid(row=4,columnspan=6)"""


"""m_g = Label(self.frame_tres,text="Escoja su elección").place(x=1,y=1)
            self.comboExample = ttk.Combobox(self.frame_tres ,values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
            self.comboExample.title="Opciones"
            self.comboExample.place(x=1,y=50)"""