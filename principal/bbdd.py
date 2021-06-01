from tkinter import *
import psycopg2
def cagada(self):
    self.cagada = "Yo me caguen to"
    print(self.cagada)


def conexion():
        con =psycopg2.connect(
            host= "localhost",
            database = "Protectora",
            user = "postgres",
            password = "1234")
        print("Conexion con éxito")
        cursor =con.cursor()

        

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
        NOMBRE CHAR(50)NOT NULL,
        CONTRASENA CHAR(50) NOT NULL
    
    ) """
    cursor.execute(sql)
    con.commit()
    print("Tabla creada con exito")

    cursor.close()