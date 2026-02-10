cliente = input("Ingrese el nombre del cliente: ")
km = int(input("Ingrese el kilometraje del vehiculo: "))

precioFijo = 5000
valorKm_extra = 200 # Tarifa para km entre 300 y 1000
valorKm_largo = 150 # Tarifa para km mayores a 1000

# Estructura de condiciones
if km <= 300:
    totalPagar = precioFijo
    print(f"Cliente: {cliente}. Solo paga tarifa fija.")

elif 300 < km <= 1000:
    # Calculamos el excedente sobre los 300km
    excedente = km - 300
    totalPagar = precioFijo + (excedente * valorKm_extra)
    print(f"Su kilometraje es mayor a 300 y menor a 1000.")

else: # Caso para km > 1000
    excedente = km - 300
    totalPagar = precioFijo + (excedente * valorKm_largo)
    print(f"Su kilometraje es mayor a 1000.")

print(f"El cliente {cliente} tiene que cancelar: {totalPagar:,.2f} bolívares")