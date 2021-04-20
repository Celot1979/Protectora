from tkinter import*
from tkinter import ttk
#*************************************************************    TABLA  ********************************************************************************************************
#***************************************************** PANTALLA REGISTROS PARA PERROS ******************************************************************************************
#*******************************************************************************************************************************************************************************
def Tabla(dog):
    tree = ttk.Treeview(dog,height=30, columns=("#0", "#1", "#2,#3", "#4", "#5","#6", "#7"))
    tree.place(x=300, y=400)
    tree.column("#0",width = 75)#Darles tamaños a las columnas
    #Cabeceras de la tabla
    tree.heading("#0", text= "ID",anchor= CENTER)
    tree.heading("#1", text= "Nombre", anchor= CENTER)
    tree.heading("#2", text= "Chip", anchor= CENTER)
    tree.heading("#3", text= "Lugar", anchor= CENTER)
    tree.column("#3",width = 100)
    tree.heading("#4", text= "Raza", anchor= CENTER)
    tree.heading("#5", text= "Fecha", anchor= CENTER)
    tree.heading("#6", text= "Año", anchor= CENTER)
    tree.heading("#7", text= "Vacunado", anchor= CENTER)