
from hash import generar_sello_integridad

def verificar(db, cursor, id):
    
    cursor.execute("SELECT nombre_paciente, fecha_hora, motivo_consulta, sello_integridad FROM citas WHERE id = %s",(id,))
     
    registro = cursor.fetchone()
    nombre_paciente, fecha_hora, motivo_consulta, sello_almacenado = registro

    sello_calculado = generar_sello_integridad(nombre_paciente, fecha_hora, motivo_consulta)
    
    print(fecha_hora)
    print('calculado', sello_calculado)
    print('almacenado', sello_almacenado)
    
    if sello_calculado == sello_almacenado:
        print('El sello coincide con el valor almacenado') 
    else: 
        print('Datos alterados')



