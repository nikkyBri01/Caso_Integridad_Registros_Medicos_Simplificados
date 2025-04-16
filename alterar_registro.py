def modificar_registro(db, cursor, id):
    cursor.execute("SELECT nombre_paciente, fecha_hora, motivo_consulta, sello_integridad FROM citas WHERE id = %s", (id,))
    registro = cursor.fetchone()

    if registro:
        nombre_paciente, fecha_hora, motivo_consulta, sello_integridad = registro

        nuevo_nombre = input('Digite su nombre (deje vacío para mantenerlo): ')
        nuevo_motivo = input('Digite el motivo (deje vacío para mantenerlo): ')

        if nuevo_nombre:
            nombre_paciente = nuevo_nombre
        if nuevo_motivo:
            motivo_consulta = nuevo_motivo

        # No recalcula el sello para simular una alteración
        cursor.execute(
            "UPDATE citas SET nombre_paciente = %s, motivo_consulta = %s WHERE id = %s",
            (nombre_paciente, motivo_consulta, id)
        )
        db.commit()
        print("Registro modificado (sin actualizar el sello).")
    else:
        print("Registro no encontrado.")

    