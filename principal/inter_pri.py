from tkinter import *

def principal(self):
    self.nombre = StringVar()
    self.etiqueta_nom = Label(self.frame, text="Nombre",)
    self.etiqueta_nom.grid(row= 1, column=1)

    self.entrada_nom= Entry(self.frame, textvariable= self.nombre)
    self.entrada_nom.grid(row= 1, column=2)