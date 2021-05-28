from tkinter import *
import psycopg2
def cagada(self):
    self.cagada = "Yo me caguen to"
    print(self.cagada)

def crear(self):
    
    try: 
        self.conectar = psycopg2.connect(database="Protectora", user="postgres", password="1234", host="localhost")
        print("connected")
    except:
        print ("I am unable to connect to the database")
    self.cur = self.conectar.cursor()
    