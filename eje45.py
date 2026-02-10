import math

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

# 2. Calcular el discriminante (D)

d = (b**2) - (4 * a * c)

print(f"\nDiscriminante (D) = {d}")

# 3. Evaluar el valor de D y aplicar la fórmula correspondiente
if d == 0:
    x1 = -b / (2 * a)
    print(f"D es igual a 0. La solución única es: X1 = X2 = {x1}")

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"D es mayor a 0. Las soluciones son:")
    print(f"X1 = {x1}")
    print(f"X2 = {x2}")

else:
    print("D es menor a 0. La ecuación no tiene solución en los Reales.")