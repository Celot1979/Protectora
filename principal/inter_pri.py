
from bbdd import *
from tkinter import *

import psycopg2


"""Creación de un frame para poder ubicar mejor los elementos de la ventana principal.
En principio la libreria Tkinter nos da la posibilidad de colocar dicho Frame encima de la root y colocar elementos.
Probado en W10 y Mac funciona a la perfección. """
def principal(self):
    self.nombre = StringVar()
    self.contrasena = StringVar()

    self.etiqueta_nom = Label(self.frame, text="NOMBRE")
    self.etiqueta_nom.grid(row= 1, column=2)
    self.etiqueta_con = Label(self.frame, text="CONTRASEÑA")
    self.etiqueta_con.grid(row= 2, column=2)

    self.entrada_nom= Entry(self.frame, textvariable= self.nombre,width=20)
    self.entrada_nom.grid(row= 1, column=3)
    self.entrada_con= Entry(self.frame, textvariable= self.contrasena,width=20)
    self.entrada_con.grid(row= 2,column=3)
    
    def registrar(self):
        self.imprimir ="ME caguen to"
        print(self.imprimir)
        cagada(self)
        crear_tabla()


    self.boton1 = Button(self.frame, text="CONECTAR")
    self.boton1.grid(row=3,column=1, padx= 10, pady= 30)
    self.boton2 = Button(self.frame, text="SALIR")
    self.boton2.grid(row=3,column=2, padx= 10, pady= 30)
    self.boton3 = Button(self.frame, text="REGISTRAR",command=lambda:registrar(self))
    self.boton3.grid(row=3,column=3, padx= 10, pady= 30)
    self.boton4 = Button(self.frame, text="BORRAR")
    self.boton4.grid(row=3,column=4, padx= 10, pady= 30)

    self.imagen = PhotoImage(file="Src/imag/Proctetora.png")
    self.Imagen2= Label(self.frame, image=self.imagen)
    self.Imagen2.grid(row=4,columnspan=6)


    self.etiqueta_nom = Label(self.frame, text="Aplicación creada con python - Tkinter")
    self.etiqueta_nom.grid(row= 5, columnspan=5)
    self.etiqueta_nom.config(justify="center")

