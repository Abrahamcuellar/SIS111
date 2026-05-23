def mostrar_asignaturas(asignaturas):
    for asignatura in asignaturas:
        nombre = asignatura["nombre"]
        suma = sum(asignatura["notas"])
        promedio = suma / len(asignatura["notas"])
        print(f"{nombre}: {promedio:.2f}")
asignaturas = [
    {"nombre": "Algebra Lineal", "notas": [80, 65, 75]},
    {"nombre": "Matematicas Discretas", "notas": [82, 92, 90]},
    {"nombre": "Pensamiento critico", "notas": [91, 81, 86]}
]
mostrar_asignaturas(asignaturas)