from tkinter import Tk
from tkinter import *
"""En este archivo tome la decisión de encapslar una clase en una función."""
def opciones_protectora():
    r = Tk()
    class Opciones():
        def __init__(self,opcion):
            #Creación de la interfaz de elección de la categoría / opción que se desea entrar
            self.opcion = opcion
            self.opcion.title("REGISTROS EN PALEVLAS ")
            self.opcion.attributes('-fullscreen', True)  #Apertura en ventana completa
            #Creación del frame que permite la cración de los botones
            self.frame_dos = Frame(self.opcion)
            self.frame_dos.pack(expand=1)
            self.frame_dos.config(bg="lightblue",width= 1000, height= 1000)
            """Funciones de los botones"""
            def perro():
                print("Entrada de perro")

            def gato():
                print("Entrada de gato")

            def adoptante():
                print("Adopcion concuida")

            def visitas():
                print("visita programada")
            #Creación de lo botones dentro del Frame
            #Creación de la opción de registros de perros
            self.perro = Button(self.frame_dos, text="Entrada de perros",command=perro())
            self.perro.grid(row=3,column=1, padx= 10, pady= 30)

            """self.imagen = PhotoImage(file="Src/imag/Proctetora.png")
            self.Imagen2= Label(self.frame_dos, image=self.imagen)
            self.Imagen2.grid(row=4,columnspan=6)"""

            #Creación de la opción de registros de gatos
            self.gato = Button(self.frame_dos, text="Entrada de gatos",command =gato())
            self.gato.grid(row=5,column=1, padx= 10, pady= 30)

            #Creación de la opción de registros de adoptantes
            self.adoptantes = Button(self.frame_dos, text="Adoptantes",command =adoptante())
            self.adoptantes.grid(row=3,column=6, padx= 10, pady= 30)

            #Creación de la opción de registros de visitas
            self.visitas = Button(self.frame_dos, text="Visitas",command =visitas())
            self.visitas.grid(row=5,column=6, padx= 10, pady= 30)

            
            

        

    op = Opciones(r)
    
    r.mainloop()   
