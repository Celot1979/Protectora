from tkinter import *
"""Creación de un frame para poder ubicar mejor los elementos de la ventana principal """
def principal(self):
    self.nombre = StringVar()
    self.contrasena = StringVar()

    self.etiqueta_nom = Label(self.frame, text="NOMBRE")
    self.etiqueta_nom.grid(row= 1, column=1)
    self.etiqueta_con = Label(self.frame, text="CONTRASEÑA")
    self.etiqueta_con.grid(row= 2, column=1)

    self.entrada_nom= Entry(self.frame, textvariable= self.nombre)
    self.entrada_nom.grid(row= 1, column=2)
    self.entrada_con= Entry(self.frame, textvariable= self.contrasena)
    self.entrada_con.grid(row= 2,column=2)

    self.boton1 = Button(self.frame, text="CONECTAR")
    self.boton1.grid(row=3,column=1, padx= 10, pady= 10)
    self.boton2 = Button(self.frame, text="SALIR")
    self.boton2.grid(row=3,column=2)
    self.boton3 = Button(self.frame, text="REGISTRAR")
    self.boton3.grid(row=3,column=3)

    self.imagen = PhotoImage(file="Src/imag/Proctetora.png")
    self.Imagen2= Label(self.frame, image=self.imagen)
    self.Imagen2.grid(row=4,columnspan=5)

