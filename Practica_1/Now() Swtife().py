def obtener_fecha_personalizada(formato):
    ahora = datetime.now()
    fecha = ahora.strftime(formato)
    return f"Fecha formateada: {fecha}"

# Llamada a la función
print(obtener_fecha_personalizada("/%m/%Y"))