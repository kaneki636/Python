# Inicializamos nuestros contadores y acumuladores
total_dias = 0
suma_maximas = 0
suma_minimas = 0
contador_errores = 0
total_ingresos = 0 # Para contar cuántas temperaturas individuales se intentaron meter

print("Ingrese las temperaturas (máx y min). Para terminar, ingrese 0 y 0.")

while True:
    print(f"\n--- Día {total_dias + 1} ---")
    t_max = float(input("Temperatura Máxima: "))
    t_min = float(input("Temperatura Mínima: "))
    
    # Condición de salida: si ambas son 0
    if t_max == 0 and t_min == 0:
        break
    
    # Cada vez que entra una pareja, es un día más
    total_dias = total_dias + 1
    
    # Validación Temperatura Máxima
    total_ingresos = total_ingresos + 1
    if 14 <= t_max <= 30:
        suma_maximas = suma_maximas + t_max
    else:
        contador_errores = contador_errores + 1
        print("¡Error! La temperatura máxima está fuera de rango (14-30°C)")

    # Validación Temperatura Mínima 
    total_ingresos = total_ingresos + 1
    if 14 <= t_min <= 30:
        suma_minimas = suma_minimas + t_min
    else:
        contador_errores = contador_errores + 1
        print("¡Error! La temperatura mínima está fuera de rango (14-30°C)")


print("\n" + "="*35)
print("REPORTE CLIMÁTICO FINAL")
print("="*35)

# g. Número de días
print(f"g. Número de días procesados: {total_dias}")

# h. Medias (Promedios)
#  calculamos si hubo días para evitar error de división por cero
if total_dias > 0:
    # Nota: El promedio se hace sobre el total de días
    media_max = suma_maximas / total_dias
    media_min = suma_minimas / total_dias
    print(f"h. Media de temperaturas máximas: {media_max:.2f}°C")
    print(f"   Media de temperaturas mínimas: {media_min:.2f}°C")

# i. Número de errores
print(f"i. Número de errores ingresados: {contador_errores}")

# j. Porcentaje de errores
if total_ingresos > 0:
    porcentaje_errores = (contador_errores / total_ingresos) * 100
    print(f"j. Porcentaje de errores: {porcentaje_errores:.2f}%")