from tkinter import *
root = Tk()
root.geometry("5000x5000")

menubar = Menu(root)
menubasedat= Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear/Conectar BBDD")
menubasedat.add_command(label="Eliminar BBDD")
menubasedat.add_command(label="Salir")
menubar.add_cascade(label="Inicio")
#Segundo menú AYUDA
ayudamenu= Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos")
ayudamenu.add_command(label="Acerca")
menubar.add_cascade(label="Ayuda")
root.mainloop()