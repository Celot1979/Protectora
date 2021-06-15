from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from window_info import *




def opciones_protectora():
    r = Toplevel()
    
    class Opciones:
        def __init__(self, opcion):
            # Creación de la interfaz de elección de la categoría / opción que se desea entrar
            self.opcion = opcion
            self.opcion.title("REGISTROS EN PALEVLAS ")
            self.opcion.attributes("-fullscreen", True)  # Apertura en ventana completa
            # Creación del frame que permite la cración de los botones
            self.frame_dos = Frame(self.opcion)
            self.frame_dos.pack(expand=1)
            #self.frame_dos.config(bg="lightblue", width=1500, height=1000)
            """Funciones de los botones"""

            def perro():
                print("Entrada de perro")

            def gato():
                print("Entrada de gato")

            def adoptante():
                print("Adopcion concuida")

            def visitas():
                print("visita programada")


            def perro_2():
                print("Prueba")

            # Creación de lo botones dentro del Frame
            # Creación de la opción de registros de perros
            self.perro = Button(self.frame_dos, text="Entrada de perros",height= 5, command=lambda:perro())
            self.perro.grid(row=3, column=1, padx=10, pady=30)

            self.imagen = PhotoImage(file="Src/imag/Perro 2.png")
            self.Imagen2 = Label(self.frame_dos, image=self.imagen)
            self.Imagen2.grid(row=3, column=2)

            # Creación de la opción de registros de gatos
            self.gato = Button(self.frame_dos, text="Entrada de gatos",height= 5, command=lambda:gato())
            self.gato.grid(row=5, column=1, padx=10, pady=30)

            self.g = PhotoImage(file="Src/imag/Gato 2.png")
            self.im_g=Label(self.frame_dos , image= self.g)
            self.im_g.grid(row=5,column=2)

            # Creación de la opción de registros de adoptantes
            self.adoptantes = Button(self.frame_dos, text="Adoptantes",height= 5, command=lambda:adoptante())
            self.adoptantes.grid(row=3, column=6, padx=10, pady=30)

            self.imagen_v = PhotoImage(file="Src/imag/Adoptantes.png")
            self.im_v = Label(self.frame_dos, image=self.imagen_v)
            self.im_v.grid(row=3,column=7)

            # Creación de la opción de registros de visitas
            self.visitas = Button(self.frame_dos, text="Visitas",height= 5, command=lambda:visitas())
            self.visitas.grid(row=5, column=6, padx=10, pady=30)

            self.imagen_vi=PhotoImage(file="Src/imag/casa2.png")
            self.im_vi = Label(self.frame_dos, image=self.imagen_vi)
            self.im_vi.grid(row=5,column=7)

        def menu (self,opcion_2):#Opciones laterales...
            self.opcion_2 = opcion_2
            self.frame_tres = Frame(self.opcion_2)
            self.frame_tres.place(x= 0, y = 0)
            self.frame_tres.config(width=5000, height=100)
            #Radiobutton
            self.elegir_opcion = Label(self.frame_tres, text="MENÚ DE ELECCIÓN").place(x = 10, y =0)#Titulo de menú de elección
            self.seleccion = IntVar()#Variable de comparación de elección por parte del usuario
            def cerrar(self):#Función que implementará el cierre por instrucción del Toplevel
                self.r_end = r.destroy()

            def imagen_informativa(self):
                self.imagen = PhotoImage(file="Src/imag/Perro 2.png")
                self.Imagen2 = Label(self.frame_dos, image=self.imagen)
                self.Imagen2.grid(row=3, column=2)
            def estado(self):#Funcíon que hace la comparación entre lo elegido por el usuario y las determinadas funciones
                self.s = self.seleccion.get()
                if self.s == 1:
                    cerrar(self)
                elif self.s == 2:
                    info()

            #Radiobotones que dan a elegir enter dos opciones        
            self.rdB= Radiobutton(self.frame_tres,text="SALIR",value=1,variable = self.seleccion, command=lambda:estado(self)).place(x = 10, y = 50)
            self.rdB_2= Radiobutton(self.frame_tres,text="INFORMACIÓN",value=2,variable = self.seleccion,command=lambda:estado(self)).place(x = 100, y =50)
            
            


            
                
                



    op = Opciones(r)
    op.menu(r)
    r.mainloop()
