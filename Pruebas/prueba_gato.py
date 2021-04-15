def cat():
    #ventana2.iconify()
    cat = Toplevel()
    cat.geometry("5000x5000")
    cat.title("Entrada en PALEVLAS")
    menubar = Menu(cat)
    cat.config(menu=menubar)
    #Declaración del menú

    Nuevo = Menu(menubar, tearoff=0)
    Editar = Menu(menubar, tearoff=0)
    borrar = Menu(menubar, tearoff=0)
    salir = Menu(menubar, tearoff=0)

    #Añadimos las partes del menú

    menubar.add_cascade(label="Nuevo", menu= Nuevo)
    menubar.add_cascade(label="Editar", menu= Editar)
    menubar.add_cascade(label="Borrar", menu= borrar)
    menubar.add_cascade(label="Salir", menu= salir) 

    cat.mainloop()

cat()