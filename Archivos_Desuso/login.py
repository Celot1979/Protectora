from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  csv
import sqlite3
from datetime import date
from datetime import datetime
from tkinter import *
from tkcalendar import Calendar

#Crear usario y logear con conexionBBDD
########################################################################################################################################################################################################
#################################### CREACION DE BBDD PARA REGISTROS OPERARIOS ###########################################################################################################################################
########################################################################################################################################################################################################
#CONEXIÓN BBDD
def conexionBBDD_usuario():
    miConexion = sqlite3.connect("Nuevo_Registro.db")
    miCursor= miConexion.cursor()
    try:
        miCursor.execute("""CREATE TABLE nuevo(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL, 
        PASSWORD VARCHAR(50) NOT NULL)""")
        messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")
    except:
        messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")
#Creacion de la BBDD
def crear():
    miConexion = sqlite3.connect("Nuevo_Registro.db")
    miCursor= miConexion.cursor()
    try:
        datos = nombre.get(), Contrasena.get()
        miCursor.execute("INSERT INTO nuevo VALUES(NULL,?,?)", (datos))
        miConexion.commit()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
    limpiarCampos_registro()
#REGISTRO DE EL NUEVO OPERARIO
def registrar_nuevo():
    conexionBBDD_usuario()
    crear()
    messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")
    

#SI EL USUARIO ES CORRECTO. COMIENZA SESIÓN   
def inicio_usario():
    miConexion = sqlite3.connect("Nuevo_Registro.db")
    miCursor= miConexion.cursor()
    usuario = nombreE.get()
    contr= PasswordE.get()
    miCursor.execute('SELECT * FROM nuevo WHERE  nombre= ? AND password = ?', (usuario, contr))
    if miCursor.fetchall():
        messagebox.showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
        segunda_ventana()
    else:
        messagebox.showerror(title = "LOGIN INCORRECTO", message = "VUELVA A ESCRIBIR USUARIO Y CONTRASEÑA")
        borrar()
    miCursor.close()

    
        
    
    

####################################################################################################
####################################################################################################
####################################################################################################