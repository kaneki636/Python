m = int(input("Ingrese la cantidad total de empleados (M): "))

total_v_tipo1 = total_v_tipo2 = total_v_tipo3 = 0
total_extranjeros_impar = 0
suma_edades = 0
total_nomina_general = 0

for i in range(1, m + 1):
    print(f"\n--- Datos del Empleado {i} ---")
    nombre = input("Nombre: ")
    nacionalidad = input("Nacionalidad (V/E): ").upper()
    edad = int(input("Edad: "))
    tipo = int(input("Tipo de empleado (1, 2, 3): "))
    horas = float(input("Horas trabajadas: "))

    # a. Cálculo del Sueldo Básico (Bruto)
    if tipo == 1:
        pago_hora = 5000
    elif tipo == 2:
        pago_hora = 10000
    else:
        pago_hora = 15000
    
    sueldo_basico = horas * pago_hora

    # b. Seguro Social (3% si el sueldo > 100,000)
    descuento_ss = 0
    if sueldo_basico > 100000:
        descuento_ss = sueldo_basico * 0.03
    
    sueldo_neto = sueldo_basico - descuento_ss

    # c. Conteo de venezolanos por tipo
    if nacionalidad == "V":
        if tipo == 1: total_v_tipo1 += 1
        elif tipo == 2: total_v_tipo2 += 1
        elif tipo == 3: total_v_tipo3 += 1

    # d. Extranjeros con edad impar
    if nacionalidad == "E" and edad % 2 != 0:
        total_extranjeros_impar += 1

    # e. Acumulado para promedio de edad
    suma_edades += edad

    # f. Acumulado total a pagar
    total_nomina_general += sueldo_neto

    print(f"Sueldo Bruto: Bs. {sueldo_basico:,.2f}")
    print(f"Sueldo Neto (con SS): Bs. {sueldo_neto:,.2f}")


print(f"Venezolanos Tipo 1: {total_v_tipo1}")
print(f"Venezolanos Tipo 2: {total_v_tipo2}")
print(f"Venezolanos Tipo 3: {total_v_tipo3}")
print(f"Extranjeros con edad impar: {total_extranjeros_impar}")
print(f"Promedio de edad general: {suma_edades / m if m > 0 else 0:.2f} años")
print(f"Total general a pagar en nómina: Bs. {total_nomina_general:,.2f}")