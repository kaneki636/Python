num_obreros = int(input("¿Cuántos obreros son? "))
meta = int(input("¿Cuál es la meta semanal? "))

alcanzaron_meta = 0
mayor_produccion = 0
nombre_mayor = ""
suma_total = 0

for i in range(1, num_obreros + 1):
    print(f"\n--- Obrero {i} ---")
    nombre = input("Nombre: ")
    total_obrero = 0

    for dia in range(1, 7):
        produccion = int(input(f"  Producción día {dia}: "))
        total_obrero += produccion

    porcentaje = (total_obrero / meta) * 100

    print(f"\n  Nombre: {nombre}")
    print(f"  Total semanal: {total_obrero}")
    print(f"  Porcentaje vs meta: {porcentaje:.2f}%")

    if total_obrero >= meta:
        alcanzaron_meta += 1

    if total_obrero > mayor_produccion:
        mayor_produccion = total_obrero
        nombre_mayor = nombre

    suma_total += total_obrero

promedio = suma_total / num_obreros
porcentaje_meta = (alcanzaron_meta / num_obreros) * 100

print(f"Obreros que alcanzaron la meta: {porcentaje_meta:.2f}%")
print(f"Obrero que más produjo: {nombre_mayor} con {mayor_produccion} bloques")
print(f"Promedio de producción: {promedio:.2f} bloques")