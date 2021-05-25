from tkinter import *
import os
"""Se tratan las imágenes que se irán usando a lo largo del programa. Se usa los condicionales 
para que la app sepa diferenciar entre sistemas operativos """
def Logo(self,ima):
    if os.name =="nt":
        self.ventana = ima
        self.Logo = PhotoImage(file="Src\Proctetora.png")
        self.Logo_2 =Label(self.ventana, image= self.Logo)
        self.Logo_2.place(x=550, y=220)
    else:
        self.Logo = PhotoImage(file="Src/Proctetora.png")
        self.Logo_2 =Label(self.ventana, image= self.Logo)
        self.Logo_2.place(x=550, y=220)

