# algoritmo_a.py
# Suma y el promedio de los primeros n números naturales

print("Cálculo de suma y promedio")

n = int(input("Escribe un número: "))

numeros = []  
suma = 0

for i in range(1, n + 1):
    numeros.append(i)
    suma += i

promedio = suma / n

print("Números:", numeros)
print("La suma de los primeros", n, "números es:", suma)
print("El promedio es:", round(promedio, 2))
