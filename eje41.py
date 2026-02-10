# 1. Entrada de datos
hectareas = float(input("Ingrese el número de hectáreas del bosque: "))

# Conversión a metros cuadrados 
metros_cuadrados = hectareas * 10000

# 2. Determinar porcentajes según la superficie
if metros_cuadrados > 1000000:
    porc_pino = 0.70
    porc_oyamel = 0.20
    porc_cedro = 0.10
else:
    porc_pino = 0.50
    porc_oyamel = 0.30
    porc_cedro = 0.20

# 3. Calcular superficie destinada a cada árbol
m2_pino = metros_cuadrados * porc_pino
m2_oyamel = metros_cuadrados * porc_oyamel
m2_cedro = metros_cuadrados * porc_cedro


num_pinos = (m2_pino * 8) / 10
num_oyameles = (m2_oyamel * 15) / 15
num_cedros = (m2_cedro * 10) / 18

# 5. Mostrar resultados
print(f"\n--- Plan de Reforestación para {hectareas} hectáreas ---")
print(f"Superficie total: {metros_cuadrados:,.2f} m2")

print(f"Cantidad de Pinos:   {int(num_pinos):,}")
print(f"Cantidad de Oyameles: {int(num_oyameles):,}")
print(f"Cantidad de Cedros:   {int(num_cedros):,}")