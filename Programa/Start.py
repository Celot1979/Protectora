
from tkinter import*
import os
from imagen_central import *
from validacion import *
"""Principio del programa. Esté archivo ejecuta todo el programa """

raiz = Tk()

class Protectora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Protectora")
        self.prueba = Logo(self,self.ventana)#Imagen central
        self.texto_principal = campos(self)#Campos de introduccion de texto
        self.Botones = botones(self)#Botones con sus acciones
        
        
        
        
        

Proyecto = Protectora(raiz)

raiz.mainloop()