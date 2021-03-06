from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  csv
import sqlite3
from datetime import date
from datetime import datetime
from tkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
import io
import os


#***************************************** VENTANA PRINCIPAL  ******************************************************************************************
#****************************************  PANTALLA PRINCIPAL ******************************************************************************************
#********************************************************************************************************************************************************************
root= Tk()
root.geometry("5000x5000")

root.title("PALEVLAS")
#***************************************** IMAGEN CENTRAL DE LA PROTECTORA ******************************************************************************************
#********************************************************************************************************************************************************************
if os.name == "nt":#Para Windows
    imagen = PhotoImage(file="Src\imag\Proctetora.png")
    #image= imagen.subsample(2,2)#Con está instrucción, se puede modificar el tamaño de las imagenes.
    Imagen_2 =Label(root, image=imagen)
    Imagen_2.place(x=650, y=220)
else:#Para Imac
    imagen = PhotoImage(file="Src/imag/Proctetora.png")
    #image= imagen.subsample(2,2)#Con está instrucción, se puede modificar el tamaño de las imagenes.
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

PasswordE=Entry(root, width= 20, textvariable=Contrasena, show= "*",background="azure")
PasswordE.place(x=1000, y= 138)

Derechos = Label(root, text="Este programa pertenece a la protectora recibiendo los derechos del desarollador Daniel Gil", background="azure",font=("Monaco",10))
Derechos.place(x=750, y = 900)
#Funciones para la pantalla principal************************************
def limpiarCampos_registro():
    nombre.set()
    Contrasena.set()

"""def conectar():#Función en desuso al crear usarios y contraseñas con base de datos
    if nombreE.get() == "Dani" and PasswordE.get() == "1":
        segunda_ventana()
    else:
        print("Error")"""
def borrar():
    nombreE.delete(0,END)
    PasswordE.delete(0,END)
def salir():
    root.destroy()
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
        nombreE.delete(0,END)
        PasswordE.delete(0,END)
    miCursor.close()

    
        
    
    

####################################################################################################
####################################################################################################
####################################################################################################





#Botones pantalla principal************************************
#Aceptar******
conecto = Button(root, text="Conectar", width= 8, command= inicio_usario)
conecto.place(x=600, y=200)
conecto.config(overrelief=GROOVE, relief=FLAT)
#Borrar*****
borrar= Button(root, text="BORRAR", width= 8, command=borrar)
borrar.place(x=800, y=200)
borrar.config(overrelief=GROOVE, relief=FLAT)
#Salir*****
salir= Button(root, text="SALIR", width= 8, command=salir)
salir.place(x=1000, y=200)
salir.config(overrelief=GROOVE, relief=FLAT)

registrar= Button(root, text="Registrar nuevo usuario", width= 15,command=registrar_nuevo)
registrar.place(x=1200, y=200)
registrar.config(overrelief=GROOVE, relief=FLAT)
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
            registro()

    def ingreso_gato():
        valor = messagebox.askquestion("Registrar","¿Deseas registrar un nuevo gato? ")
        if valor == "yes":
            registro_gato()

    def ingreso_visitas():
        valor = messagebox.askquestion("Registrar","¿Deseas registrar una nueva visita? ")
        if valor == "yes":
            registro_visitas()


    def ingreso_adopcion():
        valor = messagebox.askquestion("Registrar","¿Deseas registrar una adopcion? ")
        if valor == "yes":
            registro_adopcion()


    #---------------------------------------------------------------------------------------------------------------------
    #Una vez que el usuario acepta hacer un nuevo registro le sale la nueva pantalla
    #***************************************** VENTANA PERROS  ******************************************************************************************
    #************************************** TERCERA PANTALLA PRINCIPAL ******************************************************************************************
    #********************************************************************************************************************************************************************
    def registro():

        root.iconify()

        ventana_dos.iconify()

        perro= Toplevel()

        perro.geometry("5000x5000")

        perro.title("Registro de nuevo perro")

        ############################################## COMENZAMOS LA BBDD Y REGISTROS ###########################################################

        miId=StringVar()

        miNombre_Perro= StringVar()

        miChip=StringVar()

        miLugar =StringVar()

        miRaza =StringVar()

        miEdad=StringVar()

        miFecha=StringVar()

        miFoto= StringVar()

        #Conexión de la BBDD

        def conexionBBDD():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            try:

                miCursor.execute("""CREATE TABLE perro(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_PERRO VARCHAR(50) NOT NULL, 
                CHIP VARCHAR(50) NOT NULL, 
                LUGAR VARCHAR(50) NOT NULL, 
                RAZA VARCHAR(50) NOT NULL, 
                EDAD VARCHAR(50) NOT NULL, 
                FECHA VARCHAR(50) NOT NULL,
                FOTO BLOB NOT NULL)""")

                messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosomanete")

            except:

                messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

        def eliminarBBDD():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):

                miCursor.execute("DROP TABLE perro")

            else:

                pass

                limpiarCampos()

                mostrar()

        def salirAplicacion():

            valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")

            if valor == "yes":

                perro.destroy()

                ventana_dos.destroy()

                root.destroy()

        def limpiarCampos():

            miId.set("")

            miNombre_Perro.set("")

            miChip.set("")

            miLugar.set("")

            miRaza.set("")

            miEdad.set("")

            miFecha.set("")

            miFoto.set(" ")

        def mensaje():

            acerca=""" 
            Aplicación CRUD
            Versión 1.0
            Tecnología Python Tkinter    
            """

            messagebox.showinfo(title="INFORMACION", message= acerca)

        def crear():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()
            #Función que permite leer una imagen y conertirla en bytes
            def convertir_foto(miFoto):

                with open(miFoto, "rb") as f:

                    blob = f.read()

                return blob

            try:

                datos_perro = miNombre_Perro.get(),miChip.get(),miLugar.get(),miRaza.get(),miEdad.get(),miFecha.get(), convertir_foto(miFoto.get())

                miCursor.execute("INSERT INTO perro VALUES(NULL,?,?,?,?,?,?,?)", (datos_perro))

                miConexion.commit()

            except:

                messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")

            limpiarCampos()

            mostrar()

 

        

 

        def mostrar():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            registros = tree.get_children()

            for elemento in registros:

                tree.delete(elemento)

            try:

                miCursor.execute("SELECT * FROM perro")

                for row in miCursor:

                    tree.insert("",0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5],row[6],row[7]))

            except:

                pass

        #Tabla

        tree = ttk.Treeview(perro,height=10, columns=("#0", "#1", "#2","#3","#4","#5","#6"))

        tree.place(x=0, y=200)

        tree.column("#0",width = 75)#Darles tamaños a las columnas

        #Cabeceras de la tabla

        tree.heading("#0", text= "ID",anchor= CENTER)

        tree.heading("#1", text= "Nombre del perro", anchor= CENTER)

        tree.heading("#2", text= "Chip", anchor= CENTER)

        tree.heading("#3", text= "Lugar", anchor= CENTER)

        tree.column("#3",width = 100)

        tree.heading("#4", text= "Raza", anchor= CENTER)

        tree.heading("#5", text= "Edad", anchor= CENTER)

        tree.heading("#6", text= "Fecha de registro", anchor= CENTER)

        tree.heading("#7", text= "Foto", anchor= CENTER)

        

        def seleccionarUsandoClic(event):

            item= tree.identify("item", event.x,event.y)

            miId.set(tree.item(item,"text"))

            miNombre_Perro.set(tree.item(item,"values")[0])

            miChip.set(tree.item(item,"values")[1])

            miLugar.set(tree.item(item,"values")[2])

            miRaza.set(tree.item(item,"values")[3])

            miEdad.set(tree.item(item,"values")[4])

            miFecha.set(tree.item(item,"values")[5])

            miFoto.set(tree.item(item,"values")[6])

        tree.bind("<Double-1>", seleccionarUsandoClic)

        

        #Funciones 2ª

 

        def actualizar():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            try:

                datos_perro = miNombre_Perro.get(),miChip.get(),miLugar.get(),miRaza.get(),miEdad.get(),miFecha.get(), miFoto.get()

                miCursor.execute("UPDATE perro SET NOMBRE_PERRO = ?, CHIP = ?, LUGAR = ?, RAZA = ?, EDAD = ?, FECHA = ?, FOTO = ? WHERE ID = "+ miId.get(), (datos_perro))

                miConexion.commit()

            except:

                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")

                pass

            limpiarCampos()

            mostrar()

        def borrar():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            try:

                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):

                    miCursor.execute("DELETE FROM perro WHERE ID =" + miId.get())

                    miConexion.commit()

            except:

                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")

            limpiarCampos()

            mostrar()

 

        def pagina_anterior():

            

            segunda_ventana()

 

        def Fecha_actual():

            now = datetime.now()

            format = now.strftime('%d - %m - %Y')

            miFecha.set(format)

            miFecha.get()

        """ Función implementada para que al presionar el botón ver foto ( una vez seleccionado el registro),
        Aparaezca la foto al lado de los botones."""

        def mostrar_foto():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            miCursor.execute("SELECT * FROM perro WHERE  ID =" + miId.get())

            row = miCursor.fetchone()

            miCursor.close()

            miConexion.close()

            if row is not None:

                v_foto=row[7]

                img = Image.open(io.BytesIO(v_foto))

                pic= ImageTk.PhotoImage(img)

                imagen = Label(perro, image=pic).place(x= 900, y = 600)

                

        

            else:

                imagen = Label(perro, text="Imagen no disponible, height=20, with= 40")

            imagen.place(x= 900, y = 600)
            

 

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

 

        atrasmenu = Menu(menubar, tearoff=0)

        atrasmenu.add_command(label="Pagina anterior", command=pagina_anterior)

        menubar.add_cascade(label="Páginas anterior", menu= atrasmenu)

        #Etiquetas y cajas de texto

        e1= Entry(perro, textvariable=miId)

 

        l2= Label(perro, text="Nombre")

        l2.place(x=50, y=10)

        e2=Entry(perro, textvariable=miNombre_Perro)

        e2.place(x=110, y= 10)

 

        l3= Label(perro, text="Chip")

        l3.place(x=50, y=40)

        e3=Entry(perro, textvariable=miChip)

        e3.place(x=110, y= 40)

 

        l4= Label(perro, text="Lugar")

        l4.place(x=50, y=80)

        l4=Entry(perro, textvariable=miLugar)

        l4.place(x=110, y= 80)

 

        l5= Label(perro, text="Raza")

        l5.place(x=350, y=80)

        l5=Entry(perro, textvariable=miRaza)

        l5.place(x=475, y= 80)

 

        l5= Label(perro, text="Edad")

        l5.place(x=350, y=40)

        l5=Entry(perro, textvariable=miEdad)

        l5.place(x=475, y= 40)

 

        l5= Label(perro, text="Fecha de Registro")

        l5.place(x=350, y=10)

        l5=Entry(perro, textvariable=miFecha, width= 20)

        l5.place(x=475, y= 10)

        

        l6= Label(perro, text="Foto")

        l6.place(x=50, y=120)

        l6=Entry(perro, textvariable=miFoto, width= 20)

        l6.place(x=110, y= 120)

        




        #Botones

        b1=Button(perro, text="Crea Registro", command= crear)

        b1.place(x=0, y= 600)

 

        b2=Button(perro, text="Modificar registro", command= actualizar)

        b2.place(x=120, y= 600)

 

        b3=Button(perro, text="Mostrar Lista", command= mostrar)

        b3.place(x=270, y= 600)

 

        b4=Button(perro, text="Eliminar Registro", command= borrar)

        b4.place(x=390, y= 600)

        b4.config(bg="red")

        

 

        b5=Button(perro, text="Registrar Fecha", command= Fecha_actual)

        b5.place(x=700, y= 10)

        perro.config(menu=menubar)

 

        b6=Button(perro, text="Ver Foto", command= mostrar_foto)

        b6.place(x=500, y= 600)

        perro.mainloop()

    #---------------------------------------------------------------------------------------------------------------------
    #Una vez que el usuario acepta hacer un nuevo registro le sale la nueva pantalla
    #***************************************** VENTANA GATOS  ******************************************************************************************
    #************************************** CUARTA PANTALLA PRINCIPAL ******************************************************************************************
    #********************************************************************************************************************************************************************
    def registro_gato():
        root.iconify()
        ventana_dos.destroy()
        gato = Toplevel()
        gato.geometry("5000x5000")
        gato.title("Registro de nuevo gato")
        ############################################## COMENZAMOS LA BBDD Y REGISTROS ###########################################################
        miId=StringVar()
        miNombre= StringVar()
        miChip=StringVar()
        miLugar =StringVar()
        miRaza =StringVar()
        miEdad=StringVar()
        miFecha=StringVar()
        miFoto= StringVar()
        def conexionBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                miCursor.execute("""CREATE TABLE gato(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL, 
                CHIP VARCHAR(50) NOT NULL, 
                LUGAR VARCHAR(50) NOT NULL, 
                RAZA VARCHAR(50) NOT NULL, 
                EDAD VARCHAR(50) NOT NULL, 
                FECHA VARCHAR(50) NOT NULL,
                 FOTO BLOB NOT NULL)""")
                messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosamente")
            except:
                messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

        def eliminarBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
                miCursor.execute("DROP TABLE gato")
            else:
                pass
                limpiarCampos()
                mostrar()
        def salirAplicacion():
            valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")
            if valor == "yes":
                gato.destroy()
                ventana_dos.destroy()
                root.destroy()
        def limpiarCampos():
            miId.set("")
            miNombre.set("")
            miChip.set("")
            miLugar.set("")
            miRaza.set("")
            miEdad.set("")
            miFecha.set("")
            miFoto.set(" ")
        def mensaje():
            acerca=""" 
            Aplicación CRUD
            Versión 1.0
            Tecnología Python Tkinter    
            """
            messagebox.showinfo(title="INFORMACION", message= acerca)
        def crear():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            def convertir_foto(miFoto):
                with open(miFoto, "rb") as f:
                    blob = f.read()
                return blob
            try:
                datos = miNombre.get(),miChip.get(),miLugar.get(),miRaza.get(),miEdad.get(),miFecha.get(), convertir_foto(miFoto.get())
                miCursor.execute("INSERT INTO gato VALUES(NULL,?,?,?,?,?,?,?)", (datos))
                miConexion.commit()
            except:
                messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
            limpiarCampos()
            mostrar()

        def mostrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            registros = tree.get_children()
            for elemento in registros:
                tree.delete(elemento)
            try:
                miCursor.execute("SELECT * FROM gato")
                for row in miCursor:
                    tree.insert("",0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5],row[6],row[7]))
            except:
                pass
        #Tabla
        tree = ttk.Treeview(gato,height=10, columns=("#0", "#1", "#2","#3","#4","#5","#6"))
        tree.place(x=0, y=200)
        tree.column("#0",width = 75)#Darles tamaños a las columnas
        #Cabeceras de la tabla
        tree.heading("#0", text= "ID",anchor= CENTER)
        tree.heading("#1", text= "Nombre del gato", anchor= CENTER)
        tree.heading("#2", text= "Chip", anchor= CENTER)
        tree.heading("#3", text= "Lugar", anchor= CENTER)
        tree.column("#3",width = 100)
        tree.heading("#4", text= "Raza", anchor= CENTER)
        tree.heading("#5", text= "Edad", anchor= CENTER)
        tree.heading("#6", text= "Fecha de registro", anchor= CENTER)
        tree.heading("#7", text= "Foto", anchor= CENTER)

        def seleccionarUsandoClic(event):
            item= tree.identify("item", event.x,event.y)
            miId.set(tree.item(item,"text"))
            miNombre.set(tree.item(item,"values")[0])
            miChip.set(tree.item(item,"values")[1])
            miLugar.set(tree.item(item,"values")[2])
            miRaza.set(tree.item(item,"values")[3])
            miEdad.set(tree.item(item,"values")[4])
            miFecha.set(tree.item(item,"values")[5])
            miFoto.set(tree.item(item,"values")[6])
        tree.bind("<Double-1>", seleccionarUsandoClic)
        #Funciones 2ª

        def actualizar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miChip.get(),miLugar.get(),miRaza.get(),miEdad.get(),miFecha.get(), miFoto.get()
                miCursor.execute("UPDATE gato SET NOMBRE = ?, CHIP = ?, LUGAR = ?, RAZA = ?, EDAD = ?, FECHA = ?, FOTO = ? WHERE ID = "+ miId.get(), (datos))
                miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")
                pass
            limpiarCampos()
            mostrar()
        def borrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                    miCursor.execute("DELETE FROM gato WHERE ID =" + miId.get())
                    miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")
            limpiarCampos()
            mostrar()

        def pagina_anterior():
            segunda_ventana()

        def Fecha_actual():
            now = datetime.now()
            format = now.strftime('%d - %m - %Y')
            miFecha.set(format)
            miFecha.get()
        def mostrar_foto():

            miConexion = sqlite3.connect("Protectora.db")

            miCursor= miConexion.cursor()

            miCursor.execute("SELECT * FROM gato WHERE  ID =" + miId.get())

            row = miCursor.fetchone()

            miCursor.close()

            miConexion.close()

            if row is not None:

                v_foto=row[7]

                img = Image.open(io.BytesIO(v_foto))

                pic= ImageTk.PhotoImage(img)

                imagen = Label(gato, image=pic).place(x= 900, y = 600)

                

        

            else:

                imagen = Label(gato, text="Imagen no disponible, height=20, with= 40")

            imagen.place(x= 900, y = 600)
        ############################# DISEÑO DE LA INTERFAZ ########################################################
        #1º Menú INICIO
        menubar = Menu(gato)
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

        atrasmenu = Menu(menubar, tearoff=0)
        atrasmenu.add_command(label="Pagina anterior", command=pagina_anterior)
        menubar.add_cascade(label="Páginas anterior", menu= atrasmenu)
        #Etiquetas y cajas de texto
        e1= Entry(gato, textvariable=miId)

        l2= Label(gato, text="Nombre")
        l2.place(x=50, y=10)
        e2=Entry(gato, textvariable=miNombre)
        e2.place(x=110, y= 10)

        l3= Label(gato, text="Chip")
        l3.place(x=50, y=40)
        e3=Entry(gato, textvariable=miChip)
        e3.place(x=110, y= 40)

        l4= Label(gato, text="Lugar")
        l4.place(x=50, y=80)
        l4=Entry(gato, textvariable=miLugar)
        l4.place(x=110, y= 80)

        l5= Label(gato, text="Raza")
        l5.place(x=350, y=80)
        l5=Entry(gato, textvariable=miRaza)
        l5.place(x=475, y= 80)

        l5= Label(gato, text="Edad")
        l5.place(x=350, y=40)
        l5=Entry(gato, textvariable=miEdad)
        l5.place(x=475, y= 40)

        l5= Label(gato, text="Fecha de Registro")
        l5.place(x=350, y=10)
        l5=Entry(gato, textvariable=miFecha)
        l5.place(x=475, y= 10)

        l6= Label(gato, text="Foto")
        l6.place(x=50, y=120)
        l6=Entry(gato, textvariable=miFoto, width= 20)
        l6.place(x=110, y= 120)



        #Botones
        b1=Button(gato, text="Crea Registro", command= crear)
        b1.place(x=0, y= 600)
        b2=Button(gato, text="Modificar registro", command= actualizar)
        b2.place(x=120, y= 600)
        b3=Button(gato, text="Mostrar Lista", command= mostrar)
        b3.place(x=270, y= 600)
        b4=Button(gato, text="Eliminar Registro", command= borrar)
        b4.place(x=390, y= 600)

        b5=Button(gato, text="Registrar Fecha", command= Fecha_actual)
        b5.place(x=700, y= 10)
        b5.config(bg="red")

        b6=Button(gato, text="Ver Foto", command= mostrar_foto)
        b6.place(x=500, y= 600)
        
        gato.config(menu=menubar)
        gato.mainloop()

    #---------------------------------------------------------------------------------------------------------------------
    #Una vez que el usuario acepta hacer un nuevo registro le sale la nueva pantalla
    #****************************************************** VENTANA VISITAS  ******************************************************************************************
    #************************************************* QUINTA  PANTALLA PRINCIPAL ******************************************************************************************
    #********************************************************************************************************************************************************************
    def registro_visitas():
        root.iconify()
        ventana_dos.destroy()
        visita = Toplevel()
        visita.geometry("5000x5000")
        visita.title("Registro de nueva visita")
        
        ############################################## COMENZAMOS LA BBDD Y REGISTROS ###########################################################
        miId=StringVar()
        miNombre= StringVar()
        miApellidos=StringVar()
        miDNI =StringVar()
        miResidencia=StringVar()
        miMotivo=StringVar()
        miFecha=StringVar()
        def conexionBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                miCursor.execute("""CREATE TABLE visita(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL, 
                APELLIDOS VARCHAR(50) NOT NULL, 
                DNI VARCHAR(50) NOT NULL, 
                RESIDENCIA VARCHAR(50) NOT NULL, 
                MOTIVO VARCHAR(50) NOT NULL, 
                FECHA VARCHAR(50) NOT NULL)""")
                messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosamente")
            except:
                messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")
        def eliminarBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
                miCursor.execute("DROP TABLE visita")
            else:
                pass
                limpiarCampos()
                mostrar()

        def salirAplicacion():
            valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")
            if valor == "yes":
                visita.destroy()
                ventana_dos.destroy()
                root.destroy()

        def limpiarCampos():
            miId.set("")
            miNombre.set("")
            miApellidos.set("")
            miDNI.set("")
            miResidencia.set("")
            miMotivo.set("")
            miFecha.set("")

        def mensaje():
            acerca=""" 
            Aplicación CRUD
            Versión 1.0
            Tecnología Python Tkinter    
            """
            messagebox.showinfo(title="INFORMACION", message= acerca)

        def crear():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miApellidos.get(),miDNI.get(),miResidencia.get(),miMotivo.get(),miFecha.get()
                miCursor.execute("INSERT INTO visita VALUES(NULL,?,?,?,?,?,?)", (datos))
                miConexion.commit()
            except:
                messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
            limpiarCampos()
            mostrar()

        def mostrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            registros = tree.get_children()
            for elemento in registros:
                tree.delete(elemento)
            try:
                miCursor.execute("SELECT * FROM visita")
                for row in miCursor:
                    tree.insert("",0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5],row[6]))
            except:
                pass
        #Tabla
        tree = ttk.Treeview(visita,height=10, columns=("#0", "#1", "#2","#3","#4","#5"))
        tree.place(x=0, y=130)
        tree.column("#0",width = 75)#Darles tamaños a las columnas
        #Cabeceras de la tabla
        tree.heading("#0", text= "ID",anchor= CENTER)
        tree.heading("#1", text= "Nombre", anchor= CENTER)
        tree.heading("#2", text= "Apellidos", anchor= CENTER)
        tree.heading("#3", text= "DNI", anchor= CENTER)
        tree.column("#3",width = 100)
        tree.heading("#4", text= "Residencia", anchor= CENTER)
        tree.heading("#5", text= "Motivo", anchor= CENTER)
        tree.heading("#6", text= "Fecha de registro", anchor= CENTER)
        def seleccionarUsandoClic(event):
            item= tree.identify("item", event.x,event.y)
            miId.set(tree.item(item,"text"))
            miNombre.set(tree.item(item,"values")[0])
            miApellidos.set(tree.item(item,"values")[1])
            miDNI.set(tree.item(item,"values")[2])
            miResidencia.set(tree.item(item,"values")[3])
            miMotivo.set(tree.item(item,"values")[4])
            miFecha.set(tree.item(item,"values")[5])
        tree.bind("<Double-1>", seleccionarUsandoClic)
        #Funciones 2ª

        def actualizar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miApellidos.get(),miDNI.get(),miResidencia.get(),miMotivo.get(),miFecha.get()
                miCursor.execute("UPDATE visita SET NOMBRE = ?, APELLIDOS = ?, DNI = ?, RESIDENCIA = ?, MOTIVO = ?, FECHA = ? WHERE ID = "+ miId.get(), (datos))
                miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")
                pass
            limpiarCampos()
            mostrar()

        def borrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                    miCursor.execute("DELETE FROM visita WHERE ID =" + miId.get())
                    miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")
            limpiarCampos()
            mostrar()
        def pagina_anterior():
            segunda_ventana()

        def programar_visita():
            pass
            
        #La funcionalidad está concluida.
        ############################# DISEÑO DE LA INTERFAZ ########################################################
        #1º Menú INICIO
        menubar = Menu(visita)
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

        atrasmenu = Menu(menubar, tearoff=0)
        atrasmenu.add_command(label="Pagina anterior", command=pagina_anterior)
        menubar.add_cascade(label="Páginas anterior", menu= atrasmenu)

        def actualizar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miApellidos.get(),miDNI.get(),miResidencia.get(),miMotivo.get(),miFecha.get()
                miCursor.execute("UPDATE visita SET NOMBRE = ?, APELLIDOS = ?, DNI = ?, RESIDENCIA = ?, MOTIVO = ?, FECHA = ? WHERE ID = "+ miId.get(), (datos))
                miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")
                pass
            limpiarCampos()
            mostrar()
        ############################################################################################################################################################
        ############################################################################################################################################################
        #########################################################  C A L E N D A R I O ###############################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        #CALENDARIO
        cal = Calendar(visita, selectmode = 'day',year = 2021, month = 4,day = 23)
        cal.place(x=1200, y = 150)
        
        def grad_date():
            date.config(text = "Día de la cita: " + cal.get_date() )
            miFecha.set(cal.get_date())
            miFecha.get()
        B=Button(visita, text = "Calendario para gestionar citas",command = grad_date)
        B.place(x=1200, y = 300)
        date = Label(visita, text = "")
        date.pack(pady = 40)
        ####################################################################################################################################
        #Etiquetas y cajas de texto
        e1= Entry(visita, textvariable=miId)

        l2= Label(visita, text="Nombre")
        l2.place(x=50, y=10)
        e2=Entry(visita, textvariable=miNombre)
        e2.place(x=110, y= 10)

        l3= Label(visita, text="Apellidos")
        l3.place(x=50, y=40)
        e3=Entry(visita, textvariable=miApellidos)
        e3.place(x=110, y= 40)

        l4= Label(visita, text="D N I")
        l4.place(x=50, y=80)
        l4=Entry(visita, textvariable=miDNI)
        l4.place(x=110, y= 80)

        l5= Label(visita, text="Residencia")
        l5.place(x=350, y=80)
        l5=Entry(visita, textvariable=miResidencia)
        l5.place(x=475, y= 80)

        l5= Label(visita, text="Motivo")
        l5.place(x=350, y=40)
        l5=Entry(visita, textvariable=miMotivo)
        l5.place(x=475, y= 40)

        l5= Label(visita, text="Fecha de Registro")
        l5.place(x=350, y=10)
        l5=Entry(visita, textvariable=miFecha)
        l5.place(x=475, y= 10)
        #Botones
        b1=Button(visita, text="Crea Registro", command= crear)
        b1.place(x=0, y= 400)
        b2=Button(visita, text="Modificar registro", command= actualizar)
        b2.place(x=120, y= 400)
        b3=Button(visita, text="Mostrar Lista", command= mostrar)
        b3.place(x=270, y= 400)
        b4=Button(visita, text="Eliminar Registro", command= borrar)
        b4.place(x=390, y= 400)
        b4.config(bg="red")

        
        visita.config(menu=menubar)
        visita.mainloop()

    #****************************************************** VENTANA ADOPCION  ******************************************************************************************
    #************************************************* SEXTA  PANTALLA PRINCIPAL ******************************************************************************************
    #********************************************************************************************************************************************************************
    def registro_adopcion():
        root.iconify()
        ventana_dos.destroy()
        adopcion = Toplevel()
        adopcion.geometry("5000x5000")
        adopcion.title("Registro de adopciones")
        miId=StringVar()
        miNombre= StringVar()
        miApellidos=StringVar()
        miDNI =StringVar()
        miResidencia=StringVar()
        adopta=StringVar()
        miFecha=StringVar()
        #Funciones
        def conexionBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            
            try:
                miCursor.execute("""CREATE TABLE adopta(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL, 
                APELLIDOS VARCHAR(50) NOT NULL, 
                DNI VARCHAR(50) NOT NULL, 
                RESIDENCIA VARCHAR(50) NOT NULL,
                CHIP VARCHAR(50) NOT NULL, 
                FECHA VARCHAR(50) NOT NULL)""")
                messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosamente")
            except:
                messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

        def eliminarBBDD():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            if messagebox.askyesno(mensaje = "¿Los Datos se perderán definitivamente, Desea continuar: ?", title="ADVERTENCIA"):
                miCursor.execute("DROP TABLE adopta")
            else:
                pass
            limpiarCampos()
            mostrar()
        def salirAplicacion():
            valor = messagebox.askquestion("Salir","¿Estás seguro que deseas salir? ")
            if valor == "yes":
                adopcion.destroy()
                ventana_dos.destroy()
                root.destroy()

        def limpiarCampos():
            miId.set("")
            miNombre.set("")
            miApellidos.set("")
            miDNI.set("")
            miResidencia.set("")
            adopta.set("")
            miFecha.set("")

        def mensaje():
            acerca=""" 
            Aplicación CRUD
            Versión 1.0
            Tecnología Python Tkinter    
            """
            messagebox.showinfo(title="INFORMACION", message= acerca)
#øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
#øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
#øøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøøø
        def crear():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miApellidos.get(),miDNI.get(),miResidencia.get(),adopta.get(),miFecha.get()
                miCursor.execute("INSERT INTO adopta VALUES(NULL,?,?,?,?,?,?)", (datos))
                #miCursor.execute("DELETE FROM perro WHERE ID = " + adopta.get())
                completar_Adopcion()
                miConexion.commit()
                miCursor.close()
                
                
                
            except:
                messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
            limpiarCampos()
            mostrar()

        def mostrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            registros = tree.get_children()
            for elemento in registros:
                tree.delete(elemento)
            
            try:
                miCursor.execute("SELECT * FROM adopta")
                for row in miCursor:
                    tree.insert("",0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5],row[6]))
                completar_Adopcion()
            except:
                pass
            
        ############################################################################################################################################################
        ############################################################################################################################################################
        #########################################################  ÁRBOLES / TREE ###############################################################################################
        #########################################################     ADOPCION   ###################################################################################################
        ############################################################################################################################################################

        #Tabla
        tree = ttk.Treeview(adopcion,height=10, columns=("#0", "#1", "#2","#3","#4","#5"))
        tree.place(x=0, y=130)
        tree.column("#0",width = 75)#Darles tamaños a las columnas
        #Cabeceras de la tabla
        tree.heading("#0", text= "ID",anchor= CENTER)
        tree.heading("#1", text= "Nombre", anchor= CENTER)
        tree.heading("#2", text= "Apellidos", anchor= CENTER)
        tree.heading("#3", text= "DNI", anchor= CENTER)
        tree.column("#3",width = 100)
        tree.heading("#4", text= "Residencia", anchor= CENTER)
        tree.heading("#5", text= "Chip", anchor= CENTER)
        tree.heading("#6", text= "Fecha de registro", anchor= CENTER)





        # Segunda tabla 
        resultados_adopcion= ttk.Treeview(adopcion,height=10, columns=("#0", "#1", "#2","#3","#4","#5"))
        resultados_adopcion.place(x=0, y=500)
        #Cabeceras de la tabla
        resultados_adopcion.heading("#0", text= "ID",anchor= CENTER)
        resultados_adopcion.heading("#1", text= "Nombre de adoptante", anchor= CENTER)
        resultados_adopcion.heading("#2", text= "Apellidos", anchor= CENTER)
        resultados_adopcion.heading("#3", text= "DNI", anchor= CENTER)
        resultados_adopcion.column("#3",width = 100)
        resultados_adopcion.heading("#4", text= "Nombre animal", anchor= CENTER)
        resultados_adopcion.heading("#5", text= "Chip", anchor= CENTER)
        resultados_adopcion.heading("#6", text= "Raza", anchor= CENTER)

        def completar_Adopcion(): 
            miConexion = sqlite3.connect("Protectora.db") 
            miCursor= miConexion.cursor() 
            registros = resultados_adopcion.get_children()
            try:
                #1º Paso.Imprescindible para hacer borrado y no duplicación del tree resultados_adopcionees
                resultados_adopcion.delete(*resultados_adopcion.get_children())
                prueba = miCursor.execute("SELECT DISTINCT adopta.ID, adopta.NOMBRE, adopta.APELLIDOS, adopta.DNI, perro.NOMBRE_PERRO, perro.CHIP, perro.RAZA FROM adopta LEFT JOIN perro ON adopta.CHIP=perro.CHIP WHERE perro.CHIP is not null ") 
                usuario = prueba.fetchall() 
                for row in usuario: 
                    resultados_adopcion.insert("",END, text=row[0], values=(row[1], row[2], row[3],row[4],row[5],row[6]))   
                    #messagebox.showinfo("IMPRIMIDO CON ÉXITO", "LA CONSULTA SE HA REALIZADO CON ÉXITO")
            except Exception as e: 
                messagebox.showinfo("ADVERTENCIA", e)
            miCursor.close()


        def seleccionarUsandoClic(event):
            item= tree.identify("item", event.x,event.y)
            miId.set(tree.item(item,"text"))
            miNombre.set(tree.item(item,"values")[0])
            miApellidos.set(tree.item(item,"values")[1])
            miDNI.set(tree.item(item,"values")[2])
            miResidencia.set(tree.item(item,"values")[3])
            adopta.set(tree.item(item,"values")[4])
            miFecha.set(tree.item(item,"values")[5])
        tree.bind("<Double-1>", seleccionarUsandoClic)

        def pagina_anterior():
            segunda_ventana()

        menubar = Menu(adopcion)
        menubasedat= Menu(menubar, tearoff=0)
        menubasedat.add_command(label="Crear/Conectar BBDD", command=conexionBBDD)
        menubasedat.add_command(label="Eliminar BBDD", command=eliminarBBDD)
        menubasedat.add_command(label="Salir",command= salirAplicacion)
        menubar.add_cascade(label="Inicio", menu= menubasedat)
        adopcion.config(menu=menubar)

        #Segundo menú AYUDA
        ayudamenu= Menu(menubar, tearoff=0)
        ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
        ayudamenu.add_command(label="Acerca", command=mensaje)
        menubar.add_cascade(label="Ayuda", menu= ayudamenu)

        atrasmenu = Menu(menubar, tearoff=0)
        atrasmenu.add_command(label="Pagina anterior", command=pagina_anterior)
        menubar.add_cascade(label="Páginas anterior", menu= atrasmenu)

        def actualizar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                datos = miNombre.get(),miApellidos.get(),miDNI.get(),miResidencia.get(),adopta.get(),miFecha.get()
                miCursor.execute("UPDATE adopta SET NOMBRE = ?, APELLIDOS = ?, DNI = ?, RESIDENCIA = ?, ADOPTA = ?, FECHA = ? WHERE ID = "+ miId.get(), (datos))
                miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al actualizar el resgistro")
                pass
            limpiarCampos()
            mostrar()

        def borrar():
            miConexion = sqlite3.connect("Protectora.db")
            miCursor= miConexion.cursor()
            try:
                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                    miCursor.execute("DELETE FROM adopta WHERE ID =" + miId.get())
                    miConexion.commit()
            except:
                messagebox.showwarning("ADVERTENCIA", "Ocurrio un error al intentar eliminar el registro")
            limpiarCampos()
            mostrar()
        
       

        
        ############################################################################################################################################################
        ############################################################################################################################################################
        #########################################################  C A L E N D A R I O ###############################################################################################
        ############################################################################################################################################################
        ############################################################################################################################################################
        #CALENDARIO
        cal = Calendar(adopcion, selectmode = 'day',year = 2021, month = 4,day = 23)
        cal.place(x=1200, y = 150)
        
        def grad_date():
            date.config(text = "Día de la cita: " + cal.get_date() )
            miFecha.set(cal.get_date())
            miFecha.get()
        B=Button(adopcion, text = "Calendario para gestionar citas",command = grad_date)
        B.place(x=1200, y = 300)
        date = Label(adopcion, text = "")
        date.pack(pady = 20)
        ############################################################################################################################################################
        ############################################################################################################################################################
        #########################################################  TABLA QUE MUESTRE ADOPTANTE ###############################################################################################
        ##################################################################  ADOPTADO  #######################################################################
        ############################################################################################################################################################
        
        ####################################################################################################################################
        #Etiquetas y cajas de texto
        e1= Entry(adopcion, textvariable=miId)

        l2= Label(adopcion, text="Nombre")
        l2.place(x=50, y=10)
        e2=Entry(adopcion, textvariable=miNombre)
        e2.place(x=110, y= 10)

        l3= Label(adopcion, text="Apellidos")
        l3.place(x=50, y=40)
        e3=Entry(adopcion, textvariable=miApellidos)
        e3.place(x=110, y= 40)

        l4= Label(adopcion, text="D N I")
        l4.place(x=50, y=80)
        l4=Entry(adopcion, textvariable=miDNI)
        l4.place(x=110, y= 80)

        l5= Label(adopcion, text="Residencia")
        l5.place(x=350, y=80)
        l5=Entry(adopcion, textvariable=miResidencia)
        l5.place(x=475, y= 80)

        l5= Label(adopcion, text="Adopta")
        l5.place(x=350, y=40)
        l5=Entry(adopcion, textvariable=adopta)
        l5.place(x=475, y= 40)

        l5= Label(adopcion, text="Fecha de Registro")
        l5.place(x=350, y=10)
        l5=Entry(adopcion, textvariable=miFecha)
        l5.place(x=475, y= 10)
        #Botones
        b1=Button(adopcion, text="Crea Registro",command= crear)
        b1.place(x=0, y= 400)
        b2=Button(adopcion, text="Modificar registro",command= actualizar)
        b2.place(x=120, y= 400)
        b3=Button(adopcion, text="Mostrar Lista", command= mostrar)
        b3.place(x=270, y= 400)
        b4=Button(adopcion, text="Eliminar Registro",command= borrar)
        b4.place(x=390, y= 400)
        b4.config(bg="red")


        

        adopcion.mainloop()








    #####################################################################################################################################################################
    #####################################################################################################################################################################
    #####################################################################################################################################################################
    ################################################################## RESTO DE LA VENTANA PRINCIPAL ####################################################################
    ########################################################## IMAGENES Adptadas a los sistemas operativos *************************************
    #Perro 
    if os.name == "nt":
        imagen = PhotoImage(file="Src\imag\Perro 2.png") 
        Imagen_P =Label(ventana_dos, image=imagen)
        Imagen_P.place(x=840, y=300)

    else:
        imagen = PhotoImage(file="Src/imag/Perro 2.png") 
        Imagen_P =Label(ventana_dos, image=imagen)
        Imagen_P.place(x=840, y=300)

    perros = Button(ventana_dos, text="Entrada de Perros", width=20, height=6,command=ingreso_perro )
    perros.place(x=600, y= 300)
    #perros.config(overrelief=GROOVE, relief=FLAT)

    #Protectoras
    if os.name == "nt":
        imagen4 = PhotoImage(file="Src\imag\casa2.png")
        Imagen_V =Label(ventana_dos, image=imagen4)
        Imagen_V.place(x=1340, y=600)
    else:
        imagen4 = PhotoImage(file="Src/imag/casa2.png")
        Imagen_V =Label(ventana_dos, image=imagen4)
        Imagen_V.place(x=1340, y=600)
    visitas= Button(ventana_dos, text="Visitas", width=20, height=6,command=ingreso_visitas)
    visitas.place(x=1100, y= 600)
    #visitas.config(overrelief=GROOVE, relief=FLAT)

    #Protectora
    if os.name == "nt":
        imagen3 = PhotoImage(file="Src\imag\Adoptantes.png")
        Imagen_A =Label(ventana_dos, image=imagen3)
        Imagen_A.place(x=1340, y=300)

    else:
        imagen3 = PhotoImage(file="Src/imag/Adoptantes.png")
        Imagen_A =Label(ventana_dos, image=imagen3)
        Imagen_A.place(x=1340, y=300)
    Adoptar= Button(ventana_dos, text="Adoptantes", width=20, height=6, command= ingreso_adopcion)
    Adoptar.place(x=1100, y= 300)
    #Adoptar.config(overrelief=GROOVE, relief=FLAT)
    #Gato
    if os.name == "nt":
        imagen2 = PhotoImage(file="Src\imag\Gato 2.png")
        Imagen_G =Label(ventana_dos, image=imagen2)
        Imagen_G.place(x=840, y=600)
    else:
        imagen2 = PhotoImage(file="Src/imag/Gato 2.png")
        Imagen_G =Label(ventana_dos, image=imagen2)
        Imagen_G.place(x=840, y=600)
    gatos = Button(ventana_dos, text="Entrada de gatos", width=20, height=6,command=ingreso_gato )
    gatos.place(x=600, y= 600)
    #gatos.config(overrelief=GROOVE, relief=FLAT)
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
