
inicio = int(input("¿Desde qué grado Fahrenheit empezar?: "))
fin = int(input("¿Hasta qué grado?: "))
salto = int(input("¿De cuánto en cuánto (intervalo)?: "))


print("\nFahrenheit | Celsius  | Kelvin   | Rankine")
print("-" * 45)

# 3. Bucle para calcular y mostrar
f = inicio
while f <= fin:
    # Fórmulas
    c = 5 * (f - 32) / 9
    r = f + 459.67
    k = c + 273.15
    
    # Mostrar fila con formato simple (2 decimales)
    print(f"{f:<10} | {c:<8.2f} | {k:<8.2f} | {r:<8.2f}")
    
    # Aumentar el valor de F según el intervalo
    f = f + salto