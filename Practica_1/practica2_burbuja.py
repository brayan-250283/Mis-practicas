calificaciones = [85, 92, 60, 78, 95, 88, 70, 100, 65, 82, 90, 75, 58, 84, 91]


ascendente = calificaciones.copy()
n = len(ascendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        # Operador de comparación '>' para orden ascendente
        if ascendente[j] > ascendente[j + 1]:
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
            swapped = True
   
    if not swapped: 
        break

print("Orden Ascendente:", ascendente)

descendente = calificaciones.copy()
n = len(descendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        # Operador de comparación '<' para orden descendente
        if descendente[j] < descendente[j + 1]:
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
            swapped = True
    if not swapped:
        break

print("Orden descendente:", descendente)