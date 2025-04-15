import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="tu_user",
        password="tu_pass",
        database="tu_bd"
    )