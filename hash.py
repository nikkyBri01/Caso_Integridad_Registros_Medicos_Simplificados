def hash_simple(texto):
    xor = 0
    for i in texto: 
        xor ^= ord(i) 
    hash_xor = xor % 10000
    return str(hash_xor)

def generar_sello_integridad(nombre, fecha_hora, motivo):
    data = f'{nombre}, {fecha_hora}, {motivo}'
    return hash_simple(data)