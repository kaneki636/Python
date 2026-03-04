num_estados = int(input("¿Cuántos estados? "))

for e in range(1, num_estados + 1):
    cod_estado = int(input("\nCódigo del estado (2 dígitos): "))
    nombre_estado = input("Nombre del estado: ")
    num_ciudades = int(input(f"¿Cuántas ciudades en {nombre_estado}? "))

    monto_neto_estado = 0
    ciudades_no_alcanzaron = 0
    ciudades_40_60 = 0

    for c in range(1, num_ciudades + 1):
        cod_ciudad = int(input(f"\n  Código de ciudad (3 dígitos, termina en {cod_estado}): "))

        while cod_ciudad % 100 != cod_estado:
            print(f"  Error: los últimos 2 dígitos deben ser {cod_estado}")
            cod_ciudad = int(input("  Código de ciudad: "))

        nombre_ciudad = input("  Nombre de la ciudad: ")
        cant_esperada = int(input("  Cantidad de unidades esperada: "))
        num_canales = int(input(f"  ¿Cuántos canales en {nombre_ciudad}? "))

        total_unidades_ciudad = 0
        monto_bruto_ciudad = 0
        comision_tienda = 0
        comision_calle = 0
        mayor_monto_neto_canal = 0
        cod_mayor_canal = 0
        menor_unidades_vendedor = float('inf')
        cod_menor_vendedor = 0

        for ch in range(1, num_canales + 1):
            cod_canal = int(input(f"\n    Código del canal (4 dígitos): "))
            num_vendedores = int(input(f"    ¿Cuántos vendedores en canal {cod_canal}? "))

            monto_neto_canal = 0

            for v in range(1, num_vendedores + 1):
                cod_vendedor = int(input(f"\n      Código vendedor (5 dígitos, 11=tienda/12=calle): "))
                tipo = cod_vendedor // 1000

                while tipo != 11 and tipo != 12:
                    print("      Error: primeros 2 dígitos deben ser 11 o 12")
                    cod_vendedor = int(input("      Código vendedor: "))
                    tipo = cod_vendedor // 1000

                unidades = int(input("      Unidades vendidas: "))
                monto = float(input("      Monto total vendido: "))

                if tipo == 11:
                    comision = monto * 0.10
                    comision_tienda += comision
                else:
                    comision = monto * 0.15
                    comision_calle += comision

                neto_vendedor = monto - comision
                monto_neto_canal += neto_vendedor
                total_unidades_ciudad += unidades
                monto_bruto_ciudad += monto

                if unidades < menor_unidades_vendedor:
                    menor_unidades_vendedor = unidades
                    cod_menor_vendedor = cod_vendedor

            if monto_neto_canal > mayor_monto_neto_canal:
                mayor_monto_neto_canal = monto_neto_canal
                cod_mayor_canal = cod_canal

        monto_neto_ciudad = monto_bruto_ciudad - comision_tienda - comision_calle

        print(f"\n  ====== RESULTADOS CIUDAD: {nombre_ciudad} ======")
        print(f"  Código: {cod_ciudad}")
        print(f"  Total unidades vendidas: {total_unidades_ciudad}")
        print(f"  Monto bruto: ${monto_bruto_ciudad:.2f}")
        print(f"  Comisión tienda: ${comision_tienda:.2f}")
        print(f"  Comisión calle: ${comision_calle:.2f}")
        print(f"  Canal con mayor monto neto: {cod_mayor_canal}")
        print(f"  Vendedor con menor unidades: {cod_menor_vendedor}")

        monto_neto_estado += monto_neto_ciudad

        if total_unidades_ciudad < cant_esperada:
            ciudades_no_alcanzaron += 1

        if cant_esperada > 0:
            exceso = ((total_unidades_ciudad - cant_esperada) / cant_esperada) * 100
            if 40 <= exceso <= 60:
                ciudades_40_60 += 1

    porc_no_alcanzaron = (ciudades_no_alcanzaron / num_ciudades) * 100

    print(f"\n{'='*50}")
    print(f"RESULTADOS ESTADO: {nombre_estado}")
    print(f"{'='*50}")
    print(f"Código: {cod_estado}")
    print(f"Monto neto vendido: ${monto_neto_estado:.2f}")
    print(f"Ciudades que no alcanzaron meta: {porc_no_alcanzaron:.2f}%")
    print(f"Ciudades entre 40-60% por encima de meta: {ciudades_40_60}")