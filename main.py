from bd.connection import conectar_db
from bd.tables import crear_tabla

if __name__ == "__main__":
    db = conectar_db()
    cursor = db.cursor()
    
    crear_tabla()

    # Agregar una nueva cita
    nombre_paciente = "Juancito Pérez"
    fecha_hora = "2023-10-15 10:30:00" 
    motivo_consulta = "Consulta general"
    
    cursor.execute("INSERT INTO citas (nombre_paciente, fecha_hora, motivo_consulta) VALUES (%s, %s, %s)",
                   (nombre_paciente, fecha_hora, motivo_consulta))
    
    db.commit()  # <-- Esto guarda los cambios en la base de datos
    print("Cita insertada correctamente.")

    cursor.close()
    db.close()