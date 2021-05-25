from tkinter import *
import sqlite3
from tkinter import messagebox
from segunda_ventana.segunda import ventana_opcion_uno

"""En este archivo sirve para crear al espacio de trabajo de la pantalla de acceso."
1º Se encontrará la configuración de Tkinter con sus etiquetas, entradas de texto y botones. 
2º Funciones de ejecución de los botones creados anteriormente
3º La implementación de las funcionalidades y validaciones para crear una BBDD, crear un usasio y convalidarlo para acceder 
a la aplicación """

def campos(self):
    self.nombre = StringVar()
    self.contrasena = StringVar()

    self.nombreL =Label(self.ventana, text="Nombre")
    self.nombreL.place(x=800, y= 80)

    self.ContraL =Label(self.ventana, text="Contraseña")
    self.ContraL.place(x=800, y= 140)

    self.nombreE = Entry(self.ventana, textvariable=self.nombre)
    self.nombreE.place(x=1000, y= 78)

    self.ContraE = Entry(self.ventana, textvariable= self.contrasena, show= "*")
    self.ContraE.place(x=1000, y= 138)

def limpiarCampos_registro(self):
    self.nombre.set()
    self.contrasena.set()

def conectar_inicio():
    print("Hola")

def borrar(self):
    self.nombreE.delete(0,END)
    self.ContraE.delete(0,END)

def salir(self):
    self.ventana.destroy()

#Crear usario y logear con conexionBBDD
########################################################################################################################################################################################################
#################################### CREACION DE BBDD PARA REGISTROS OPERARIOS ###########################################################################################################################################
########################################################################################################################################################################################################
#CONEXIÓN BBDD
def conexionBBDD_usuario(self):
    self.miConexion = sqlite3.connect("Nuevo_Registro.db")
    self.miCursor= self.miConexion.cursor()
    try:
        self.miCursor.execute("""CREATE TABLE nuevo(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL, 
        PASSWORD VARCHAR(50) NOT NULL)""")
        messagebox.showinfo("1º Paso", "CREADA LA BBDD")
    except:
        messagebox.showinfo("1º Paso", " NO CREADA LA BBDD")

def crear(self):
    self.miConexion = sqlite3.connect("Nuevo_Registro.db")
    self.miCursor= self.miConexion.cursor()
    try:
        self.datos = self.nombre.get(), self.contrasena.get()
        self.miCursor.execute("INSERT INTO nuevo VALUES(NULL,?,?)", (self.datos))
        self.miConexion.commit()
    except:
        messagebox.showinfo("2º paso", "PROBLEMA EN LA FUNCIÓN CREAR")
    limpiarCampos_registro(self)
    
#REGISTRO DE EL NUEVO OPERARIO
def registrar_nuevo(self):
    try:
        conexionBBDD_usuario(self)
        crear(self)
        messagebox.showinfo("3º", "SE HA CREADO EL REGISTRO")
    except:
        messagebox.showinfo("3º", " NOOOOO   SE HA CREADO EL REGISTRO")
def cerrar_ventana(self):
    self.ventana.iconmask()

#SI EL USUARIO ES CORRECTO. COMIENZA SESIÓN   
def inicio_usario(self):
    self.miConexion = sqlite3.connect("Nuevo_Registro.db")
    self.miCursor= self.miConexion.cursor()
    self.usuario = self.nombreE.get()
    self.contr= self.ContraE.get()
    self.miCursor.execute('SELECT * FROM nuevo WHERE  nombre= ? AND password = ?', (self.usuario, self.contr))
    if self.miCursor.fetchall():
        messagebox.showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
        ventana_opcion_uno(self)
        self.ventana.iconmask()
        
    else:
        messagebox.showerror(title = "LOGIN INCORRECTO", message = "VUELVA A ESCRIBIR USUARIO Y CONTRASEÑA")
        self.nombreE.delete(0,END)
        self.ContraE.delete(0,END)
    self.miCursor.close()
    
        
    
def botones(self):
    self.conecta = Button(self.ventana, text="CONECTAR",command= lambda: inicio_usario(self))
    self.conecta.place(x=600, y=200)

    self.Borrar = Button(self.ventana, text="BORRAR",command= lambda: borrar(self))
    self.Borrar.place(x=800, y=200)

    self.salir= Button(self.ventana, text="SALIR", width= 8, command= lambda: salir(self))
    self.salir.place(x=1000, y=200)

    self.registrar= Button(self.ventana, text="Registrar nuevo usuario",command= lambda: registrar_nuevo(self))
    self.registrar.place(x=1200, y=200)




