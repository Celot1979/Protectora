from tkinter import*
from perro3 import*
from etiquetas_texto_perro import *
from Tabla_perro import*
def segunda_ventana(root):
    root.iconmask()
    
    ventana_dos = Toplevel()
    ventana_dos.geometry("5000x5000")
    ventana_dos.title("Bienvenido a PALEVLAS")
    #IMAGENES*************************************
    #Perro
    imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Perro 2.png")
    Imagen_P =Label(ventana_dos, image=imagen)
    Imagen_P.place(x=840, y=300)
    perros = Button(ventana_dos, text="Entrada de Perros", width=20, height=6,background="blue", activebackground="blue", command= lambda:perro(ventana_dos) )
    perros.place(x=600, y= 300)
    perros.config(overrelief=GROOVE, relief=FLAT)
    #Visitas
    imagen4 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/casa2.png")
    Imagen_V =Label(ventana_dos, image=imagen4)
    Imagen_V.place(x=1340, y=600)
    visitas= Button(ventana_dos, text="Visitas", width=20, height=6,background="blue", activebackground="blue")
    visitas.place(x=1100, y= 600)
    visitas.config(overrelief=GROOVE, relief=FLAT)
    #Adopcion
    imagen3 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/family 2.png")
    Imagen_A =Label(ventana_dos, image=imagen3)
    Imagen_A.place(x=1340, y=300)
    Adoptar= Button(ventana_dos, text="Adoptantes", width=20, height=6,background="blue", activebackground="blue")
    Adoptar.place(x=1100, y= 300)
    Adoptar.config(overrelief=GROOVE, relief=FLAT)
    #Gato
    imagen2 = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Gato 2.png")
    Imagen_G =Label(ventana_dos, image=imagen2)
    Imagen_G.place(x=840, y=600)
    gatos = Button(ventana_dos, text="Entrada de gatos", width=20, height=6,background="blue", activebackground="blue" )
    gatos.place(x=600, y= 600)
    gatos.config(overrelief=GROOVE, relief=FLAT)


    
    ventana_dos.mainloop()