from bd.connection import conectar_db
from bd.tables import crear_tabla
from agregar_cita import agregar_cita
from verificar_integridad import verificar
from alterar_registro import modificar_registro

if __name__ == "__main__":
    #Ejecutar conexión con MYSQL
    db = conectar_db()
    cursor = db.cursor()
    
    #LLamar a las funciones
    crear_tabla(db, cursor)
    agregar_cita(db, cursor)
    verificar(db, cursor, '8')
    
    # modificar_registro(db, cursor, '8')
    # verificar(db, cursor, '8')
    
    cursor.close()
    db.close()
    
    