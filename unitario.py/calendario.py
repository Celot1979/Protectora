# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()
mi_Frame = Frame() #Creacion del Frame
mi_Frame.pack()  #Empaquetamiento del Frame
mi_Frame.config(bg="blue") #cambiar color de fondo 
mi_Frame.config(width="400", height="200") #cambiar tamaño
mi_Frame.config(bd=24) #cambiar el grosor del borde
mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor
mi_Frame.pack(side="right")
# Set geometry
root.geometry("5000x5000")
# Add Calender
cal = Calendar(mi_Frame, selectmode = 'day',year = 2020, month = 5,day = 22)


cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
# Add Button and Label
Button(mi_Frame, text = "Get Date",command = grad_date).pack(pady = 20)
date = Label(root, text = "")
date.pack(pady = 20)
# Excecute Tkinter
root.mainloop()