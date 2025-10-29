# algoritmo_21.py
# Calcula promedio y aprueba o reprueba

print("Calculo de notas")


nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))


promedio = (nota1 + nota2 + nota3) / 3


print(f"\nEl promedio del estudiante es: {promedio}")


if promedio >= 3.0:
    print("El estudiante APRUEBA la materia.")
else:
    print("El estudiante REPRUEBA la materia.")
