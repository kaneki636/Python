# Inicializamos variables globales para el reporte del día
total_pasajeros_dia = 0
pasajeros_cero_pago = 0

cant_vuelos = int(input("¿Cuántos vuelos se procesarán hoy? "))

# CICLO 1: Vuelos
for v in range(cant_vuelos):
    print(f"\n--- DATOS DEL VUELO {v + 1} ---")
    num_vuelo = input("Número de vuelo: ")
    cant_pasajeros = int(input(f"¿Cuántos pasajeros hay en el vuelo {num_vuelo}? "))
    
    monto_total_vuelo = 0
    
    # Variables para el pasajero con mayor y menor peso del VUELO
    nombre_mayor = ""; abordo_mayor = ""; max_peso_vuelo = -1.0
    nombre_menor = ""; abordo_menor = ""; min_peso_vuelo = 99999.0
    
    # CICLO 2: Pasajeros
    for p in range(cant_pasajeros):
        total_pasajeros_dia += 1
        print(f"\n> Pasajero {p + 1}:")
        nombre = input("   Nombre: ")
        cod_abordo = input("   Código de abordo: ")
        cant_maletas = int(input("   ¿Cuántas maletas tiene? "))
        
        peso_total_pasajero = 0
        monto_pasajero = 0
        
        # Variables para la maleta más pesada del PASAJERO
        maleta_mas_pesada_cod = ""
        max_peso_maleta = -1.0
        
        # CICLO 3: Maletas
        for m in range(cant_maletas):
            cod_maleta = input(f"      Código maleta {m + 1}: ")
            peso_m = float(input(f"      Peso maleta {m + 1} (Kgs): "))
            
            peso_total_pasajero += peso_m
            
            # Cálculo de tarifa por maleta según la tabla
            if peso_m > 15:
                tarifa = 2500
            elif peso_m > 12:
                tarifa = 2000
            elif peso_m > 9:
                tarifa = 1500
            elif peso_m > 6:
                tarifa = 1200
            elif peso_m > 3:
                tarifa = 600
            else:
                tarifa = 0
                
            monto_pasajero += (peso_m * tarifa)
            
            # ii. Buscar maleta con mayor peso del pasajero
            if peso_m > max_peso_maleta:
                max_peso_maleta = peso_m
                maleta_mas_pesada_cod = cod_maleta
        
        # i. Imprimir reporte por pasajero
        print(f"\n   [REPORTE PASAJERO]")
        print(f"   Vuelo: {num_vuelo} | Abordo: {cod_abordo} | Nombre: {nombre}")
        print(f"   Total Kgs: {peso_total_pasajero} | Monto: ${monto_pasajero}")
        
        # ii. Imprimir maleta más pesada
        print(f"   Maleta más pesada: {maleta_mas_pesada_cod} ({max_peso_maleta} Kgs)")
        
        # iii. Lógica para mayor y menor peso del vuelo
        if peso_total_pasajero > max_peso_vuelo:
            max_peso_vuelo = peso_total_pasajero
            nombre_mayor = nombre
            abordo_mayor = cod_abordo
            
        if peso_total_pasajero < min_peso_vuelo:
            min_peso_vuelo = peso_total_pasajero
            nombre_menor = nombre
            abordo_menor = cod_abordo
            
        # v. Acumular pasajeros que no pagan
        if monto_pasajero == 0:
            pasajeros_cero_pago += 1
            
        monto_total_vuelo += monto_pasajero

    print(f"\n=== RESUMEN VUELO {num_vuelo} ===")
    print(f"Monto total recaudado: ${monto_total_vuelo}")
    print(f"Pasajero con MÁS peso: {nombre_mayor} ({abordo_mayor}) - {max_peso_vuelo} Kgs")
    print(f"Pasajero con MENOS peso: {nombre_menor} ({abordo_menor}) - {min_peso_vuelo} Kgs")


if total_pasajeros_dia > 0:
    porcentaje_gratis = (pasajeros_cero_pago / total_pasajeros_dia) * 100
    print(f"\n*** ESTADÍSTICA GLOBAL ***")
    print(f"Porcentaje de pasajeros que no pagaron: {porcentaje_gratis:.2f}%")