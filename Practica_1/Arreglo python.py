# Arreglo bidimensional: [ID, Nombre, Stock, Precio]
inventario = [
    [101, "Laptops", 4, 800.00],
    [102, "Teclados", 15, 25.00],
    [103, "Monitores", 3, 200.00],
    [104, "Ratones", 20, 15.00]
]

valor_total_tienda = 0
reabastecer = []

# Recorrer la matriz desestructurando cada fila directamente
for id_prod, nombre, stock, precio in inventario:
    # 1. Calcular el valor de este producto y sumarlo al total
    valor_total_tienda += stock * precio
    
    # 2. Filtrar productos con bajo stock (menos de 5 unidades)
    if stock < 5:
        reabastecer.append(nombre)

# Mostrar resultados formateados
print(f"Valor total del inventario en tienda: ${valor_total_tienda:,.2f}")
print(f"Productos que requieren reabastecimiento urgente: {reabastecer}")

# --- RESULTADO EN CONSOLA ---
# Valor total del inventario en tienda: $4,475.00
# Productos que requieren reabastecimiento urgente: ['Laptops', 'Monitores']
