import sqlite3
from tkinter import *
from tkinter import messagebox
import io
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
        messagebox.showinfo("BBDDD Creada con exito", "ENHORABUENA YA TIENES TÚ BBDD CREADA")
    except:
        messagebox.showinfo("LA BBDD YA ESTÁ CREADA", "SIGUE CON EL PROCCESO ")
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
def mostrar_foto():
    miConexion = sqlite3.connect("FOTO.db")
    miCursor= miConexion.cursor()
    miCursor.execute("SELECT FOTO FROM FOTO WHERE ID= 1" )
    row=miCursor.fetchone()
    miCursor.close()
    miConexion.close()
    if row is not None:
        v_foto = row[3]
        img = Image.open(io.BytesIO(v_foto))
        pic= ImageTk.PhotoImage(img)
        imagen = Label(root, image=pic)
        imagen.place(x=400, y=400)
    else:
        imagen = Label(root, text = "Imagen no encontrada")
        imagen.place(x=400, y=400)
    imagen.place(x=400, y=400)
    

def registrar_nuevo():
    conexionBBDD_usuario()
    crear()
    mostrar_foto()
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