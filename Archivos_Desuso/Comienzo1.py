from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from segunda_ventana2 import*
from perro3 import*

#***************************************** VENTANA PRINCIPAL  ******************************************************************************************
#****************************************  PANTALLA PRINCIPAL ******************************************************************************************
#********************************************************************************************************************************************************************
root= Tk()
root.geometry("5000x5000")
root.title("PALEVLAS")
#***************************************** IMAGEN CENTRAL DE LA PROTECTORA ******************************************************************************************
#********************************************************************************************************************************************************************
imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Proctetora.png")
Imagen_2 =Label(root, image=imagen)
Imagen_2.place(x=650, y=220)
#***************************************** ETIQUETAS-CUADROS DE TEXTO-VARIABLES  ******************************************************************************************
#********************************************* PANTALLA PRINCIPAL ******************************************************************************************
#********************************************************************************************************************************************************************
#Variables para pantalla principal
nombre=StringVar()
Contrasena = StringVar()
#Etiquetas pantalla principal************************************
nombreL= Label(root,text="NOMBRE",  background="azure",font=("Monaco",18))
nombreL.place(x=800, y= 80)

PasswordL= Label(root,text="CONTRASEÑA",  background="azure",font=("Monaco",18))
PasswordL.place(x=800, y= 140)
#Caja de texto pantalla principal************************************
nombreE=Entry(root, width= 20, textvariable=nombre,background="azure")
nombreE.place(x=1000, y= 78)

PasswordE=Entry(root, width= 20, textvariable=Contrasena,background="azure")
PasswordE.place(x=1000, y= 138)

Derechos = Label(root, text="Este programa pertenece a la protectora recibiendo los derechos del desarollador Daniel Gil", background="azure",font=("Monaco",10))
Derechos.place(x=750, y = 900)
#Funciones para la pantalla principal************************************
def conectar():
    if nombreE.get() == "Dani" and PasswordE.get() == "1":
        segunda_ventana(root)
    else:
        print("Error")
def borrar():
    nombreE.delete(0,END)
    PasswordE.delete(0,END)
def salir():
    root.destroy()

#Botones pantalla principal************************************
#Aceptar******
conecto = Button(root, text="Conectar", width= 8, background="blue", activebackground="blue", command=conectar)
conecto.place(x=800, y=200)
conecto.config(overrelief=GROOVE, relief=FLAT)
#Borrar*****
borrar= Button(root, text="BORRAR", width= 8, background="blue", activebackground="blue", command=borrar)
borrar.place(x=1000, y=200)
borrar.config(overrelief=GROOVE, relief=FLAT)
#Salir*****
salir= Button(root, text="SALIR", width= 8, background="blue", activebackground="blue", command=salir)
salir.place(x=1200, y=200)
salir.config(overrelief=GROOVE, relief=FLAT)
#***************************************** VENTANA DE OPCIONES  ******************************************************************************************
#************************************** SEGUNDA PANTALLA PRINCIPAL ******************************************************************************************
#********************************************************************************************************************************************************************

















root.mainloop()