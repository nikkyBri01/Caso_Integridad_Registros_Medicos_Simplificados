from hash import generar_sello_integridad
from datetime import datetime

def agregar_cita(db, cursor):
      
    # Agregar una nueva cita 
    nombre_paciente = input('Digite su nombre aquí: ')
    fecha_hora = datetime.now() 
    formato_fijo = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
    motivo_consulta = input("¿Cuál es el motivo de su consulta?")
    sello_integridad = generar_sello_integridad(nombre_paciente, formato_fijo, motivo_consulta)
    
    cursor.execute("INSERT INTO citas (nombre_paciente, fecha_hora, motivo_consulta, sello_integridad) VALUES (%s, %s, %s, %s)",
    (nombre_paciente, formato_fijo, motivo_consulta, sello_integridad))

    
    db.commit()  # Guarda los cambios en la base de datos
    print("Cita insertada correctamente.")

