from bbdd import *
from tkinter import *
from tkinter import messagebox

import psycopg2


def principal(self):
    self.nombre = StringVar()
    self.contrasena = StringVar()

    self.etiqueta_nom = Label(self.frame, text="NOMBRE")
    self.etiqueta_nom.grid(row=1, column=2)
    self.etiqueta_con = Label(self.frame, text="CONTRASEÑA")
    self.etiqueta_con.grid(row=2, column=2)

    self.entrada_nom = Entry(self.frame, textvariable=self.nombre, width=20)
    self.entrada_nom.grid(row=1, column=3)
    self.entrada_con = Entry(self.frame, textvariable=self.contrasena, width=20)
    self.entrada_con.grid(row=2, column=3)

    def registrar(self):
        registro_usuario(self.nombre.get(), self.contrasena.get())

    def conectar(self):
        conectar_usuario(self.nombre.get(), self.contrasena.get())

    def borrar(self):
        self.nombre.set(" ")
        self.contrasena.set(" ")

    def salir(self):
        self.ventana.destroy()

    self.boton1 = Button(self.frame, text="CONECTAR", command=lambda: conectar(self))
    self.boton1.grid(row=3, column=1, padx=10, pady=30)
    self.boton2 = Button(self.frame, text="SALIR", command=lambda: salir(self))
    self.boton2.grid(row=3, column=2, padx=10, pady=30)
    self.boton3 = Button(self.frame, text="REGISTRAR", command=lambda: registrar(self))
    self.boton3.grid(row=3, column=3, padx=10, pady=30)
    self.boton4 = Button(self.frame, text="BORRAR", command=lambda: borrar(self))
    self.boton4.grid(row=3, column=4, padx=10, pady=30)

    self.imagen = PhotoImage(file="Src/imag/Proctetora.png")
    self.Imagen2 = Label(self.frame, image=self.imagen)
    self.Imagen2.grid(row=4, columnspan=6)

    self.etiqueta_nom = Label(self.frame, text="Aplicación creada con python - Tkinter")
    self.etiqueta_nom.grid(row=5, columnspan=5)
    self.etiqueta_nom.config(justify="center")