
estudiantes = [
    {"nombre" : "Andres", "notas": [3.0, 4.5, 4.0]},
    {"nombre" : "Fabio", "notas": [4.0, 5.0, 3.5]},
    {"nombre" : "maria", "notas": [2.9, 3.0, 3.6]}
]

print("----datos cargados----")
print (f"total de estudiantes: {len(estudiantes)}")

def reporte(estudiantes):
    print("---reporte final---")
    for est in estudiantes:
        suma = sum(est["notas"])
        prom = suma / len(est["notas"])
        if prom >= 3.0:
            estado = "aprobado"
        else:
            estado = "reprobado"

        print(f"estudiante: {est["nombre"]} su estado es: {estado}")


reporte(estudiantes)