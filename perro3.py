from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
def perro(ventana_dos):
    ventana_dos.iconmask()
    dog = Toplevel()
    dog.geometry("5000x5000")
    dog.title("Entrada en PALEVLAS")
    #VARIABLES ##########################3
    id =StringVar()
    nombre=StringVar()
    chip =StringVar()
    lugar =StringVar()
    raza =StringVar()
    fecha =StringVar()
    year =StringVar()
    vacunado =StringVar()
    #*************************************************************    TABLA  ********************************************************************************************************
    #***************************************************** PANTALLA REGISTROS PARA PERROS ******************************************************************************************
    #*******************************************************************************************************************************************************************************
    tree = ttk.Treeview(dog,height=30, columns=("#0", "#1", "#2,#3", "#4", "#5","#6", "#7"))
    tree.place(x=300, y=400)
    tree.column("#0",width = 75)#Darles tamaños a las columnas
    #Cabeceras de la tabla
    tree.heading("#0", text= "ID",anchor= CENTER)
    tree.heading("#1", text= "Nombre", anchor= CENTER)
    tree.heading("#2", text= "Chip", anchor= CENTER)
    tree.heading("#3", text= "Lugar", anchor= CENTER)
    tree.column("#3",width = 100)
    tree.heading("#4", text= "Raza", anchor= CENTER)
    tree.heading("#5", text= "Fecha", anchor= CENTER)
    tree.heading("#6", text= "Año", anchor= CENTER)
    tree.heading("#7", text= "Vacunado", anchor= CENTER)
    
    
    
    #************************************************************* CAMPOS PARA RELLENAR ********************************************************************************************************
    #********************************************************** ETIQUETAS Y CAJAS DE TEXTO ******************************************************************************************
    #*******************************************************************************************************************************************************************************

    id= Label(dog, text ="ID",background="azure",font=("Monaco",18))
    id.place(x=400, y=80)
    id_txt= Entry(dog, width=20, textvariable=id, background="azure")
    id_txt.place(x=500, y= 80)

    #Nombre
    nombre= Label(dog, text ="Nombre",background="azure",font=("Monaco",18))
    nombre.place(x=750, y=80)
    nombre_txt= Entry(dog, width=20, textvariable=nombre, background="azure")
    nombre_txt.place(x=900, y= 80)


    #Chip
    chip= Label(dog, text ="Chip",background="azure",font=("Monaco",18))
    chip.place(x=1150, y=80)
    chip_txt= Entry(dog, width=20, textvariable=chip, background="azure")
    chip_txt.place(x=1250, y= 80)
            
    #Lugar
    lugar= Label(dog, text ="Lugar",background="azure",font=("Monaco",18))
    lugar.place(x=400, y=160)
    lugar_txt= Entry(dog, width=20, textvariable=lugar, background="azure")
    lugar_txt.place(x=500, y= 160)
    #Raza
    raza= Label(dog, text ="Raza",background="azure",font=("Monaco",18))
    raza.place(x=750, y=160)
    raza_txt= Entry(dog, width=20, textvariable=raza, background="azure")
    raza_txt.place(x=900, y= 160)
    #agnos
    agnos= Label(dog, text ="Años",background="azure",font=("Monaco",18))
    agnos.place(x=1150, y=160)
    agnos_txt= Entry(dog, width=20, textvariable= year, background="azure")
    agnos_txt.place(x=1250, y= 160)
    #Fecha
    fecha= Label(dog, text ="Fecha",background="azure",font=("Monaco",18))
    fecha.place(x=400, y=240)
    fecha_txt= Entry(dog, width=20, textvariable=fecha, background="azure")
    fecha_txt.place(x=500, y= 240)
    #Vacunado
    vacunado= Label(dog, text ="Vacunado",background="azure",font=("Monaco",18))
    vacunado.place(x=750, y=240)
    vacunado_txt= Entry(dog, width=20, textvariable=vacunado, background="azure")
    vacunado_txt.place(x=900, y= 240)

    #************************************************************* BASE DE DATOS ********************************************************************************************************
    #************************************************************** FUNCIONES ******************************************************************************************
    #*******************************************************************************************************************************************************************************
    id = StringVar()
    nombre= StringVar()
    chip= StringVar()
    lugar= StringVar()
    raza= StringVar()
    agnos= StringVar()
    fecha= StringVar()
    vacunado= StringVar()
    def conexionBBDD():
        miConexion = sqlite3.connect("Perro.db")
        miCursor= miConexion.cursor()
        try:
            miCursor.execute("""CREATE TABLE Perro(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50) NOT NULL, 
            CHIP VARCHAR(50) NOT NULL, 
            LUGAR VARCHAR(50) NOT NULL,
            RAZA VARCHAR(50) NOT NULL,
            AGNOS VARCHAR(50) NOT NULL,
            FECHA VARCHAR(50) NOT NULL, 
            VACUNADO VARCHAR(50) NOT NULL, )""")
            messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosomanete")
        except:
            messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")
    def eliminarBBDD():
        miConexion = sqlite3.connect("Perro.db")
        miCursor= miConexion.cursor()
        if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
            miCursor.execute("DROP TABLE Perro")
        else:
            pass
        limpiarCampos()
        mostrar()

    def salirAplicacion():
        valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")
        if valor == "yes":
            dog.destroy()

    def limpiarCampos():
        id.set("")
        nombre.set("")
        chip.set("")
        lugar.set("")
        raza.set("")
        agnos.set("")
        fecha.set("")
        vacunado.set("")
    def mensaje():
        acerca=""" 
        Aplicación CRUD
        Versión 1.0
        Tecnología Python Tkinter    
        """
        messagebox.showinfo(title="IINFORMACION", message= acerca)

    def crear():
        miConexion = sqlite3.connect("Perro.db")
        miCursor= miConexion.cursor()
        try:
            datos = nombre.get(),chip.get(),lugar.get(),raza.get(),agnos.get(),fecha.get(),vacunado.get()
            miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?,?,?,?,?)", (datos))
            miConexion.commit()
        except:
            messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
        limpiarCampos()
        mostrar()

    def mostrar():
        miConexion = sqlite3.connect("Perro.db")
        miCursor= miConexion.cursor()
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM Perro")
            for row in miCursor:
                tree.insert("",0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6],row[7]))
        except:
            pass
    def seleccionarUsandoClic(event):
        item= tree.identify("item", event.x,event.y)
        id.set(tree.item(item,"text"))
        nombre.set(tree.item(item,"values")[0])
        chip.set(tree.item(item,"values")[1])
        lugar.set(tree.item(item,"values")[2])
        raza.set(tree.item(item,"values")[3])
        agnos.set(tree.item(item,"values")[4])
        fecha.set(tree.item(item,"values")[5])
        vacunado.set(tree.item(item,"values")[6])
    tree.bind("<Double-1>", seleccionarUsandoClic)
    """Hasta aquí hemos llegado. Revisar el archivo BBDD para seguir rellenando las funciones """

    
    
    


    dog.mainloop()