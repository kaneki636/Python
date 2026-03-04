def control_obesidad():
    MIEMBROS = 5
    BASCULAS = 10

    for i in range(1, MIEMBROS + 1):
        print(f"\n--- Miembro número {i} ---")
        peso_anterior = float(input("Ingrese su peso de la última reunión (kg): "))
        
        suma_pesos = 0
        print(f"Por favor, realice el pesaje en las {BASCULAS} básculas.")
        
        for j in range(1, BASCULAS + 1):
            peso_bascula = float(input(f"  Peso en báscula {j}: "))
            suma_pesos += peso_bascula
        
        # Calcular promedio actual
        peso_actual_promedio = suma_pesos / BASCULAS
        diferencia = peso_actual_promedio - peso_anterior
        
        # Determinar resultado
        if diferencia > 0:
            print(f"RESULTADO: SUBIÓ {diferencia:.2f} kilos.")
        elif diferencia < 0:
            # Usamos abs() para mostrar el valor positivo en el mensaje de "bajó"
            print(f"RESULTADO: BAJÓ {abs(diferencia):.2f} kilos.")
        else:
            print("RESULTADO: Se mantiene en el mismo peso.")

# Ejecutar el programa
control_obesidad()