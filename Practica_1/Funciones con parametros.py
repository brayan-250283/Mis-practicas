def saludar_usuario(nombre, rol):
    # Uso de f-string para interpolación de variables
    mensaje = f"Hola, {nombre}. Tu rol asignado es: {rol}."
    print(mensaje)

# Llamada a la función
saludar_usuario("Brayan", "Administrador")





import matplotlib.pyplot as plt

def graficar_puntos(eje_x, eje_y, titulo):
    # Crear gráfica simple usando matplotlib
    plt.plot(eje_x, eje_y, marker='o')
    plt.title(f"Gráfica: {titulo}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Llamada a la función
datos_x = [1, 2, 3, 4, 5]
datos_y = [2, 4, 6, 8, 10]
graficar_puntos(datos_x, datos_y, "Crecimiento Lineal")