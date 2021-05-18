import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root= Tk()
root.title("Prueba")
root.geometry("800x600")
nom= StringVar()
pas= StringVar()
foto= StringVar()
#Creación de la BBDD con el campo BLOB 
def conexionBBDD_usuario():
    miConexion = sqlite3.connect("FOTO.db")
    miCursor= miConexion.cursor()
    try:
        miCursor.execute("""CREATE TABLE foto(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL, 
        PASSWORD VARCHAR(50) NOT NULL,
        FOTO BLOB NOT NULL)""")
        messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")
    except:
        messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")
#Función que nos permite abir la foto y leerla. Nos la devulve como BLOB
def convertir_foto(foto):
    with open(foto, "rb") as f:
        blob = f.read()
    return blob


def crear():
    miConexion = sqlite3.connect("FOTO.db")
    miCursor= miConexion.cursor()
    try:
        datos = nom.get(), pas.get(), convertir_foto(foto.get())#Si te fijas en la última parte, la convierto para que pueda ser almacenada
        miCursor.execute("INSERT INTO foto VALUES(NULL,?,?,?)", (datos))
        miConexion.commit()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
    

def registrar_nuevo():
    conexionBBDD_usuario()
    crear()
    messagebox.showinfo("USUARIO REGISTRADO", "ENHORABUENA TE HAS REGISTRADO CON EXITO")

n = Label(root,text="Nombre")
n.place(x=150,y=150)

p = Label(root,text="Contraseña")
p.place(x=150,y=180)

no= Entry(root, textvariable=nom)
no.place(x=250,y=150)

pas= Entry(root, textvariable=pas)
pas.place(x=250,y=180)

f = Label(root,text="Foto")
f.place(x=150,y=210)

fot= Entry(root, textvariable=foto)
fot.place(x=250,y=210)


b1 = Button(root,text="Mostrar", command= registrar_nuevo)
b1.place(x=300,y=240)



root.mainloop()