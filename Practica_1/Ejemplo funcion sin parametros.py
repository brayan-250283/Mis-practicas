from datetime import datetime

def mostrar_fecha_actual():
    # Obtener fecha y hora actual usando now()
    ahora = datetime.now()
    # Formatear la fecha usando strftime()
    fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
    # Imprimir usando un f-string
    print(f"Fecha y hora actual: {fecha_formateada}")

# Llamada a la función
mostrar_fecha_actual()