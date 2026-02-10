
lectura_anterior = float(input("Ingrese la lectura anterior: "))
lectura_actual = float(input("Ingrese la lectura actual: "))
costo_aseo = float(input("Ingrese el monto por servicio de aseo urbano: "))

consumo = lectura_actual - lectura_anterior
print(f"Consumo total: {consumo} Kwh")


if consumo <= 100:

    costo_electricidad = 2622.00
else:
    if consumo <= 300:
        precio_kwh = 79.78
    elif consumo <= 500:
        precio_kwh = 89.52
    else:
        precio_kwh = 97.95

    costo_electricidad = consumo * precio_kwh


total_pagar = costo_electricidad + costo_aseo

print(f"Monto por electricidad: {costo_electricidad:,.2f} Bs.")
print(f"Monto por aseo urbano: {costo_aseo:,.2f} Bs.")
print(f"TOTAL A PAGAR: {total_pagar:,.2f} Bs.")