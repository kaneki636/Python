# Entrada de datos
capital = float(input("Ingrese el capital a depositar: "))
tasa = float(input("Ingrese la tasa de interés (ejemplo 0.06): "))
semanas = int(input("Ingrese la duración en semanas: "))

# Convertir semanas a días
dias = semanas * 7

# Guardar el capital inicial para mostrarlo al final
capital_inicial = capital

# Encabezado de la tabla
print(f"\n{'Día':<10}{'Interés':<15}{'Capital Acumulado':<20}")
print("-" * 45)

# Calcular interés día por día
for dia in range(1, dias + 1):
    interes = (tasa * capital) / 365
    capital = capital + interes
    print(f"{dia:<10}{interes:<15.2f}{capital:<20.2f}")

# Resultados finales
print("-" * 45)
print(f"\nCapital inicial:    ${capital_inicial:.2f}")
print(f"Tasa de interés:    {tasa}")
print(f"Duración:           {semanas} semanas ({dias} días)")
print(f"Capital acumulado:  ${capital:.2f}")
print(f"Interés ganado:     ${capital - capital_inicial:.2f}")