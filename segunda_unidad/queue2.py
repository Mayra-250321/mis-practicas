from collections import deque
import time
cola_reproduccion=deque()
#AGREGAR CANCIONES A LA COLA
cola_reproduccion.append("1. Antologia")
cola_reproduccion.append("2. viento")
cola_reproduccion.append("3. Jueves")
#MOSTAR LAS CANCIOMES EN ESPERA
print("CANCIONES EN ESPERA")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("iniciando reproduccion")
#EL REPRODUCTOR PROCESA LA COLA, CANCION POR CANCION 
#DESENCOLAR
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"sonando ahora:{cancion_actual}")
    time.sleep(1) #simule la duracion del tema
    print(f"Finalizo:{cancion_actual}")
#MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA 
print(f"Quedan:{len(cola_reproduccion)} canciones en la cola")
print("LA COLA REPRODUCIDA HA FINALIZADO")