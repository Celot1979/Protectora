def nuevo_perro():
            #ID
            id= Label(dog, text ="ID",background="azure",font=("Monaco",18))
            id.place(x=800, y=80)
            id_txt= Entry(dog, width=20, textvariable=id, background="azure")
            id_txt.place(x=1000, y= 78)
            #Chip
            chip= Label(dog, text ="Chip",background="azure",font=("Monaco",18))
            chip.place(x=800, y=160)
            chip_txt= Entry(dog, width=20, textvariable=chip, background="azure")
            chip_txt.place(x=1000, y= 158)
            
            #Lugar
            lugar= Label(dog, text ="Lugar",background="azure",font=("Monaco",18))
            lugar.place(x=800, y=200)
            lugar_txt= Entry(dog, width=20, textvariable=lugar, background="azure")
            lugar_txt.place(x=1000, y= 198)
            #Raza
            raza= Label(dog, text ="Raza",background="azure",font=("Monaco",18))
            raza.place(x=800, y=240)
            raza_txt= Entry(dog, width=20, textvariable=raza, background="azure")
            raza_txt.place(x=1000, y= 238)
            #agnos
            agnos= Label(dog, text ="Años",background="azure",font=("Monaco",18))
            agnos.place(x=800, y=280)
            agnos_txt= Entry(dog, width=20, textvariable= year, background="azure")
            agnos_txt.place(x=1000, y= 278)
            #Fecha
            fecha= Label(dog, text ="Fecha",background="azure",font=("Monaco",18))
            fecha.place(x=800, y=320)
            fecha_txt= Entry(dog, width=20, textvariable=fecha, background="azure")
            fecha_txt.place(x=1000, y= 318)
            #Vacunado
            vacunado= Label(dog, text ="Vacunado",background="azure",font=("Monaco",18))
            vacunado.place(x=800, y=360)
            vacunado_txt= Entry(dog, width=20, textvariable=vacunado, background="azure")
            vacunado_txt.place(x=1000, y= 358)

            #Nombre
            nombre= Label(dog, text ="Nombre",background="azure",font=("Monaco",18))
            nombre.place(x=800, y=120)
            nombre_txt= Entry(dog, width=20, textvariable=nombre, background="azure")
            nombre_txt.place(x=1000, y= 118)