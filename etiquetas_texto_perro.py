from tkinter import*
import sqlite3
def nuevaAlta(dog):
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
    #Botones de prueba
    b1P=Button(dog, text="Crea Registro")
    b1P.place(x=400, y= 320)
    b2P=Button(dog, text="Modificar registro")
    b2P.place(x=600, y= 320)
    b3p=Button(dog, text="Mostrar Lista")
    b3p.place(x=800, y= 320)
    b4p=Button(dog, text="Eliminar Registro")
    b4p.place(x=1000, y= 320)
    b4p.config(bg="red")




    #b1=Button(dog, text="Crea Registro", #command= crear)
    #b1.place(x=400, y= 320)
    #b2=Button(dog, text="Modificar registro", command= actualizar)
    #b2.place(x=120, y= 400)
    #b3=Button(dog, text="Mostrar Lista", command= mostrar)
    #b3.place(x=270, y= 400)
    #b4=Button(dog, text="Eliminar Registro", command= borrar)
    #b4.place(x=390, y= 400)
    #b4.config(bg="red")