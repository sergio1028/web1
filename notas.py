
estudiantes = [
    {"nombre" : "Andres", "notas": [3.0, 4.5, 4.0]},
    {"nombre" : "Fabio", "notas": [4.0, 5.0, 3.5]},
    {"nombre" : "Maria", "notas": [2.9, 3.0, 3.6]}
]

print("----datos cargados----")
print (f"total de estudiantes: {len(estudiantes)}")

def calcular_promedio(lista_notas):

    if len(lista_notas) == 0:
        return 0
    
    suma = 0
    for nota in lista_notas:
        suma += nota

    promedio = suma / len(lista_notas)
    return promedio


print("prueba del promedio Maria", calcular_promedio(estudiantes[2]["notas"]))
