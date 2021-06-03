import builtins
from tkinter import *
from tkinter import messagebox
import psycopg2
def cagada(self):
    self.cagada = "Yo me caguen to"
    print(self.cagada)


"""def conexion():
        con =psycopg2.connect(
            host= "localhost",
            database = "Protectora",
            user = "postgres",
            password = "1234")
        print("Conexion con éxito")
        cursor =con.cursor()"""

        

def crear_tabla():
    con =psycopg2.connect(
            host= "localhost",
            database = "Protectora",
            user = "postgres",
            password = "1234")
    print("Conexion con éxito")
    cursor =con.cursor()
    cursor.execute("DROP TABLE IF EXISTS REGISTROS ")
    sql = """CREATE TABLE REGISTROS(
        ID SERIAL PRIMARY KEY,
        NOMBRE CHAR(50)NOT NULL,
        CONTRASENA CHAR(50) NOT NULL
    
    ) """
    cursor.execute(sql)
    con.commit()
    print("Tabla creada con exito")
    messagebox.showinfo("Tabla creada", "Proceso concluido")

    cursor.close()

def registro_usuario(nombre,contrasena):
    con =psycopg2.connect(
            host= "localhost",
            database = "Protectora",
            user = "postgres",
            password = "1234")
    try:
        cursor =con.cursor()
        
        datos = nombre.get(),contrasena.get()
        sql = "INSERT INTO REGISTROS (NOMBRE,CONTRASENA) VALUES (%s,%s)"
        cursor.execute(sql, datos)
        con.commit()
        messagebox.showinfo("Registro", "Registro creado con exito")
    except:
        messagebox.showwarning("ATENCIÓN", "ERROR EN EL REGISTRO")
    """Intento de registrar usuarios de la protectora """

