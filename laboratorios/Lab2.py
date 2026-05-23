print("--PROMEDIO DE NOTAS--")
mate =  int(input("Ingrese la cantidad de materias: "))
def asignaturas():
    asignaturas = []
    for i in range(int(mate)):
        asignatura = input("Ingrese el nombre de la asignatura: ")
        asignaturas.append(asignatura)
    return asignaturas
print("Tus asignaturas son:", asignaturas())
for materia in asignaturas():
    print(f"Materia: {materia}")
examenes = int(input(f"ngrese la cantidad de examenes para la materia {materia}: "))
def notasex():
    notasex = []
    for i in range(int(examenes)):
        nota = float(input(f"Ingrese la nota del examen para : "))
        notasex.append(nota)
    return notasex
print("Tus notas son:", notasex())
practicas = int(input("Ingrese la cantidad de practicas para la materia"))
def notasprac():
    notasprac = []
    for i in range(int(practicas)):
        nota = float(input(f"Ingrese la nota de la practica para Z: "))
        notasprac.append(nota)
    return notasprac
print("Tus notas son:", notasprac())
def promedio():
    sumaexamenes = sum(notasex())
    sumapracticas = sum(notasprac())
    total = sumaexamenes + sumapracticas
    promedio = total / (examenes + practicas)
    return promedio
for materia in asignaturas():
    print(f"El promedio de la materia {materia} es: {promedio()}")