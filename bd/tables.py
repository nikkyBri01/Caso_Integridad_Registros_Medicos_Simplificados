import mysql.connector

def crear_tabla(db, cursor):
    
    # SQL para crear la tabla
    crear_tabla_citas = """
    CREATE TABLE IF NOT EXISTS citas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_paciente VARCHAR(255) NOT NULL,
        fecha_hora DATETIME NOT NULL,
        motivo_consulta TEXT NOT NULL,
        sello_integridad VARCHAR(10) NOT NULL
    );
    """
    try:
        cursor.execute(crear_tabla_citas)
        print("Tabla 'citas' creada con éxito.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
