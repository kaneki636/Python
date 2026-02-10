
capital_actual = float(input("Ingrese el capital actual de la empresa: "))

prestamo = 0

# 2. Lógica para determinar el préstamo y el nuevo saldo
if capital_actual < 0:
    # Caso negativo: Pedir hasta llegar a 10,000
    # Ejemplo: si debe 2,000 (-2000), el préstamo debe ser 12,000
    prestamo = 10000 - capital_actual
    saldo_final = 10000
elif capital_actual <= 20000:
    # Caso entre 0 y 20,000: Pedir hasta llegar a 20,000
    prestamo = 20000 - capital_actual
    saldo_final = 20000
else:
    # Caso superior a 20,000: No pide nada
    prestamo = 0
    saldo_final = capital_actual

# 3. Reparto del presupuesto

equipo_computo = 5000
mobiliario = 2000
resto = saldo_final - (equipo_computo + mobiliario)


insumos = resto / 2
incentivos = resto / 2


if prestamo > 0:
    print(f"Monto del préstamo a solicitar: ${prestamo:,.2f}")
else:
    print("No es necesario solicitar un préstamo bancario.")

print(f"Saldo total para presupuesto: ${saldo_final:,.2f}")
print(f"Cantidad para Insumos: ${insumos:,.2f}")
print(f"Cantidad para Incentivos al personal: ${incentivos:,.2f}")