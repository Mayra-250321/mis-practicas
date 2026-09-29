def mostrar_encabezado_escuela():
    print("Instituto")
    print("Reporte de Evaluacion y Calificaciones")

def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    print(f"Boleta del alumno {nombre_alumno}")
    print(f"Nota de examenes (70%): {nota_examenes}")
    print(f"Nota de tareas (30%): {nota_tareas}")
    print(f"Calificacion Final: {nota_final}")
    print(f"Estado Academico: {estado}")
    
    if nota_final < nota_minima:
        print("Resultado: Debe presentar examen extraordinario")
    else:
        print("Resultado: No necesita examen extraordinario")

mostrar_encabezado_escuela()
generar_boleta("Iracel Apaez", 8.2, 9.9)


