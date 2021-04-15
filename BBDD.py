from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Desarrollo de interfaz gráfica

root= Tk()
root.title("Aplicación CRUD con Base de datos")
root.geometry("600x600")

miId=StringVar()
miNombre= StringVar()
miCargo=StringVar()
miSalario =StringVar()

def conexionBBDD():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    try:
        miCursor.execute("""CREATE TABLE empleado(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50) NOT NULL, CARGO VARCHAR(50) NOT NULL, SALARIO NOT NULL)""")
        messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosomanete")
    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

def eliminarBBDD():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass
    limpiarCampos()
    mostrar()
    
def salirAplicacion():
    valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mensaje():
    acerca=""" 
    Aplicación CRUD
    Versión 1.0
    Tecnología Python Tkinter    
    """
    messagebox.showinfo(title="IINFORMACION", message= acerca)


def crear():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    try:
        datos = miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)", (datos))
        miConexion.commit()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
    limpiarCampos()
    mostrar()


   

def mostrar():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleado")
        for row in miCursor:
            tree.insert("",0, text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass

#Tabla
tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2"))
tree.place(x=0, y=130)
tree.column("#0",width = 75)#Darles tamaños a las columnas
#Cabeceras de la tabla
tree.heading("#0", text= "ID",anchor= CENTER)
tree.heading("#1", text= "Nombre del empleado", anchor= CENTER)
tree.heading("#2", text= "Cargo", anchor= CENTER)
tree.heading("#3", text= "Salario", anchor= CENTER)
tree.column("#3",width = 100)


#Para que salga los resgistros en los entrys para posteriomente modificar
def seleccionarUsandoClic(event):
    item= tree.identify("item", event.x,event.y)
    miId.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miCargo.set(tree.item(item,"values")[1])
    miSalario.set(tree.item(item,"values")[2])
tree.bind("<Double-1>", seleccionarUsandoClic)


#Funciones 2ª

def actualizar():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("UPDATE empleado SET NOMBRE = ?, CARGO = ?, SALARIO = ? WHERE ID = "+ miId.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")
        pass
    limpiarCampos()
    mostrar()
        

def borrar():
    miConexion = sqlite3.connect("BDatos.db")
    miCursor= miConexion.cursor()
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM empleado WHERE ID =" + miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")
    limpiarCampos()
    mostrar()

#La funcionalidad está concluida.

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
e1= Entry(root, textvariable=miId)

l2= Label(root, text="Nombre")
l2.place(x=50, y=10)
e2=Entry(root, textvariable=miNombre, width=50)
e2.place(x=110, y= 10)

l3= Label(root, text="Cargo")
l3.place(x=50, y=40)
e3=Entry(root, textvariable=miCargo)
e3.place(x=110, y= 40)

l4= Label(root, text="Salario")
l4.place(x=50, y=80)
l4=Entry(root, textvariable=miSalario, width=10)
l4.place(x=110, y= 80)

#Botones
b1=Button(root, text="Crea Registro", command= crear)
b1.place(x=0, y= 400)
b2=Button(root, text="Modificar registro", command= actualizar)
b2.place(x=120, y= 400)
b3=Button(root, text="Mostrar Lista", command= mostrar)
b3.place(x=270, y= 400)
b4=Button(root, text="Eliminar Registro", command= borrar)
b4.place(x=390, y= 400)
b4.config(bg="red")

root.config(menu=menubar)


root.mainloop()