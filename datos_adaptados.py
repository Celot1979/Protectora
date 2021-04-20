
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root= Tk()
root.geometry("5000x5000")
root.title("PALEVLAS")
#Variables
id =StringVar()
nombre=StringVar()
chip =StringVar()
lugar =StringVar()
raza =StringVar()
fecha =StringVar()
year =StringVar()
vacunado =StringVar()
def conexionBBDD():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute("""
        CREATE TABLE perro(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50) NOT NULL,CHIP VARCHAR(50) NOT NULL,LUGAR VARCHAR(50) NOT NULL,RAZA VARCHAR(50) NOT NULL,FECHA INT (15) NOT NULL,YEAR INT(15) NOT NULL,VACUNADO NOT NULL""")
        messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosomente")

    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

def eliminarBBDD():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
        miCursor.execute("DROP TABLE perro")
    else:
        pass
    

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Estás seguro que deseas salir de la aplicación?")
    if valor == "si":
        root.destroy()

def limpiarCampos():
    id.set("")
    nombre.set("")
    chip.set("")
    lugar.set("")
    raza.set("") 
    fecha.set("") 
    year.set("") 
    vacunado.set("")
def mensaje():
    acerca="""Aplicación Python-Tkinter Version 1.0"""
############################# METODOS CRUD ###############################################
def crear():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    try:
        datos= nombre.get(),chip.get(),lugar.get(),raza.get(),fecha.get(),year.get(),vacunado.get()
        miCursor.execute("INSERT INTO perro VALUES(NULL,?,?,?,?,?,?,?)",(datos))
        miConexion.commit()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
        pass
    limpiarCampos()
    mostrar()

def inserta(nombre,chip,lugar,raza,fecha,year,vacunado):
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    datos=(nombre,chip,lugar,raza,fecha,year,vacunado)
    sql="""INSERT INTO perro(nombre,chip,lugar,raza,fecha,year,vacunado)VALUES(?,?,?,?,?,?,?"""
    if(miCursor.execute(sql,datos)):
        messagebox.showinfo("CORRECTO", "Se guardo")
    else:
        messagebox.showinfo("INCORRECTO", "NO GUARDADO")
    miConexion.commit()
    miCursor.close()
def guardar():
    no =nombre.get()
    ch= chip.get()
    lu=lugar.get()
    ra=raza.get()
    fe=fecha.get()
    ye=year.get()
    va=vacunado.get()
    if((no== "")or (ch== "")):
        messagebox.showinfo("INCORRECTO", "Faltan datos")
    else:
        inserta(no,ch,lu,ra,fe,ye,va)
        messagebox.showinfo("GUARDADO", "Registro guardado")
        limpiarCampos()
        mostrar()



        


def mostrar():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM perro")
        for row in miCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    except:
        pass

############################# TREE ###################################################################
tree= ttk.Treeview(height=10, columns=("#0","#1","#2","#3","#4","#5","#6"))
tree.place(x=0,y=130)
tree.column("#0",width=100)
tree.heading("#0", text="ID", anchor= CENTER)

tree.heading("#1", text="Nombre", anchor= CENTER)

tree.column("#2",width=100)
tree.heading("#2", text="CHIP", anchor= CENTER)

tree.column("#3",width=150)
tree.heading("#3", text="LUGAR", anchor= CENTER)

tree.heading("#4", text="RAZA", anchor= CENTER)

tree.column("#5",width=70)
tree.heading("#5", text="FECHA", anchor= CENTER)

tree.column("#6",width=50)
tree.heading("#6", text="YEAR", anchor= CENTER)

tree.column("#7",width=100)
tree.heading("#7", text="VACUNADO", anchor= CENTER)

def actualizar():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    try:
        datos= nombre.get(),chip.get(),lugar.get(),raza.get(),fecha.get(),year.get(),vacunado.get()
        miCursor.execute("UPDATE perro SET NOMBRE =?, CHIP=?,LUGAR=?,RAZA=?,FECHA=?,YEAR=?,VACUNADO=? WHERE ID="+ id.get(),(datos))
        miConexion.commit()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al actualizar el registro")
    limpiarCampos()
    mostrar()

def borrar():
    miConexion =sqlite3.connect("b.db")
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message="¿REalmente desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM perro WHERE ID=" + id.get())
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")
    limpiarCampos()
    mostrar()


################# MENU ###########################################

############################# DISEÑO DE LA INTERFAZ ########################################################
#1º Menú INICIO
menubar = Menu(root)
menubasedat= Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear/Conectar BBDD", command=conexionBBDD)
menubasedat.add_command(label="Eliminar BBDD", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command= salirAplicacion)
menubar.add_cascade(label="Inicio", menu= menubasedat)
#Segundo menú AYUDA
ayudamenu= Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu= ayudamenu)

#Etiquetas y cajas de texto
e1= Entry(root, textvariable=id)

l2= Label(root, text="Nombre")
l2.place(x=50, y=400)
e2=Entry(root, textvariable=nombre, width=20)
e2.place(x=110, y= 400)

l3= Label(root, text="Chip")
l3.place(x=400, y=400)
e3=Entry(root, textvariable=chip)
e3.place(x=450, y= 400)

l4= Label(root, text="Lugar")
l4.place(x=690, y=400)
e4=Entry(root, textvariable=lugar)
e4.place(x=740, y= 400)

l5= Label(root, text="Raza")
l5.place(x=50, y=500)
e5=Entry(root, textvariable=raza)
e5.place(x=110, y= 500)

l6= Label(root, text="Fecha")
l6.place(x=400, y=500)
e6=Entry(root, textvariable=fecha)
e6.place(x=450, y= 500)

l7= Label(root, text="Año")
l7.place(x=690, y=500)
e7=Entry(root, textvariable=year)
e7.place(x=740, y= 500)

l8= Label(root, text="Vacunado")
l8.place(x=50, y=600)
e8=Entry(root, textvariable=vacunado)
e8.place(x=150, y= 600)

b1= Button(root,text="Crear Registro", command=guardar)
b1.place(x=50, y=700)

b2= Button(root,text="Modificar Registro", command=actualizar)
b2.place(x=200, y=700)

b3= Button(root,text="Mostrar Registros", command=mostrar)
b3.place(x=350, y=700)

b4= Button(root,text="Borrar Registro", command=borrar)
b4.place(x=500, y=700)











root.config(menu=menubar)


root.mainloop()