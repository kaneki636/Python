
deuda_pendiente = 12775
pago_actual = 100
diferencia = 125
contador_pagos = 0

print(f"{'Pago #':<10} | {'Monto Pago':<15} | {'Deuda Pendiente':<15}")
print("-" * 45)

# El ciclo continúa mientras todavía debamos dinero
while deuda_pendiente > 0:
    contador_pagos += 1
    
    deuda_pendiente = deuda_pendiente - pago_actual
    

    print(f"{contador_pagos:<10} | {pago_actual:<15.2f} | {max(0, deuda_pendiente):<15.2f}")
    

    ultimo_pago_realizado = pago_actual
    

    pago_actual = pago_actual + diferencia

print("-" * 45)
print(f"RESULTADO FINAL:")
print(f"Número de pagos realizados: {contador_pagos}")
print(f"Monto del último pago: {ultimo_pago_realizado} Bs.")