import matplotlib.pyplot as plt

# CORREGIDO: Añadido el signo =
datos = [42, 12, 88, 23, 7, 65, 34, 50]

# ALGORITMO DE INSERCION
def insercion(arr):
    a = arr.copy()
    comp = 0
    # CORREGIDO: Cambiado [] por ()
    for i in range(1, len(a)):
        clave, j = a[i], i - 1
        while j >= 0 and a[j] > clave:
            comp += 1
            a[j+1] = a[j]  # CORREGIDO: Añadido el signo =
            j -= 1
        if j >= 0: 
            comp += 1
        a[j+1] = clave
    return a, comp  # CORREGIDO: Movido fuera del bucle for

# ALGORITMO DE SELECCION
def seleccion(arr):  # CORREGIDO: Añadido el :
    a = arr.copy()
    comp = 0
    n = len(a)  # CORREGIDO: Definido el valor de n
    for i in range(n):
        min_idnx = i
        for j in range(i + 1, n):  # CORREGIDO: Eliminado el + extra
            comp += 1
            if a[j] < a[min_idnx]:
                min_idnx = j
        # CORREGIDO: Movido fuera del bucle de 'j'
        a[i], a[min_idnx] = a[min_idnx], a[i]
    return a, comp  # CORREGIDO: Movido fuera del bucle for

# EJECUTAMOS LOS DOS ALGORITMOS
lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)

# GRAFICACION CON MATPLOTLIB
# CORREGIDO: subplots en plural
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))

# GRAFICO 1: LISTA DESORDENADA
ax1.bar(range(len(datos)), datos, color='red')
ax1.set_title('1. LISTA ORIGINAL')
ax1.set_ylabel('Valor')

# GRAFICO 2: LISTA ORDENADA
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='blue')
ax2.set_title('2. LISTA ORDENADA')

# GRAFICO 3 COMPARACIONES REALIZADAS
ax3.bar(['insercion', 'seleccion'], [comp_ins, comp_sel], color=["#175b8b", "#b6733a"])
ax3.set_title('3. COMPARACIONES')
ax3.set_ylabel('cantidad')

plt.tight_layout()
plt.show()  # CORREGIDO: Escrito correctamente show()
