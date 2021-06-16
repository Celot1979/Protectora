from bbdd import *
from tkinter import *
from tkinter import messagebox
import psycopg2

def acogida_perro():
    p = Toplevel()
    class Perro():
        def __init__(self,op_perro):
            self.opc_perro = op_perro
            self.opc_perro.title("REGISTROS PERROS")
            self.frame_perro = Frame(self.opc_perro)
            self.frame_perro.place(x=60, y=40)
            #self.frame_perro.config(bg="white", width=1800, height=1000)
            #Variables
        def la_en(self, opc_perro):
            self.opc_perro= opc_perro
            id = StringVar()
            nombre= StringVar()
            chip = StringVar()
            lugar = StringVar()
            raza= StringVar()
            edad= StringVar()
            foto= StringVar()
            #Labels
            self.id = Label(self.frame_perro, text="ID").grid(row=1,column=1)
            self.nombre = Label(self.frame_perro, text="NOMBRE").grid(row=2,column=1)
            
            self.lugar = Label(self.frame_perro, text="LUGAR",padx=10,pady=10).grid(row=3,column=1) 
            self.raza = Label(self.frame_perro, text="RAZA",padx=10,pady=10).grid(row=1,column=3) 
            self.edad = Label(self.frame_perro, text="EDAD",padx=10,pady=10).grid(row=2,column=3)
            self.foto = Label(self.frame_perro, text="FOTO",padx=10,pady=10).grid(row=1,column=5)
            self.chip = Label(self.frame_perro, text="CHIP",padx=10,pady=10).grid(row=3,column=3)

            #entrys

            self.e_id=Entry(self.frame_perro, textvariable = id).grid(row=1,column=2)
            self.e_nombre=Entry(self.frame_perro, textvariable = nombre).grid(row=2,column=2)
            self.e_lugar=Entry(self.frame_perro, textvariable = lugar).grid(row=1,column=4)
            self.e_raza=Entry(self.frame_perro, textvariable = raza).grid(row=2,column=4)
            self.e_edad=Entry(self.frame_perro, textvariable = edad).grid(row=3,column=4)
            self.e_foto=Entry(self.frame_perro, textvariable = foto).grid(row=1,column=6)
            self.e_chip=Entry(self.frame_perro, textvariable = chip).grid(row=3,column=2)

        def botones(self,op_boton):
            self.opc_boton= op_boton
            self.frame_boton = Frame(self.opc_boton)
            self.frame_boton.place(x=60, y=200)
            #Funciones
            def guardar(self):
                print("Hola mundo")
            def borrar(self):
                self.e_id.set("")
                self.e_nombre.set("")
                self.e_lugar.set("")
                self.e_raza.set("")
                self.e_edad.set("")
                self.e_foto.set("")
                self.e_foto.set("")
            def modificar(self):
                print("Modificado")
            def salir(self):
                print("Sacado")
            #Botones
            self.boton_guardar= Button(self.frame_boton , text= "GUARDAR", command = lambda: guardar(self),padx=10, pady=10).grid(row=1,column=1)
            self.boton_borrado= Button(self.frame_boton , text= "BORRAR", command = lambda: borrar(self),padx=10, pady=10).grid(row=1,column=2)
            self.boton_modificar= Button(self.frame_boton , text= "MODIFICAR", command = lambda: modificar(self),padx=10, pady=10).grid(row=1,column=3)
            self.boton_salir= Button(self.frame_boton , text= "SALIR", command = lambda: salir(self),padx=10, pady=10).grid(row=1,column=4)


    perro_1 = Perro(p)
    perro_1.la_en(p) 
    perro_1.botones(p)
    p.mainloop()
