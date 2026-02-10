
peso_niños = cont_niños = 0
peso_jovenes = cont_jovenes = 0
peso_adultos = cont_adultos = 0
peso_viejos = cont_viejos = 0

print("Registro de pesos y edades (100 personas)")

for i in range(1, 101):
    print(f"\nPersona {i}:")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso (kg): "))

    # Clasificación según la tabla proporcionada
    if 0 <= edad <= 12:
        peso_niños += peso
        cont_niños += 1
    elif 13 <= edad <= 29:
        peso_jovenes += peso
        cont_jovenes += 1
    elif 30 <= edad <= 59:
        peso_adultos += peso
        cont_adultos += 1
    elif edad >= 60:
        peso_viejos += peso
        cont_viejos += 1

# Cálculo y despliegue de promedios (validando no dividir por cero)

print(f"Niños (0-12): {peso_niños/cont_niños if cont_niños > 0 else 0:.2f} kg")
print(f"Jóvenes (13-29): {peso_jovenes/cont_jovenes if cont_jovenes > 0 else 0:.2f} kg")
print(f"Adultos (30-59): {peso_adultos/cont_adultos if cont_adultos > 0 else 0:.2f} kg")
print(f"Viejos (60+): {peso_viejos/cont_viejos if cont_viejos > 0 else 0:.2f} kg")