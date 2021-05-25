from tkinter import *
from tkinter import messagebox
"""Comienzo de la segunda ventana. En el archivo podremos capturar las acciones que quiera realizar el usuario """
def ventana_opcion_uno(self):
    self.opcion = Toplevel()
    self.opcion.geometry("5000x5000")
    self.opcion.title("Bienvenido a PALEVLAS")
    def prueba(self):
        print("Pruebas")
    self.perros = Button( self.opcion, text="Entrada de Perros", width=20, height=6,command=lambda: prueba(self) )
    self.perros.place(x=600, y= 300)







    self.opcion.mainloop()
