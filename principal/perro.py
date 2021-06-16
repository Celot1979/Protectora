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



    perro_1 = Perro(p) 
    p.mainloop()
