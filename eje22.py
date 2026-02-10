
P = float(input("Ingrese el precio de contado (P): "))
T = float(input("Ingrese el monto de cada cuota (T): "))

total_cuotas = T * 12
recargo_bs = total_cuotas - P
porcentaje_recargo = (recargo_bs * 100) / P

print(f"El total pagado por cuotas es: {total_cuotas}")
print(f"El porcentaje de recargo es: {porcentaje_recargo}%")