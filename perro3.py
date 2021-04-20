from BBDD import mostrar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from etiquetas_texto_perro import *

import sqlite3
def perro(ventana_dos):
    ventana_dos.iconmask()
    dog = Toplevel()
    dog.geometry("5000x5000")
    dog.title("Entrada en PALEVLAS")
    #FUNCIONES

    def mensaje():
        print("hola")

    
    menubar = Menu(dog)
    Nuevo = Menu(menubar, tearoff=0)
    Editar = Menu(menubar, tearoff=0)
    borrar = Menu(menubar, tearoff=0)
    salir = Menu(menubar, tearoff=0)
    dog.config(menu=menubar)
    #FUNCIONES



















    
    #Menu
    menubar.add_cascade(label="Nuevo", menu= Nuevo)
    #menubar.add_cascade(label="Editar", menu= Editar)
    #menubar.add_cascade(label="Borrar", menu= borrar)
    #menubar.add_cascade(label="Salir", menu= salir) 
    
    Nuevo.add_command(label="Nueva alta", command=lambda: nuevaAlta(dog))
    Nuevo.add_command(label="Crear/ conectar BBDD", command=mostrar)
    Nuevo.add_command(label="Elimnar BBDD", command=mostrar)
    #Variables
    id =StringVar()
    nombre=StringVar()
    chip =StringVar()
    lugar =StringVar()
    raza =StringVar()
    fecha =StringVar()
    year =StringVar()
    vacunado =StringVar()

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
    lugar = Label(dog, text="Lugar", background="azure", font=("Monaco", 18))
    lugar.place(x=400, y=160)
    lugar_txt = Entry(dog, width=20, textvariable=lugar, background="azure")
    lugar_txt.place(x=500, y=160)
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
    #Botones de prueba. Los botones reales ya están en etiquetas_texto.py
    b1P=Button(dog, text="Crea Registro",command= crear)
    b1P.place(x=400, y= 320)
    b2P=Button(dog, text="Modificar registro", command= actualizar)
    b2P.place(x=600, y= 320)
    b3p=Button(dog, text="Mostrar Lista", command= mostrar)
    b3p.place(x=800, y= 320)
    b4p=Button(dog, text="Eliminar Registro", command= borrar)
    b4p.place(x=1000, y= 320)
    b4p.config(bg="red")
    
    
    
    





    dog.mainloop()
