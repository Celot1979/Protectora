import builtins
from tkinter import *
from tkinter import messagebox
import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Protectora",
        user="postgres",
        password="1234")


def crear_tabla():
    con = get_connection()
    print("Conexion con éxito")
    cursor = con.cursor()

    sql = """CREATE TABLE IF NOT EXISTS USERS(
        ID SERIAL PRIMARY KEY,
        NOMBRE CHAR(50)NOT NULL,
        CONTRASENA CHAR(50) NOT NULL
    
    ) """
    cursor.execute(sql)
    con.commit()
    messagebox.showinfo("Proceso concluido")

    cursor.close()


def registro_usuario(nombre, contrasena):
    crear_tabla()
    con = get_connection()
    try:
        cursor = con.cursor()

        datos = nombre, contrasena
        sql = "INSERT INTO USERS (NOMBRE,CONTRASENA) VALUES (%s,%s)"
        cursor.execute(sql, datos)
        con.commit()
        messagebox.showinfo("Registro", "Registro creado con exito")
    except:
        messagebox.showwarning("ATENCIÓN", "ERROR EN EL REGISTRO")


def conectar_usuario(nombre, contrasena):
    crear_tabla()
    con = get_connection()
    try:
        cursor = con.cursor()
        datos = nombre, contrasena
        sql = "SELECT * FROM USERS WHERE NOMBRE = %s AND CONTRASENA = %s"
        cursor.execute(sql, datos)
        if cursor.fetchone():
            print("Usuario logeado")
    except Exception as e:
        messagebox.showwarning("ATENCIÓN", e)
