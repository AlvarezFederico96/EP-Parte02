
import sqlite3

conexion = sqlite3.connect("ventas.db")


tabla_usuario="""CREATE TABLE usuario(
                    Idusuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Usuario TEXT UNIQUE, 
                    Clave TEXT)"""


tabla_producto="""CREATE TABLE producto(
                    Idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre     TEXT UNIQUE,
                    Codigo     TEXT UNIQUE,
                    Precio     REAL
                    )"""

cursor = conexion.cursor()
cursor.execute(tabla_usuario)
cursor.execute(tabla_producto)


conexion.close()





