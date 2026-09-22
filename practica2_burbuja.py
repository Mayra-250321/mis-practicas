calificaciones = [8.5, 9.8, 7.2, 9.1, 8.7, 7.0, 9.9, 8.0, 7.6, 7.2, 9.3, 9.6, 9.9, 7.9, 9.9]

print(f"Lista original: {calificaciones}")

# Orden ascendente
ascendente = calificaciones.copy()
n = len(ascendente)

for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if ascendente[j] > ascendente[j + 1]:
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
            swapped = True

    if not swapped:
        break

print(f"Orden Ascendente: {ascendente}")


# Orden descendente
descendente = calificaciones.copy()

for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if descendente[j] < descendente[j + 1]:
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
            swapped = True

    if not swapped:
        break

print(f"Orden Descendente: {descendente}")