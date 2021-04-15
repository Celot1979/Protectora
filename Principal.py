from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  csv
import sqlite3




root = Tk()
root.geometry("5000x5000")
root.title("PALEVLAS")
################################################# SEGUNDA VENTANA #######################################################################################################
def menu():
    root.iconify()
    ventana2 = Toplevel()
    ventana2.geometry("5000x5000")
    ventana2.title("Bienvenido a PALEVLAS")
# - - - - - - - - - - - - - - - - - - - - - - CONTROL BBDD - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    #Seguir aquí introducciendo el código de la BBDD

# - - - - - - - - - - - - - - - - - - - - - - -Botones de control - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - -- - -PERROS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    

    
    def dog():
        ventana2.iconify()
        dog = Toplevel()
        dog.geometry("5000x5000")
        dog.title("Entrada en PALEVLAS")
        menubar = Menu(dog)
        menubasedat= Menu(menubar, tearoff=0)
#------------ VARIABLES EN LA VENTANA DE PERROS ----------------------------
        id =StringVar()
        nombre=StringVar()
        chip =StringVar()
        lugar =StringVar()
        raza =StringVar()
        fecha =StringVar()
        year =StringVar()
        vacunado =StringVar() 


        dog.mainloop()
 #----------------------------------------------------------- FINAL DE VENTANA PERRRO --------------------------------------------------------------------------------------------------------------
    def Eleccion_perros():#2 ventana opcion de hacer clic en perro y entrar a una nueva ventana
        perros = Button(ventana2, text="Entrada de Perros", width=20, height=6,background="blue", activebackground="blue", command=dog )
        perros.place(x=600, y= 300)
        perros.config(overrelief=GROOVE, relief=FLAT)
        
    Eleccion_perros()
    imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Perro 2.png")
    Imagen_P =Label(ventana2, image=imagen)
    Imagen_P.place(x=840, y=300)
   
    
    
#----------------------------------------------------------- FINAL  PERRRO --------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - -- - - COMIENZO DE GATOS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    def cat():
        ventana2.iconify()
        cat = Toplevel()
        cat.geometry("5000x5000")
        cat.title("Entrada en PALEVLAS")
        menubar = Menu(cat)
        cat.config(menu=menubar)
        #Declaración del menú

        Nuevo = Menu(menubar, tearoff=0)
        Editar = Menu(menubar, tearoff=0)
        borrar = Menu(menubar, tearoff=0)
        salir = Menu(menubar, tearoff=0)
#------------------------------- FUNCION / Nuevo Gato --------------------------------------------------
        def nuevo_gato():
            #ID
            id= Label(cat, text ="ID",background="azure",font=("Monaco",18))
            id.place(x=800, y=80)
            id_txt= Entry(cat, width=20, textvariable=id, background="azure")
            id_txt.place(x=1000, y= 78)
            #Chip
            chip= Label(cat, text ="Chip",background="azure",font=("Monaco",18))
            chip.place(x=800, y=120)
            chip_txt= Entry(cat, width=20, textvariable=id, background="azure")
            chip_txt.place(x=1000, y= 118)
            
            #Lugar
            lugar= Label(cat, text ="Lugar",background="azure",font=("Monaco",18))
            lugar.place(x=800, y=160)
            lugar_txt= Entry(cat, width=20, textvariable=id, background="azure")
            lugar_txt.place(x=1000, y= 158)
            #Raza
            raza= Label(cat, text ="Raza",background="azure",font=("Monaco",18))
            raza.place(x=800, y=200)
            raza_txt= Entry(cat, width=20, textvariable=id, background="azure")
            raza_txt.place(x=1000, y= 198)
            #agnos
            agnos= Label(cat, text ="Años",background="azure",font=("Monaco",18))
            agnos.place(x=800, y=240)
            agnos_txt= Entry(cat, width=20, textvariable=id, background="azure")
            agnos_txt.place(x=1000, y= 238)
            #Fecha
            fecha= Label(cat, text ="Fecha",background="azure",font=("Monaco",18))
            fecha.place(x=800, y=280)
            fecha_txt= Entry(cat, width=20, textvariable=id, background="azure")
            fecha_txt.place(x=1000, y= 278)
            #Vacunado
            vacunado= Label(cat, text ="Vacunado",background="azure",font=("Monaco",18))
            vacunado.place(x=800, y=320)
            vacunado_txt= Entry(cat, width=20, textvariable=id, background="azure")
            vacunado_txt.place(x=1000, y= 318)


            

        Nuevo.add_command(label="Nueva alta", command= nuevo_gato)
        #-------- SALIR ----------------------------------------------------
        def off():
            cat.destroy()
            ventana2.destroy()
            root.destroy()   
        salir.add_command(label="Salir", command= off)  
#------------------------------------------------
        cat.mainloop()
#----------------------------------------------------------- FINAL DE VENTANA GATOS / FUNCION --------------------------------------------------------------------------------------------------------------




    gatos = Button(ventana2, text="Entrada de gatos", width=20, height=6,background="blue", activebackground="blue", command=cat )
    gatos.place(x=600, y= 600)
    gatos.config(overrelief=GROOVE, relief=FLAT)
    imagen2 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Gato 2.png")
    Imagen_G =Label(ventana2, image=imagen2)
    Imagen_G.place(x=840, y=600)
#----------------------------------------------------------- FINAL  GATOS --------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - -- - - ADOPTANTES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def adopt():
        ventana2.iconify()
        adopt = Toplevel()
        adopt.geometry("5000x5000")
        adopt.title("Entrada en PALEVLAS")
        menubar = Menu(adopt)
        adopt.config(menu=menubar)
        #Declaración del menú

        Nuevo = Menu(menubar, tearoff=0)
        Editar = Menu(menubar, tearoff=0)
        borrar = Menu(menubar, tearoff=0)
        salir = Menu(menubar, tearoff=0)

        #Añadimos las partes del menú

        menubar.add_cascade(label="Nuevo", menu= Nuevo)
        menubar.add_cascade(label="Editar", menu= Editar)
        menubar.add_cascade(label="Borrar", menu= borrar)
        menubar.add_cascade(label="Salir", menu= salir) 
        def adoptante():
            #ID
            id= Label(adopt, text ="ID",background="azure",font=("Monaco",18))
            id.place(x=800, y=80)
            id_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            id_txt.place(x=1000, y= 78)
            #Chip
            chip= Label(adopt, text ="Chip",background="azure",font=("Monaco",18))
            chip.place(x=800, y=120)
            chip_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            chip_txt.place(x=1000, y= 118)
            
            #Lugar
            lugar= Label(adopt, text ="Lugar",background="azure",font=("Monaco",18))
            lugar.place(x=800, y=160)
            lugar_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            lugar_txt.place(x=1000, y= 158)
            #Raza
            raza= Label(adopt, text ="Raza",background="azure",font=("Monaco",18))
            raza.place(x=800, y=200)
            raza_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            raza_txt.place(x=1000, y= 198)
            #agnos
            agnos= Label(adopt, text ="Años",background="azure",font=("Monaco",18))
            agnos.place(x=800, y=240)
            agnos_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            agnos_txt.place(x=1000, y= 238)
            #Fecha
            fecha= Label(adopt, text ="Fecha",background="azure",font=("Monaco",18))
            fecha.place(x=800, y=280)
            fecha_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            fecha_txt.place(x=1000, y= 278)
            #Vacunado
            vacunado= Label(adopt, text ="Vacunado",background="azure",font=("Monaco",18))
            vacunado.place(x=800, y=320)
            vacunado_txt= Entry(adopt, width=20, textvariable=id, background="azure")
            vacunado_txt.place(x=1000, y= 318)


            

        Nuevo.add_command(label="Nueva alta", command= adoptante)
        #-------- SALIR ----------------------------------------------------
        def off():
            adopt.destroy()
            ventana2.destroy()
            root.destroy()   
        salir.add_command(label="Salir", command= off)









        adopt.mainloop()


    Adoptar= Button(ventana2, text="Adoptantes", width=20, height=6,background="blue", activebackground="blue" , command=adopt)
    Adoptar.place(x=1100, y= 300)
    Adoptar.config(overrelief=GROOVE, relief=FLAT)
    imagen3 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/family 2.png")
    Imagen_A =Label(ventana2, image=imagen3)
    Imagen_A.place(x=1340, y=300)

    # - - - - - - - - - - - - - - - - - - - - - - -- - - Visitas - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def visit():
        ventana2.iconify()
        visit = Toplevel()
        visit.geometry("5000x5000")
        visit.title("Entrada en PALEVLAS")
        visit.mainloop()
    
    visitas= Button(ventana2, text="Visitas", width=20, height=6,background="blue", activebackground="blue" ,command=visit)
    visitas.place(x=1100, y= 600)
    visitas.config(overrelief=GROOVE, relief=FLAT)
    imagen4 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/casa2.png")
    Imagen_V =Label(ventana2, image=imagen4)
    Imagen_V.place(x=1340, y=600)


    ventana2.mainloop()
################################################# VENTANA PRINCIPAL ################################################
#Variables
nombre=StringVar()
Contrasena = StringVar()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Imagen:
imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Proctetora.png")
Imagen_2 =Label(root, image=imagen)
Imagen_2.place(x=650, y=220)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

nombreL= Label(root,text="NOMBRE",  background="azure",font=("Monaco",18))
nombreL.place(x=800, y= 80)

PasswordL= Label(root,text="CONTRASEÑA",  background="azure",font=("Monaco",18))
PasswordL.place(x=800, y= 140)

nombreE=Entry(root, width= 20, textvariable=nombre,background="azure")
nombreE.place(x=1000, y= 78)

PasswordE=Entry(root, width= 20, textvariable=Contrasena,background="azure")
PasswordE.place(x=1000, y= 138)

Derechos = Label(root, text="Este programa pertenece a la protectora recibiendo los derechos del desarollador Daniel Gil", background="azure",font=("Monaco",10))
Derechos.place(x=750, y = 900)
def conectar():
    if nombreE.get() == "Dani" and PasswordE.get() == "1":
        menu()
    else:
        print("Error")
conectar = Button(root, text="Conectar", width= 8, background="blue", activebackground="blue", command=conectar)
conectar.place(x=800, y=200)
conectar.config(overrelief=GROOVE, relief=FLAT)

def borrar():
    nombreE.delete(0,END)
    PasswordE.delete(0,END)

borrar= Button(root, text="BORRAR", width= 8, background="blue", activebackground="blue", command=borrar)
borrar.place(x=1000, y=200)
borrar.config(overrelief=GROOVE, relief=FLAT)


def salir():
    root.destroy()
salir= Button(root, text="SALIR", width= 8, background="blue", activebackground="blue", command=salir)
salir.place(x=1200, y=200)
salir.config(overrelief=GROOVE, relief=FLAT)


################################################# FINAL VENTANA PRINCIPAL ################################################

root.mainloop()
