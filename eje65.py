# Pedimos los datos básicos del trabajador
nombre = input("Nombre del trabajador: ")
cedula = input("Cédula o ID: ")
print("Cargos disponibles: 1-Obrero, 2-Administrativo, 3-Ejecutivo")
cargo = int(input("Ingrese el número del cargo: "))

# 1. Determinar el sueldo básico según el cargo
if cargo == 1:
    sueldo_basico = 100000
elif cargo == 2:
    sueldo_basico = 165500
elif cargo == 3:
    sueldo_basico = 250000
else:
    sueldo_basico = 0
    print("Cargo no válido.")

# Si el sueldo es válido, procedemos con los cálculos
if sueldo_basico > 0:
    # 2. Asignaciones (Lo que suma)
    hijos = int(input("¿Cuántos hijos tiene? "))
    if hijos > 5:
        hijos = 5  # El tope es 5 hijos según el problema
    
    # Cada hijo da 10%, entonces multiplicamos (10% * cantidad de hijos)
    aporte_hijos = sueldo_basico * (0.10 * hijos)
    
    asistencia = float(input("Días asistidos en el mes (0 a 30): "))
    # Si asistió más del 95% de 30 días (esto es > 28.5 días)
    if asistencia > (30 * 0.95):
        bono_asistencia = sueldo_basico * 0.05
    else:
        bono_asistencia = 0

    # 3. Deducciones (Lo que resta)
    caja_ahorro = sueldo_basico * 0.10
    seguro_social = sueldo_basico * 0.02
    
    # 4. Cálculo del Sueldo Neto
    # Sueldo Neto = Básico + Asignaciones - Deducciones
    sueldo_neto = sueldo_basico + aporte_hijos + bono_asistencia - caja_ahorro - seguro_social

    
    print("REGISTRO DE PAGO")
    print("="*40)
    print(f"Nombre:         {nombre}")
    print(f"Cédula:         {cedula}")
    print(f"Sueldo Básico:  {sueldo_basico}")
    print(f"Caja de Ahorro: {caja_ahorro} (Deducción)")
    print(f"Seguro Social:  {seguro_social} (Deducción)")
    print("-" * 20)
    print(f"SUELDO NETO:    {sueldo_neto}")
    print("="*40)