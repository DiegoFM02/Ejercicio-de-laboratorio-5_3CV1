def mochila1(items, capacity):
    # Ordenar los objetos por beneficio por unidad de peso (valor / peso)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    taken_items = []

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            taken_items.append((value, weight))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            taken_items.append((fraction * value, capacity))
            break  # Se alcanzó la capacidad máxima de la mochila

    return total_value, taken_items

# Datos de ejemplo
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

# Llamar a la función para obtener la ganancia máxima y los objetos seleccionados
max_value, selected_items = mochila1(items, capacity)

print("Ganancia máxima:", max_value)
print("Objetos seleccionados (beneficio, peso):", selected_items)



##########################################################################################
"""def mochila2(items, capacity):
    # Ordenar los objetos por beneficio por unidad de peso (valor / peso)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    taken_items = []

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            taken_items.append((value, weight))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            taken_items.append((fraction * value, capacity))
            break  # Se alcanzó la capacidad máxima de la mochila

    return total_value, taken_items

# Datos de ejemplo
items = [(60, 30), (100, 35), (120, 40)]
capacity = 50

# Llamar a la función para obtener la ganancia máxima y los objetos seleccionados
max_value, selected_items = mochila2(items, capacity)

print("Ganancia máxima:", max_value)
print("Objetos seleccionados (beneficio, peso):", selected_items)"""



##########################################################################################
"""def mochila3(items, capacity):
    # Ordenar los objetos por beneficio por unidad de peso (valor / peso)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    taken_items = []

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            taken_items.append((value, weight))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            taken_items.append((fraction * value, capacity))
            break  # Se alcanzó la capacidad máxima de la mochila

    return total_value, taken_items

# Datos de ejemplo
items = [(20, 5), (50, 20), (55, 35)]
capacity = 50

# Llamar a la función para obtener la ganancia máxima y los objetos seleccionados
max_value, selected_items = mochila3(items, capacity)

print("Ganancia máxima:", max_value)
print("Objetos seleccionados (beneficio, peso):", selected_items)"""



##########################################################################################
"""def mochila4(items, capacity):
    # Ordenar los objetos por beneficio por unidad de peso (valor / peso)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    taken_items = []

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            taken_items.append((value, weight))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            taken_items.append((fraction * value, capacity))
            break  # Se alcanzó la capacidad máxima de la mochila

    return total_value, taken_items

# Datos de ejemplo
items = [(25, 10), (45, 20), (35, 30)]
capacity = 50

# Llamar a la función para obtener la ganancia máxima y los objetos seleccionados
max_value, selected_items = mochila4(items, capacity)

print("Ganancia máxima:", max_value)
print("Objetos seleccionados (beneficio, peso):", selected_items)"""
