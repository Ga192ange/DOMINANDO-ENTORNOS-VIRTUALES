# algoritmo_22.py
# Temperatura en Celsius a Fahrenheit y Kelvin

print("Temperatura")


celsius = float(input("Ingrese la temperatura en grados Celsius: "))


fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15


print(f"\nTemperatura en Fahrenheit: {fahrenheit:} °F")
print(f"Temperatura en Kelvin: {kelvin:} K")
