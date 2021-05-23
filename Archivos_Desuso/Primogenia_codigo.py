from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  csv
import sqlite3

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
        segunda_ventana()
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
def segunda_ventana():
    root.iconmask()
    ventana_dos = Toplevel()
    ventana_dos.geometry("5000x5000")
    ventana_dos.title("Bienvenido a PALEVLAS")
    #---------------------------------------------------------------------------------------------------------------------
    #Para pedir al usuario si desea registrar un nuevo perro
    def ingreso_perro():
        valor = messagebox.askquestion("Registrar","¿Deseas registrar un nuevo perro? ")
        if valor == "yes":
            messagebox.showinfo("Ahora","Ahora vamos a ellos")
            registro()
    #---------------------------------------------------------------------------------------------------------------------
    #Una vez que el usuario acepta hacer un nuevo registro le sale la nueva pantalla
    #***************************************** VENTANA PERROS  ******************************************************************************************
    #************************************** TERCERA PANTALLA PRINCIPAL ******************************************************************************************
    #********************************************************************************************************************************************************************
    def registro():
        root.iconify()
        ventana_dos.destroy()
        perro= Toplevel()
        perro.geometry("5000x5000")
        perro.title("Registro de nuevo perro")
        ############################################## COMENZAMOS LA BBDD Y REGISTROS ###########################################################
        miId=StringVar()
        miNombre= StringVar()
        miCargo=StringVar()
        miSalario =StringVar()
        #Conexión de la BBDD
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
                perro.destroy()
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
            messagebox.showinfo(title="INFORMACION", message= acerca)
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
        tree = ttk.Treeview(perro,height=10, columns=("#0", "#1", "#2"))
        tree.place(x=0, y=130)
        tree.column("#0",width = 75)#Darles tamaños a las columnas
        #Cabeceras de la tabla
        tree.heading("#0", text= "ID",anchor= CENTER)
        tree.heading("#1", text= "Nombre del empleado", anchor= CENTER)
        tree.heading("#2", text= "Cargo", anchor= CENTER)
        tree.heading("#3", text= "Salario", anchor= CENTER)
        tree.column("#3",width = 100)
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
        menubar = Menu(perro)
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
        e1= Entry(perro, textvariable=miId)

        l2= Label(perro, text="Nombre")
        l2.place(x=50, y=10)
        e2=Entry(perro, textvariable=miNombre, width=50)
        e2.place(x=110, y= 10)

        l3= Label(perro, text="Cargo")
        l3.place(x=50, y=40)
        e3=Entry(perro, textvariable=miCargo)
        e3.place(x=110, y= 40)

        l4= Label(perro, text="Salario")
        l4.place(x=50, y=80)
        l4=Entry(perro, textvariable=miSalario, width=10)
        l4.place(x=110, y= 80)
        #Botones
        b1=Button(perro, text="Crea Registro", command= crear)
        b1.place(x=0, y= 400)
        b2=Button(perro, text="Modificar registro", command= actualizar)
        b2.place(x=120, y= 400)
        b3=Button(perro, text="Mostrar Lista", command= mostrar)
        b3.place(x=270, y= 400)
        b4=Button(perro, text="Eliminar Registro", command= borrar)
        b4.place(x=390, y= 400)
        b4.config(bg="red")
        perro.config(menu=menubar)
        perro.mainloop()

    #IMAGENES*************************************
    #Perro 
    imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Perro 2.png")
    Imagen_P =Label(ventana_dos, image=imagen)
    Imagen_P.place(x=840, y=300)
    perros = Button(ventana_dos, text="Entrada de Perros", width=20, height=6,background="blue", activebackground="blue",command=ingreso_perro )
    perros.place(x=600, y= 300)
    perros.config(overrelief=GROOVE, relief=FLAT)

    #Visitas
    imagen4 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/casa2.png")
    Imagen_V =Label(ventana_dos, image=imagen4)
    Imagen_V.place(x=1340, y=600)
    visitas= Button(ventana_dos, text="Visitas", width=20, height=6,background="blue", activebackground="blue")
    visitas.place(x=1100, y= 600)
    visitas.config(overrelief=GROOVE, relief=FLAT)

    #Adopcion
    imagen3 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/family 2.png")
    Imagen_A =Label(ventana_dos, image=imagen3)
    Imagen_A.place(x=1340, y=300)
    Adoptar= Button(ventana_dos, text="Adoptantes", width=20, height=6,background="blue", activebackground="blue")
    Adoptar.place(x=1100, y= 300)
    Adoptar.config(overrelief=GROOVE, relief=FLAT)
    #Gato
    imagen2 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Gato 2.png")
    Imagen_G =Label(ventana_dos, image=imagen2)
    Imagen_G.place(x=840, y=600)
    gatos = Button(ventana_dos, text="Entrada de gatos", width=20, height=6,background="blue", activebackground="blue" )
    gatos.place(x=600, y= 600)
    gatos.config(overrelief=GROOVE, relief=FLAT)
    #Menú segunda ventana para
    #funciones 
    def mensaje():
        acerca=""" 
        Aplicación CRUD
        Versión 1.0
        Tecnología Python Tkinter
        Autor Daniel Gil 
        """
        messagebox.showinfo(title="INFORMACION", message= acerca)

    def salirapp():
        ventana_dos.destroy()
        root.destroy()

    
    
    menubar = Menu(root)
    menubasedat= Menu(menubar, tearoff=0)
    menubasedat.add_command(label="Salir",command= salirapp)
    menubar.add_cascade(label="Inicio", menu= menubasedat)
    #Segundo menú AYUDA
    ayudamenu= Menu(menubar, tearoff=0)
    ayudamenu.add_command(label="Acerca",command=mensaje)
    menubar.add_cascade(label="Ayuda", menu= ayudamenu)
    ventana_dos.config(menu=menubar)
    

    ventana_dos.mainloop()



























root.mainloop()